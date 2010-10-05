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

from html2text import html2text

class RichDescriptionField(ExtensionField, atapi.TextField):

    def getRaw(self, instance, raw=False, **kwargs):
        value = super(RichDescriptionField,
                      self).getRaw(instance, raw=raw, **kwargs)
        if not value:
            # Try to get Value from Description if it wasn't set until yet
            value = instance.Description()
        return value

    def set(self, instance, value, **kwargs):
        instance.setDescription(html2text(value).strip())
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