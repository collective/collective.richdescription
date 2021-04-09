from collective.richdescription import strip_html
from collective.richdescription import _
from plone.app.dexterity.behaviors.metadata import IBasic
from plone.app.textfield import RichText as RichTextField
from plone.app.textfield.value import RichTextValue
from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import implementer
from zope.interface import provider


IBasic['description'].readonly = True  # Hide the description field


@provider(IFormFieldProvider)
class IRichDescription(model.Schema):

    richdescription = RichTextField(
        title=_('label_description', default='Summary'),
        description=_(
            'help_description',
            default='Used in item listings and search results.'
        ),
        required=False,
        missing_value='',
    )
    # Order after title from IDublinCore
    form.order_after(richdescription='IDublinCore.title')


@implementer(IRichDescription)
@adapter(IDexterityContent)
class RichDescription:

    def __init__(self, context):
        self.context = context

    @property
    def richdescription(self):
        ctx = self.context
        return getattr(
            ctx,
            'richdescription',
            getattr(ctx, 'description', '')
        )

    @richdescription.setter
    def richdescription(self, value):
        if not isinstance(RichTextValue, value):
            value = RichTextValue(raw=value)
        self.context.richdescription = value
        self.context.description = strip_html(value.raw)
