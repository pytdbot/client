from ..types import (
    ButtonStyleDanger,
    ButtonStyleLink,
    ButtonStylePrimary,
    ButtonStyleSuccess,
    InlineKeyboardButtonTypeCallback,
    InlineKeyboardButtonTypeCallbackWithPassword,
    InlineKeyboardButtonTypeCopyText,
    InlineKeyboardButtonTypeDisabled,
    InlineKeyboardButtonTypeLoginUrl,
    InlineKeyboardButtonTypeSwitchInline,
    InlineKeyboardButtonTypeUrl,
    InlineKeyboardButtonTypeUser,
    InlineKeyboardButtonTypeWebApp,
    InputAnimation,
    InputAudio,
    InputDocument,
    InputFileId,
    InputFileRemote,
    InputMessageAnimation,
    InputMessageAudio,
    InputMessageDocument,
    InputMessagePhoto,
    InputMessageVideo,
    InputMessageVoiceNote,
    InputPhoto,
    InputRichMessageMedia,
    InputVideo,
    InputVoiceNote,
    PageBlockAnchor,
    PageBlockAnimation,
    PageBlockAudio,
    PageBlockBlockQuote,
    PageBlockButtonRow,
    PageBlockCaption,
    PageBlockCollage,
    PageBlockDetails,
    PageBlockDivider,
    PageBlockDocument,
    PageBlockExpandableBlockQuote,
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
    RichTextButton,
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
    TargetChatChosen,
    TargetChatCurrent,
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
    tg_button,
    tg_button_row,
    tg_collage,
    tg_document,
    tg_map,
    tg_math,
    tg_math_block,
    tg_reference,
    tg_slideshow,
    tg_time,
    unordered_list,
    video,
)
from .strings import create_extra_id
from .text_format import (
    _datetime_format,
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


def _media_id():
    return create_extra_id()


def _input_file(file_obj):
    if not file_obj:
        return None

    if file_obj.remote and file_obj.remote.id:
        return InputFileRemote(id=file_obj.remote.id)

    if file_obj.id:
        return InputFileId(id=file_obj.id)

    return None


def _input_message(media_obj, has_spoiler=False):
    if not media_obj:
        return None

    t = media_obj.getType()

    if t == "photo":
        if not media_obj.sizes:
            return None
        size = media_obj.sizes[-1]
        inp = _input_file(size.photo)
        if not inp:
            return None
        return InputMessagePhoto(
            photo=InputPhoto(photo=inp, width=size.width or 0, height=size.height or 0),
            has_spoiler=has_spoiler,
        )

    if t == "video":
        inp = _input_file(media_obj.video)
        if not inp:
            return None
        return InputMessageVideo(
            video=InputVideo(
                video=inp,
                duration=media_obj.duration or 0,
                width=media_obj.width or 0,
                height=media_obj.height or 0,
                supports_streaming=media_obj.supports_streaming or False,
            ),
            has_spoiler=has_spoiler,
        )

    if t == "audio":
        inp = _input_file(media_obj.audio)
        if not inp:
            return None
        return InputMessageAudio(
            audio=InputAudio(
                audio=inp,
                duration=media_obj.duration or 0,
                title=media_obj.title or "",
                performer=media_obj.performer or "",
            )
        )

    if t == "voiceNote":
        inp = _input_file(media_obj.voice)
        if not inp:
            return None
        return InputMessageVoiceNote(
            voice_note=InputVoiceNote(
                voice_note=inp,
                duration=media_obj.duration or 0,
                waveform=media_obj.waveform or b"",
            )
        )

    if t == "animation":
        inp = _input_file(media_obj.animation)
        if not inp:
            return None
        return InputMessageAnimation(
            animation=InputAnimation(
                animation=inp,
                duration=media_obj.duration or 0,
                width=media_obj.width or 0,
                height=media_obj.height or 0,
            ),
            has_spoiler=has_spoiler,
        )

    if t == "document":
        inp = _input_file(media_obj.document)
        if not inp:
            return None
        return InputMessageDocument(document=InputDocument(document=inp))

    return None


class _MediaCollector:
    __slots__ = ("items",)

    def __init__(self):
        self.items = []

    def add(self, kind, media_obj, has_spoiler=False):
        content = _input_message(media_obj, has_spoiler=has_spoiler)
        if not content:
            return ""

        media_id = _media_id()
        self.items.append(InputRichMessageMedia(id=media_id, media=content))
        return f"tg://{kind}?id={media_id}"


def _rt(rt, ctx):
    if rt is None:
        return ""

    t = rt.getType()
    h = _RT_HANDLERS.get(t)

    return h(rt, ctx) if h else ""


def _rt_plain(rt, _):
    return rt.text or ""


def _rt_child(fn):
    def h(rt, ctx):
        return fn(_rt(rt.text, ctx))

    return h


def _rt_child_escaped(fn):
    def h(rt, ctx):
        return fn(_rt(rt.text, ctx), html=True, escape=False)

    return h


def _rt_passthrough(rt, ctx):
    return _rt(rt.text, ctx)


def _rt_url(rt, ctx):
    return hyperlink(_rt(rt.text, ctx), rt.url or "", html=True, escape=False)


def _rt_email(rt, ctx):
    return email_link(rt.email_address or "", _rt(rt.text, ctx))


def _rt_phone(rt, ctx):
    return phone(rt.phone_number or "", _rt(rt.text, ctx))


def _rt_anchor(rt, _):
    return anchor(rt.name or "")


def _rt_anchor_link(rt, ctx):
    return in_doc_link(rt.anchor_name or "", _rt(rt.text, ctx))


def _rt_ref_link(rt, ctx):
    return tag("a", _rt(rt.text, ctx), href=rt.url or "")


def _rt_reference(rt, ctx):
    return tg_reference(rt.name or "", _rt(rt.text, ctx))


def _rt_emoji(rt, _):
    return custom_emoji(rt.alternative_text or "", rt.custom_emoji_id, html=True)


def _rt_time(rt, ctx):
    return tg_time(
        rt.unix_time or 0, _datetime_format(rt.formatting_type), _rt(rt.text, ctx)
    )


def _rt_math(rt, _):
    return tg_math(rt.expression or "")


def _rt_mention_name(rt, ctx):
    return mention(_rt(rt.text, ctx), rt.user_id, html=True, escape=False)


def _rt_texts(rt, ctx):
    return "".join(_rt(x, ctx) for x in (rt.texts or []))


def _rt_button(rt, ctx):
    return _inline_button_html(rt.button, ctx)


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
    RichTextButton.getType(): _rt_button,
}


def _caption_html(cap, ctx):
    if cap is None:
        return ""

    if isinstance(cap, PageBlockCaption):
        text = _rt(cap.text, ctx)
        credit = cap.credit

        if credit:
            text += tag("cite", _rt(credit, ctx))
        return text

    return _rt(cap, ctx)


def _media_fig(media_tag, cap, ctx):
    cap_html = _caption_html(cap, ctx)
    if cap_html:
        return figure(media_tag, figcaption(cap_html))

    return figure(media_tag)


def _list_item(item, ctx):
    inner = _blocks(item.blocks, ctx)
    if item.has_checkbox:
        return list_item(inner, checked=item.is_checked)

    return list_item(inner)


def _table_cell_html(cell, ctx):
    cs = cell.colspan
    rs = cell.rowspan

    align = H_ALIGN.get(cell.align.getType()) if cell.align else None
    valign = V_ALIGN.get(cell.valign.getType()) if cell.valign else None

    fn = table_header_cell if cell.is_header else table_cell
    return fn(
        _rt(cell.text, ctx),
        colspan=cs if cs != 1 else None,
        rowspan=rs if rs != 1 else None,
        align=align,
        valign=valign,
    )


def _blocks(blocks, ctx):
    if not blocks:
        return ""

    return "".join(_block(b, ctx) for b in blocks)


def _block(b, ctx):
    t = b.getType()
    h = _BLOCK_HANDLERS.get(t)
    return h(b, ctx) if h else ""


def _bk_paragraph(b, ctx):
    return paragraph(_rt(b.text, ctx))


def _bk_heading(b, ctx):
    return heading(b.size or 1, _rt(b.text, ctx))


def _bk_anchor(b, _):
    return anchor(b.name or "")


def _bk_preformatted(b, ctx):
    lang = b.language or ""
    text = _rt(b.text, ctx)

    if lang:
        return tag("pre", tag("code", text, **{"class": f"language-{lang}"}))

    return tag("pre", text)


def _bk_footer(b, ctx):
    return footer(_rt(b.footer, ctx))


def _bk_divider(_, __):
    return horizontal_rule()


def _bk_list(b, ctx):
    items = b.items or []
    if any(it.has_checkbox for it in items):
        return tag("ul", *(_list_item(it, ctx) for it in items))

    first = items[0] if items else None
    first_type = first.type if first else ""
    if first_type:
        return ordered_list(
            *(_list_item(it, ctx) for it in items),
            start=first.value or 1,
            type=first_type,
        )

    return unordered_list(*(_list_item(it, ctx) for it in items))


def _bk_blockquote(b, ctx):
    inner = _blocks(b.blocks, ctx)
    credit = b.credit

    return blockquote(inner, cite=_rt(credit, ctx) if credit else None)


def _bk_expandable_blockquote(b, ctx):
    credit = b.credit

    return blockquote(
        _rt(b.text, ctx),
        cite=_rt(credit, ctx) if credit else None,
        expandable=True,
    )


def _bk_pullquote(b, ctx):
    credit = b.credit

    return aside(_rt(b.text, ctx), cite=_rt(credit, ctx) if credit else None)


def _bk_document(b, ctx):
    src = ctx.add("document", b.document)
    return _media_fig(tg_document(src), b.caption, ctx)


def _bk_photo(b, ctx):
    src = ctx.add("photo", b.photo, has_spoiler=b.has_spoiler)
    return _media_fig(image(src, spoiler=b.has_spoiler), b.caption, ctx)


def _bk_video(b, ctx):
    src = ctx.add("video", b.video, has_spoiler=b.has_spoiler)
    return _media_fig(video(src, spoiler=b.has_spoiler), b.caption, ctx)


def _bk_audio(b, ctx):
    src = ctx.add("audio", b.audio)
    return _media_fig(audio(src), b.caption, ctx)


def _bk_voice(b, ctx):
    src = ctx.add("audio", b.voice_note)
    return _media_fig(audio(src), b.caption, ctx)


def _bk_animation(b, ctx):
    src = ctx.add("animation", b.animation, has_spoiler=b.has_spoiler)
    return _media_fig(video(src, spoiler=b.has_spoiler), b.caption, ctx)


def _bk_map(b, ctx):
    loc = b.location

    return _media_fig(
        tg_map(loc.latitude or 0, loc.longitude or 0, b.zoom or 14), b.caption, ctx
    )


def _bk_collage(b, ctx):
    return tg_collage(
        _blocks(b.blocks, ctx), caption=_caption_html(b.caption, ctx) or None
    )


def _bk_slideshow(b, ctx):
    return tg_slideshow(
        _blocks(b.blocks, ctx), caption=_caption_html(b.caption, ctx) or None
    )


def _bk_table(b, ctx):
    cells = b.cells or []
    rows = [table_row(*(_table_cell_html(c, ctx) for c in row)) for row in cells]

    return table(
        *rows,
        bordered=b.is_bordered,
        striped=b.is_striped,
        compact=b.is_compact,
        caption=_caption_html(b.caption, ctx) or None,
    )


def _bk_details(b, ctx):
    return details(_blocks(b.blocks, ctx), summary=_rt(b.header, ctx), open=b.is_open)


def _bk_math(b, _):
    return tg_math_block(b.expression or "")


_BUTTON_STYLE = {
    ButtonStylePrimary.getType(): "primary",
    ButtonStyleDanger.getType(): "danger",
    ButtonStyleSuccess.getType(): "success",
    ButtonStyleLink.getType(): "link",
}


def _callback_data_str(data):
    if data is None:
        return None
    if isinstance(data, str):
        return data
    if isinstance(data, (bytes, bytearray)):
        try:
            return data.decode("utf-8")
        except UnicodeDecodeError:
            return data.decode("latin-1")
    return str(data)


def _bt_url(t):
    return "url", {"url": t.url or ""}


def _bt_user(t):
    return "url", {"url": f"tg://user?id={t.user_id or 0}"}


def _bt_callback(t):
    return "callback_data", {"data": _callback_data_str(t.data)}


def _bt_web_app(t):
    return "web_app", {"url": t.url or ""}


def _bt_login(t):
    extra = {"url": t.url or ""}
    if t.forward_text:
        extra["forward_text"] = t.forward_text
    return "login_url", extra


def _bt_switch(t):
    extra = {"query": t.query or ""}
    target = t.target_chat
    if target is None:
        return "switch_inline_query", extra

    tt = target.getType()
    if tt == TargetChatCurrent.getType():
        return "switch_inline_query_current_chat", extra
    if tt == TargetChatChosen.getType():
        types = target.types
        if types:
            extra["allow_user_chats"] = types.allow_user_chats
            extra["allow_bot_chats"] = types.allow_bot_chats
            extra["allow_group_chats"] = types.allow_group_chats
            extra["allow_channel_chats"] = types.allow_channel_chats
        return "switch_inline_query_chosen_chat", extra

    return "switch_inline_query", extra


def _bt_copy(t):
    return "copy_text", {"text": t.text or ""}


def _bt_disabled(_):
    return "disabled", {}


_BUTTON_TYPE_HANDLERS = {
    InlineKeyboardButtonTypeUrl.getType(): _bt_url,
    InlineKeyboardButtonTypeUser.getType(): _bt_user,
    InlineKeyboardButtonTypeCallback.getType(): _bt_callback,
    InlineKeyboardButtonTypeCallbackWithPassword.getType(): _bt_callback,
    InlineKeyboardButtonTypeWebApp.getType(): _bt_web_app,
    InlineKeyboardButtonTypeLoginUrl.getType(): _bt_login,
    InlineKeyboardButtonTypeSwitchInline.getType(): _bt_switch,
    InlineKeyboardButtonTypeCopyText.getType(): _bt_copy,
    InlineKeyboardButtonTypeDisabled.getType(): _bt_disabled,
}


def _inline_button_html(btn, ctx):
    if not btn:
        return ""

    kwargs = {}
    if btn.style:
        style = _BUTTON_STYLE.get(btn.style.getType())
        if style:
            kwargs["style"] = style

    if not btn.type:
        return ""

    h = _BUTTON_TYPE_HANDLERS.get(btn.type.getType())
    if not h:
        return ""

    html_type, extra = h(btn.type)
    kwargs.update(extra)

    return tg_button(_rt(btn.text, ctx), type=html_type, **kwargs)


def _bk_button_row(b, ctx):
    align = H_ALIGN.get(b.align.getType()) if b.align else None
    return tg_button_row(
        *(_inline_button_html(btn, ctx) for btn in (b.buttons or [])),
        align=align,
    )


_BLOCK_HANDLERS = {
    PageBlockParagraph.getType(): _bk_paragraph,
    PageBlockSectionHeading.getType(): _bk_heading,
    PageBlockAnchor.getType(): _bk_anchor,
    PageBlockPreformatted.getType(): _bk_preformatted,
    PageBlockFooter.getType(): _bk_footer,
    PageBlockDivider.getType(): _bk_divider,
    PageBlockList.getType(): _bk_list,
    PageBlockBlockQuote.getType(): _bk_blockquote,
    PageBlockExpandableBlockQuote.getType(): _bk_expandable_blockquote,
    PageBlockPullQuote.getType(): _bk_pullquote,
    PageBlockDocument.getType(): _bk_document,
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
    PageBlockButtonRow.getType(): _bk_button_row,
}


def rich_message_to_html(message: RichMessage):
    r"""Convert a TDLib rich message object to HTML

    Media uses ``tg://photo|video|audio|animation|document?id=<id>`` sources. Matching
    :class:`~pytdbot.types.InputRichMessageMedia` entries are returned for
    :meth:`~pytdbot.Client.sendRichMessage`

    Parameters:
        message (:class:`pytdbot.types.RichMessage`):
            The rich message object containing rich blocks

    Returns:
        (:py:class:`str`, list[:class:`~pytdbot.types.InputRichMessageMedia`]):
            HTML string and media list

            .. code-block:: python

                html, media = rich_message_to_html(message)
                await client.sendRichMessage(chat_id, html=html, media=media)
    """

    ctx = _MediaCollector()
    return _blocks(message.blocks, ctx), ctx.items
