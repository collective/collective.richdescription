from Products.CMFPlone.utils import safe_unicode
from plone.app.textfield.value import RichTextValue
from plone.app.contenttypes.migration.utils import ATCT_LIST
from plone.app.contenttypes.migration import migration


def richdescription_migrator(old, new):
    field = old.getField('richdescription')
    mime_type = field.getContentType(old)
    raw_text = safe_unicode(field.getRaw(old))
    if raw_text.strip() == '':
        return
    richtext = RichTextValue(raw=raw_text, mimeType=mime_type,
                             outputMimeType='text/x-html-safe')
    new.richdescription = richtext


def patch_ATCT_LIST():
    for key, value in ATCT_LIST.items():
        # Add 'richdescription' to all extended_fields fields
        ext = value.get('extended_fields', [])
        if 'richdescription' not in ext:
            # ... because patch_ATCT_LIST might be called more than once
            ext.append('richdescription')
patch_ATCT_LIST()


orig_ATCTBaseMigrator = migration.ATCTBaseMigrator
class ATCTBaseMigrator(orig_ATCTBaseMigrator):
    """Patch ATCTBaseMigrator to do the richdescription.
    Please note: works until a derived class overwrited the custom method.
    """
    def custom(self):
        richdescription_migrator(self.old, self.new)
migration.ATCTBaseMigrator = ATCTBaseMigrator
