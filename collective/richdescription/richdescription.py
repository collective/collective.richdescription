# -*- coding: utf-8 -*-
#
# GNU General Public License (GPL)
#
__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from zope.component import adapts
from zope.interface import implements

try:
    from Products.LinguaPlone import public  as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi

from Products.Archetypes import PloneMessageFactory as _
from Products.Archetypes.ExtensibleMetadata import ExtensibleMetadata
from Products.Archetypes.interfaces import IExtensibleMetadata
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.field import ExtensionField

import re
def strip_html(html):
    """ Strips out html characters and leading or trailing whitespace.

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
    text = re_html.sub('', html)
    return text.strip()


class RichDescriptionField(ExtensionField, atapi.TextField):

    def getRaw(self, instance, raw=False, **kwargs):
        value = super(RichDescriptionField,
                      self).getRaw(instance, raw=raw, **kwargs)
        if not value:
            # Try to get Value from Description if it wasn't set until yet
            value = instance.Description()
            # Set it to the RichDescriptionField ...
            super(RichDescriptionField, self).set(instance, value, **kwargs)
            # ... and get it back to be able to return a BaseUnit object
            value = super(RichDescriptionField,
                          self).getRaw(instance, raw=raw, **kwargs)
        return value

    def set(self, instance, value, **kwargs):
        try:
            # Set Description only if richdescription attribute exists ...
            ## instance.richdescription
            value_orig = instance.Description()
            value_prev = instance.richdescription.getRaw()
            if not value and not value_prev and value_orig:
                # richdescription never set, but description -> prefill
                value = value_orig
            cleaned = strip_html(value)
            instance.setDescription(cleaned)
        except AttributeError:
            # ... but prefill richdescription if it didn't exist until now.
            value = instance.Description()
        return super(RichDescriptionField,
                     self).set(instance, value, **kwargs)


class RichDescriptionExtender(object):
    implements(IOrderableSchemaExtender)
    adapts(IExtensibleMetadata)

    fields = [
        RichDescriptionField('richdescription',
            required=False,
            searchable=True,
            default_content_type = 'text/html',
            allowable_content_types = ('text/html',),
            widget=atapi.RichWidget(
                allow_file_upload = False,
                label=_(u'label_description', default=u'Description'),
                description=_(u'help_description',
                              default=u'Used in item listings and search results.'),
                ),
            ),
    ]

    def __init__(self, context): self.context = context
    def getFields(self): return self.fields

    def getOrder(self, order):
        schemata_default = order['default']
        schemata_default.remove('richdescription')
        idx = schemata_default.index('description')
        schemata_default.insert(idx+1, 'richdescription')
        return order


class RichDescriptionModifier(object):
    implements(ISchemaModifier)
    adapts(IExtensibleMetadata)

    def __init__(self, context): self.context = context

    def fiddle(self, schema):
        schema['description'].widget.visible = {'view': 'hidden',
                                                'edit': 'hidden'}
