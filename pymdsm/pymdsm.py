from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern

SMALL_TEXT_REGEX = r'(?<!\.)(\.{2})([^\.]*?)(\.{2})(?!\.)'

class PymdsmExtension(Extension):
    """Adds Small extension to Markdown class."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        super(PymdsmExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md):
        """Insert <small>test</small> tags as ..test.."""

        small_tag = SimpleTagPattern(SMALL_TEXT_REGEX, 'small')
        md.inlinePatterns.register(small_tag, 'small', 175)

def makeExtension(*args, **kwargs):
    """Return extension."""

    return PymdsmExtension(*args, **kwargs)

