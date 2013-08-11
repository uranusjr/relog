from docutils.core import publish_parts


def render_to_html(raw_content, options=None):
    """
    Render given raw reStructuredText content to HTML format (body content
    only). The content will be rendered by docutils.core.publish_parts using
    the HTML writer.

    An optional parameter options can be given to override the default behavior
    of the writer. If a dict is given, it will be passed directly to
    publish_parts as the settings_overrides parameter. If omitted or given
    None, the default behavior is to set the initial header level to h2.
    """
    options = options or {}
    # Add a line before the content to supress the document title. The added
    # content (<p>a</p>, 8 characters) is then removed after redering.
    rendered = publish_parts(
        source='a\n\n' + raw_content,
        writer_name='html', settings_overrides=options
    )
    return rendered['body'][8:]
