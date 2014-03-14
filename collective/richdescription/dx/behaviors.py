from collective.richdescription import strip_html
from plone.app.dexterity import PloneMessageFactory as _PMF
from plone.app.textfield import RichText as RichTextField
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapts
from zope.interface import alsoProvides, implements


class IRichDescription(model.Schema):

    richdescription = RichTextField(
        title=_PMF(u'label_description', default=u'Summary'),
        description=_PMF(
            u'help_description',
            default=u'Used in item listings and search results.'
        ),
        required=False,
        missing_value=u'',
    )
alsoProvides(IRichDescription, IFormFieldProvider)


class RichDescription(object):
    implements(IRichDescription)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context

    @property
    def richdescription(self):
        ctx = self.context
        return getattr(
            ctx,
            'richdescription',
            getattr(ctx, 'description', u'')
        )

    @richdescription.setter
    def richdescription(self, value):
        self.context.richdescription = value
        self.context.description = strip_html(value)
