from pytdbot import types, utils


def test_tag_and_newline():
    assert utils.tag("p", "hi") == "<p>hi</p>"
    assert utils.tag("img", src="x") == '<img src="x"/>'
    assert utils.newline() == "<br>"
    assert utils.newline(2) == "<br><br>"


def test_inline_marks():
    assert utils.marked("x") == "<mark>x</mark>"
    assert utils.subscript("x") == "<sub>x</sub>"
    assert utils.superscript("x") == "<sup>x</sup>"
    assert utils.anchor("n") == '<a name="n"></a>'
    assert utils.email_link("a@b.c", "mail") == '<a href="mailto:a@b.c">mail</a>'
    assert utils.phone("+1", "call") == '<a href="tel:+1">call</a>'
    assert utils.in_doc_link("n", "go") == '<a href="#n">go</a>'
    assert utils.thinking("hmm") == "<tg-thinking>hmm</tg-thinking>"
    assert utils.tg_reference("r", "t") == '<tg-reference name="r">t</tg-reference>'
    assert utils.tg_time(1, "D", "d") == '<tg-time unix="1" format="D">d</tg-time>'
    assert utils.tg_math("x^2") == "<tg-math>x^2</tg-math>"
    assert utils.tg_math_block("x^2") == "<tg-math-block>x^2</tg-math-block>"


def test_blocks():
    assert utils.heading(1, "T") == "<h1>T</h1>"
    assert utils.heading(1, "T", name="n") == '<a name="n"></a><h1>T</h1>'
    assert utils.paragraph("a", "b") == "<p>ab</p>"
    assert utils.footer("f") == "<footer>f</footer>"
    assert utils.horizontal_rule() == "<hr/>"


def test_lists():
    assert utils.list_item("x") == "<li>x</li>"
    assert utils.list_item("x", value=2) == '<li value="2">x</li>'
    assert '<input type="checkbox" checked/>' in utils.list_item("x", checked=True)
    assert utils.unordered_list("a", "b") == "<ul><li>a</li><li>b</li></ul>"
    assert (
        utils.ordered_list("a", start=3, reversed=True)
        == '<ol start="3" reversed><li>a</li></ol>'
    )


def test_quotes_and_media():
    assert utils.blockquote("q", cite="c") == "<blockquote>q<cite>c</cite></blockquote>"
    assert "expandable" in utils.blockquote("q", expandable=True)
    assert utils.aside("q") == "<aside>q</aside>"
    assert utils.image("u", alt="a") == '<img src="u" alt="a"/>'
    assert "tg-spoiler" in utils.image("u", spoiler=True)
    assert utils.video("u") == '<video src="u"></video>'
    assert utils.audio("u") == '<audio src="u"></audio>'
    assert utils.figure("x") == "<figure>x</figure>"
    assert utils.figcaption("c") == "<figcaption>c</figcaption>"
    assert utils.tg_map(1.0, 2.0, 3) == '<tg-map lat="1.0" long="2.0" zoom="3"/>'
    assert utils.tg_document("u") == '<tg-document src="u"></tg-document>'


def test_collage_slideshow_table_details():
    img = utils.image("u")
    assert utils.tg_collage(img, caption="c").startswith("<tg-collage>")
    assert utils.tg_slideshow(img, caption="c").startswith("<tg-slideshow>")
    cell = utils.table_cell("d")
    header = utils.table_header_cell("h")
    assert cell == "<td>d</td>"
    assert header == "<th>h</th>"
    row = utils.table_row(cell)
    assert row == "<tr><td>d</td></tr>"
    assert utils.table_header("H") == "<tr><th>H</th></tr>"
    tbl = utils.table(row, bordered=True, caption="cap")
    assert tbl.startswith("<table bordered>")
    assert "<caption>cap</caption>" in tbl
    assert (
        utils.details("body", summary="s")
        == "<details><summary>s</summary>body</details>"
    )
    assert "open" in utils.details("body", summary="s", open=True)


def test_tg_button_types():
    assert 'type="url"' in utils.tg_button("Go", type="url", url="https://t.me")
    assert 'type="callback_data"' in utils.tg_button(
        "Go", type="callback_data", data="ok"
    )
    raw = utils.callback_data("ok")
    assert "data=" in utils.tg_button("Go", type="callback_data", data=raw)
    assert 'type="web_app"' in utils.tg_button("Go", type="web_app", url="https://t.me")
    login = utils.tg_button(
        "Go",
        type="login_url",
        url="https://t.me",
        forward_text="fwd",
        request_write_access=True,
    )
    assert 'type="login_url"' in login
    assert "request-write-access" in login
    assert 'type="switch_inline_query"' in utils.tg_button(
        "Go", type="switch_inline_query", query="q"
    )
    assert 'type="switch_inline_query_current_chat"' in utils.tg_button(
        "Go", type="switch_inline_query_current_chat", query="q"
    )
    chosen = utils.tg_button(
        "Go",
        type="switch_inline_query_chosen_chat",
        query="q",
        allow_user_chats=True,
        allow_bot_chats=True,
        allow_group_chats=True,
        allow_channel_chats=True,
    )
    assert "allow-user-chats" in chosen
    assert 'type="copy_text"' in utils.tg_button("Go", type="copy_text", text="hi")
    assert 'type="disabled"' in utils.tg_button("Go", type="disabled")
    row = utils.tg_button_row(
        utils.tg_button("A", type="url", url="https://t.me"), align="left"
    )
    assert row.startswith('<tg-button-row align="left">')


def test_rich_message_to_html():
    message = types.RichMessage(
        blocks=[
            types.PageBlockParagraph(text=types.RichTextPlain(text="hello")),
            types.PageBlockDivider(),
        ]
    )
    html, media = utils.rich_message_to_html(message)
    assert "<p>hello</p>" in html
    assert "<hr/>" in html
    assert media == []
