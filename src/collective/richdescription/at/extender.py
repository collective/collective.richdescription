# -*- coding: utf-8 -*-
from Products.Archetypes import PloneMessageFactory as _
from Products.Archetypes.interfaces import IExtensibleMetadata
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from collective.richdescription import strip_html
from zope.component import adapter
from zope.interface import implementer

try:
    from Products.LinguaPlone import public as atapi
except ImportError:
    # No multilingual support
    from Products.Archetypes import atapi


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


@implementer(IOrderableSchemaExtender)
@adapter(IExtensibleMetadata)
class RichDescriptionExtender(object):

    fields = [
        RichDescriptionField(
            'richdescription',
            required=False,
            searchable=True,
            default_content_type='text/html',
            allowable_content_types=('text/html',),
            widget=atapi.RichWidget(
                allow_file_upload=False,
                label=_(u'label_description', default=u'Description'),
                description=_(
                    u'help_description',
                    default=u'Used in item listings and search results.'
                ),
            ),
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, order):
        schemata_default = order['default']
        schemata_default.remove('richdescription')
        idx = schemata_default.index('description')
        schemata_default.insert(idx + 1, 'richdescription')
        return order


@implementer(ISchemaModifier)
@adapter(IExtensibleMetadata)
class RichDescriptionModifier(object):

    def __init__(self, context):
        self.context = context

    def fiddle(self, schema):
        schema['description'].widget.visible = {'view': 'hidden',
                                                'edit': 'hidden'}
