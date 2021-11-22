import re


def strip_html(html):
    """Strips out html characters and leading or trailing whitespace.

    Usage:

    >>> html = '''<a href="some"
    ... title="where"> else < or<br /> </a><!-- nothing -->'''
    >>> strip_html(html)
    'else < or'

    Won't work for:

    >>> html = '''<a href="some"
    ... title="where"> else < or > that<br /> </a><!-- nothing -->'''
    >>> strip_html(html)
    'else  that'

    """
    # regex pattern from:
    # http://love-python.blogspot.com/2008/07/strip-html-tags-using-python.html
    re_html = re.compile("<[^<]*?/?>")
    text = re_html.sub("", html)
    return text.strip()
