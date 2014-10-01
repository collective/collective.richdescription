# -*- coding: utf-8 -*-
from Products.CMFPlone.utils import safe_unicode
from collective.richdescription.dx.behaviors import IRichDescription
from plone.app.contenttypes.migration.migration import ICustomMigrator
from plone.app.contenttypes.migration.utils import ATCT_LIST
from plone.app.textfield.value import RichTextValue
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
import logging

logger = logging.getLogger(__name__)


@implementer(ICustomMigrator)
@adapter(Interface)
class RichDescriptionMigrator(object):

    def __init__(self, context):
        self.context = context

    def migrate(self, old, new):
        behavior = IRichDescription(new, None)
        if not behavior:
            return
        field = old.getField('richdescription')
        mime_type = field.getContentType(old)
        raw_text = safe_unicode(field.getRaw(old))
        if raw_text.strip() == '':
            return
        richtext = RichTextValue(raw=raw_text, mimeType=mime_type,
                                 outputMimeType='text/x-html-safe')
        behavior.richdescription = richtext

        logger.info(
            "Migrating richdescription value: %s" % (  # noqa
                len(raw_text) > 10 and '%s...' %  # noqa
                raw_text[:10] or raw_text
            )
        )


def patch_ATCT_LIST():
    for key, value in ATCT_LIST.items():
        # Add 'richdescription' to all extended_fields fields
        ext = value.get('extended_fields', [])
        if 'richdescription' not in ext:
            # ... because patch_ATCT_LIST might be called more than once
            ext.append('richdescription')
patch_ATCT_LIST()
