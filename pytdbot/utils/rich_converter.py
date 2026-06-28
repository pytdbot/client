from ..types import (
    DateTimeFormattingTypeAbsolute,
    DateTimeFormattingTypeRelative,
    DateTimePartPrecisionLong,
    DateTimePartPrecisionShort,
    PageBlockAnchor,
    PageBlockAnimation,
    PageBlockAudio,
    PageBlockBlockQuote,
    PageBlockCaption,
    PageBlockCollage,
    PageBlockDetails,
    PageBlockDivider,
    PageBlockFooter,
    PageBlockHorizontalAlignmentCenter,
    PageBlockHorizontalAlignmentLeft,
    PageBlockHorizontalAlignmentRight,
    PageBlockList,
    PageBlockMap,
    PageBlockMathematicalExpression,
    PageBlockParagraph,
    PageBlockPhoto,
    PageBlockPreformatted,
    PageBlockPullQuote,
    PageBlockSectionHeading,
    PageBlockSlideshow,
    PageBlockTable,
    PageBlockVerticalAlignmentBottom,
    PageBlockVerticalAlignmentMiddle,
    PageBlockVerticalAlignmentTop,
    PageBlockVideo,
    PageBlockVoiceNote,
    RichMessage,
    RichTextAnchor,
    RichTextAnchorLink,
    RichTextBankCardNumber,
    RichTextBold,
    RichTextBotCommand,
    RichTextCashtag,
    RichTextCustomEmoji,
    RichTextDateTime,
    RichTextEmailAddress,
    RichTextFixed,
    RichTextHashtag,
    RichTextItalic,
    RichTextMarked,
    RichTextMathematicalExpression,
    RichTextMention,
    RichTextMentionName,
    RichTextPhoneNumber,
    RichTextPlain,
    RichTextReference,
    RichTextReferenceLink,
    RichTexts,
    RichTextSpoiler,
    RichTextStrikethrough,
    RichTextSubscript,
    RichTextSuperscript,
    RichTextUnderline,
    RichTextUrl,
)
from .rich_messages import (
    anchor,
    aside,
    audio,
    blockquote,
    details,
    email_link,
    figcaption,
    figure,
    footer,
    heading,
    horizontal_rule,
    image,
    in_doc_link,
    list_item,
    marked,
    ordered_list,
    paragraph,
    phone,
    subscript,
    superscript,
    table,
    table_cell,
    table_header_cell,
    table_row,
    tag,
    tg_collage,
    tg_map,
    tg_math,
    tg_math_block,
    tg_reference,
    tg_slideshow,
    tg_time,
    unordered_list,
    video,
)
from .text_format import (
    bold,
    code,
    custom_emoji,
    hyperlink,
    italic,
    mention,
    spoiler,
    strikethrough,
    underline,
)

H_ALIGN = {
    PageBlockHorizontalAlignmentLeft.getType(): "left",
    PageBlockHorizontalAlignmentCenter.getType(): "center",
    PageBlockHorizontalAlignmentRight.getType(): "right",
}

V_ALIGN = {
    PageBlockVerticalAlignmentTop.getType(): "top",
    PageBlockVerticalAlignmentMiddle.getType(): "middle",
    PageBlockVerticalAlignmentBottom.getType(): "bottom",
}

DATE_FORMAT = {
    DateTimePartPrecisionShort.getType(): "d",
    DateTimePartPrecisionLong.getType(): "D",
}

TIME_FORMAT = {
    DateTimePartPrecisionShort.getType(): "t",
    DateTimePartPrecisionLong.getType(): "T",
}


def _datetime_format(ft):
    if ft is None:
        return ""

    if isinstance(ft, DateTimeFormattingTypeRelative):
        return "r"

    if isinstance(ft, DateTimeFormattingTypeAbsolute):
        parts = ""
        if ft.show_day_of_week:
            parts = "w"

        dp = ft.date_precision.getType() if ft.date_precision else ""
        tp = ft.time_precision.getType() if ft.time_precision else ""

        dd = DATE_FORMAT.get(dp)
        tt = TIME_FORMAT.get(tp)

        if dd:
            parts += dd
        if tt:
            parts += tt

        return parts

    return ""


def _get_file_url(media_obj, file_url_func):
    if not media_obj:
        return ""

    t = media_obj.getType()
    if t == "video":
        file_obj = media_obj.video
    elif t == "audio":
        file_obj = media_obj.audio
    elif t == "voiceNote":
        file_obj = media_obj.voice
    elif t == "animation":
        file_obj = media_obj.animation
    elif t == "photo":
        file_obj = media_obj.sizes[-1].photo
    else:
        return ""

    if file_url_func:
        return file_url_func(media_obj)

    return file_obj.remote.id or ""


def _rt(rt, f):
    if rt is None:
        return ""

    t = rt.getType()
    h = _RT_HANDLERS.get(t)

    return h(rt, f) if h else ""


def _rt_plain(rt, _):
    return rt.text or ""


def _rt_child(fn):
    def h(rt, f):
        return fn(_rt(rt.text, f))

    return h


def _rt_child_escaped(fn):
    def h(rt, f):
        return fn(_rt(rt.text, f), html=True, escape=False)

    return h


def _rt_passthrough(rt, f):
    return _rt(rt.text, f)


def _rt_url(rt, f):
    return hyperlink(_rt(rt.text, f), rt.url or "", html=True, escape=False)


def _rt_email(rt, f):
    return email_link(rt.email_address or "", _rt(rt.text, f))


def _rt_phone(rt, f):
    return phone(rt.phone_number or "", _rt(rt.text, f))


def _rt_anchor(rt, _):
    return anchor(rt.name or "")


def _rt_anchor_link(rt, f):
    return in_doc_link(rt.anchor_name or "", _rt(rt.text, f))


def _rt_ref_link(rt, f):
    return tag("a", _rt(rt.text, f), href=rt.url or "")


def _rt_reference(rt, f):
    return tg_reference(rt.name or "", _rt(rt.text, f))


def _rt_emoji(rt, _):
    return custom_emoji(rt.alternative_text or "", rt.custom_emoji_id, html=True)


def _rt_time(rt, f):
    return tg_time(
        rt.unix_time or 0, _datetime_format(rt.formatting_type), _rt(rt.text, f)
    )


def _rt_math(rt, _):
    return tg_math(rt.expression or "")


def _rt_mention_name(rt, f):
    return mention(_rt(rt.text, f), rt.user_id, html=True, escape=False)


def _rt_texts(rt, f):
    return "".join(_rt(x, f) for x in (rt.texts or []))


_RT_HANDLERS = {
    RichTextPlain.getType(): _rt_plain,
    RichTextBold.getType(): _rt_child_escaped(bold),
    RichTextItalic.getType(): _rt_child_escaped(italic),
    RichTextUnderline.getType(): _rt_child_escaped(underline),
    RichTextStrikethrough.getType(): _rt_child_escaped(strikethrough),
    RichTextFixed.getType(): _rt_child_escaped(code),
    RichTextSpoiler.getType(): _rt_child_escaped(spoiler),
    RichTextMarked.getType(): _rt_child(marked),
    RichTextSubscript.getType(): _rt_child(subscript),
    RichTextSuperscript.getType(): _rt_child(superscript),
    RichTextUrl.getType(): _rt_url,
    RichTextEmailAddress.getType(): _rt_email,
    RichTextPhoneNumber.getType(): _rt_phone,
    RichTextAnchor.getType(): _rt_anchor,
    RichTextAnchorLink.getType(): _rt_anchor_link,
    RichTextReferenceLink.getType(): _rt_ref_link,
    RichTextReference.getType(): _rt_reference,
    RichTextCustomEmoji.getType(): _rt_emoji,
    RichTextDateTime.getType(): _rt_time,
    RichTextMathematicalExpression.getType(): _rt_math,
    RichTextMention.getType(): _rt_passthrough,
    RichTextMentionName.getType(): _rt_mention_name,
    RichTextHashtag.getType(): _rt_passthrough,
    RichTextCashtag.getType(): _rt_passthrough,
    RichTextBotCommand.getType(): _rt_passthrough,
    RichTextBankCardNumber.getType(): _rt_passthrough,
    RichTexts.getType(): _rt_texts,
}


def _caption_html(cap, f):
    if cap is None:
        return ""

    if isinstance(cap, PageBlockCaption):
        text = _rt(cap.text, f)
        credit = cap.credit

        if credit:
            text += tag("cite", _rt(credit, f))
        return text

    return _rt(cap, f)


def _photo_url(photo, f):
    if not photo:
        return ""

    return _get_file_url(photo, f)


def _media_fig(media_tag, cap, f):
    cap_html = _caption_html(cap, f)
    if cap_html:
        return figure(media_tag, figcaption(cap_html))

    return figure(media_tag)


def _list_item(item, f):
    inner = _blocks(item.blocks, f)
    if item.has_checkbox:
        return list_item(inner, checked=item.is_checked)

    return list_item(inner)


def _table_cell_html(cell, f):
    cs = cell.colspan
    rs = cell.rowspan

    align = H_ALIGN.get(cell.align.getType()) if cell.align else None
    valign = V_ALIGN.get(cell.valign.getType()) if cell.valign else None

    fn = table_header_cell if cell.is_header else table_cell
    return fn(
        _rt(cell.text, f),
        colspan=cs if cs != 1 else None,
        rowspan=rs if rs != 1 else None,
        align=align,
        valign=valign,
    )


def _blocks(blocks, f):
    if not blocks:
        return ""

    return "".join(_block(b, f) for b in blocks)


def _block(b, f):
    t = b.getType()
    h = _BLOCK_HANDLERS.get(t)
    return h(b, f) if h else ""


def _bk_paragraph(b, f):
    return paragraph(_rt(b.text, f))


def _bk_heading(b, f):
    return heading(b.size or 1, _rt(b.text, f))


def _bk_anchor(b, _):
    return anchor(b.name or "")


def _bk_preformatted(b, f):
    lang = b.language or ""
    text = _rt(b.text, f)

    if lang:
        return tag("pre", tag("code", text, **{"class": f"language-{lang}"}))

    return tag("pre", text)


def _bk_footer(b, f):
    return footer(_rt(b.footer, f))


def _bk_divider(_, __):
    return horizontal_rule()


def _bk_list(b, f):
    items = b.items or []
    if any(it.has_checkbox for it in items):
        return tag("ul", *(_list_item(it, f) for it in items))

    first = items[0] if items else None
    first_type = first.type if first else ""
    if first_type:
        return ordered_list(
            *(_list_item(it, f) for it in items),
            start=first.value or 1,
            type=first_type,
        )

    return unordered_list(*(_list_item(it, f) for it in items))


def _bk_blockquote(b, f):
    inner = _blocks(b.blocks, f)
    credit = b.credit

    return blockquote(inner, cite=_rt(credit, f) if credit else None)


def _bk_pullquote(b, f):
    credit = b.credit

    return aside(_rt(b.text, f), cite=_rt(credit, f) if credit else None)


def _bk_photo(b, f):
    return _media_fig(
        image(_photo_url(b.photo, f), spoiler=b.has_spoiler), b.caption, f
    )


def _bk_video(b, f):
    return _media_fig(
        video(_get_file_url(b.video, f), spoiler=b.has_spoiler), b.caption, f
    )


def _bk_audio(b, f):
    return _media_fig(audio(_get_file_url(b.audio, f)), b.caption, f)


def _bk_voice(b, f):
    return _media_fig(audio(_get_file_url(b.voice_note, f)), b.caption, f)


def _bk_animation(b, f):
    return _media_fig(
        video(_get_file_url(b.animation, f), spoiler=b.has_spoiler), b.caption, f
    )


def _bk_map(b, f):
    loc = b.location

    return _media_fig(
        tg_map(loc.latitude or 0, loc.longitude or 0, b.zoom or 14), b.caption, f
    )


def _bk_collage(b, f):
    return tg_collage(_blocks(b.blocks, f), caption=_caption_html(b.caption, f) or None)


def _bk_slideshow(b, f):
    return tg_slideshow(
        _blocks(b.blocks, f), caption=_caption_html(b.caption, f) or None
    )


def _bk_table(b, f):
    cells = b.cells or []
    rows = [table_row(*(_table_cell_html(c, f) for c in row)) for row in cells]

    return table(
        *rows,
        bordered=b.is_bordered,
        striped=b.is_striped,
        caption=_caption_html(b.caption, f) or None,
    )


def _bk_details(b, f):
    return details(_blocks(b.blocks, f), summary=_rt(b.header, f), open=b.is_open)


def _bk_math(b, _):
    return tg_math_block(b.expression or "")


_BLOCK_HANDLERS = {
    PageBlockParagraph.getType(): _bk_paragraph,
    PageBlockSectionHeading.getType(): _bk_heading,
    PageBlockAnchor.getType(): _bk_anchor,
    PageBlockPreformatted.getType(): _bk_preformatted,
    PageBlockFooter.getType(): _bk_footer,
    PageBlockDivider.getType(): _bk_divider,
    PageBlockList.getType(): _bk_list,
    PageBlockBlockQuote.getType(): _bk_blockquote,
    PageBlockPullQuote.getType(): _bk_pullquote,
    PageBlockPhoto.getType(): _bk_photo,
    PageBlockVideo.getType(): _bk_video,
    PageBlockAudio.getType(): _bk_audio,
    PageBlockVoiceNote.getType(): _bk_voice,
    PageBlockAnimation.getType(): _bk_animation,
    PageBlockMap.getType(): _bk_map,
    PageBlockCollage.getType(): _bk_collage,
    PageBlockSlideshow.getType(): _bk_slideshow,
    PageBlockTable.getType(): _bk_table,
    PageBlockDetails.getType(): _bk_details,
    PageBlockMathematicalExpression.getType(): _bk_math,
}


def rich_message_to_html(message: RichMessage, file_url_func=None):
    r"""Convert a TDLib rich message object to HTML

    Parameters:
        message (:class:`pytdbot.types.RichMessage`):
            The rich message object containing rich blocks

        file_url_func (``callable``, *optional*):
            A function that receives the full media object (:class:`pytdbot.types.Photo`, :class:`pytdbot.types.Video`, :class:`pytdbot.types.Audio`,
            :class:`pytdbot.types.VoiceNote`, or :class:`pytdbot.types.Animation`) and returns an HTTP/HTTPS URL string.
            If ``None``, file IDs are used as ``src`` values. (file_id media send is not supported by Telegram)

    Returns:
        :py:class:`str`: The rendered HTML string
    """

    return _blocks(message.blocks, file_url_func)
