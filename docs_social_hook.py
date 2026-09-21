from __future__ import annotations

import html
import json

from properdocs.plugins import event_priority


def _title(page, config) -> str:
    name = config.site_name
    if page.is_homepage:
        return name
    page_title = (page.meta or {}).get("title") or page.title
    if page_title:
        return f"{page_title} - {name}"
    return name


def _desc(page, config) -> str:
    return (page.meta or {}).get("description") or config.site_description or ""


@event_priority(50)
def on_post_page(output: str, page, config):
    at = output.find("</head>")
    if at < 0 or not config.site_url:
        return output

    site = config.site_url.rstrip("/")
    title = html.escape(_title(page, config), quote=True)
    desc = html.escape(_desc(page, config), quote=True)
    image = "https://opengraph.githubassets.com/1/pytdbot/client"
    url = html.escape(page.canonical_url or f"{site}/", quote=True)
    name = html.escape(config.site_name, quote=True)

    bits = [
        '<meta property="og:type" content="website" />',
        f'<meta property="og:title" content="{title}" />',
        f'<meta property="og:site_name" content="{name}" />',
        f'<meta property="og:description" content="{desc}" />',
        f'<meta property="og:url" content="{url}" />',
        f'<meta property="og:image" content="{image}" />',
        '<meta property="og:image:type" content="image/png" />',
        '<meta property="og:image:width" content="1200" />',
        '<meta property="og:image:height" content="630" />',
        '<meta name="twitter:card" content="summary_large_image" />',
        f'<meta name="twitter:title" content="{title}" />',
        f'<meta name="twitter:description" content="{desc}" />',
        f'<meta name="twitter:image" content="{image}" />',
    ]
    if page.is_homepage:
        bits.insert(
            0,
            '<script type="application/ld+json">'
            + json.dumps(
                {
                    "@context": "https://schema.org",
                    "@type": "WebSite",
                    "name": config.site_name,
                    "alternateName": ["Pytdbot", "pytdbot"],
                    "url": f"{site}/",
                },
                ensure_ascii=False,
            )
            + "</script>",
        )
    return output[:at] + "\n".join(bits) + "\n" + output[at:]
