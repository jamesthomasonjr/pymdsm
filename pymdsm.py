from markdown.extensions import Extension
from markdown.inlinepatterns import SimpleTagPattern

# Match '..abc..' but do not match '...abc...'
SMALL_TEXT_REGEX = r'(?<!\.)(\.{2})([^\.]*?)(\.{2})(?!\.)'

class Pymdsm(Extension):
    def extendMarkdown(self, md):
        small_tag = SimpleTagPattern(SMALL_TEXT_REGEX, 'small')
        md.inlinePatterns.register(small_tag, 'small', 175)
