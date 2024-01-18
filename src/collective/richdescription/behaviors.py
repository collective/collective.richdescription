from . import _
from .utils import strip_html
from plone.app.dexterity import textindexer
from plone.app.textfield import RichText as RichTextField
from plone.app.textfield.value import RichTextValue
from plone.app.z3cform.widget import RichTextFieldWidget
from plone.autoform import directives
from plone.autoform.directives import widget
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope import schema
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


PATTERN_OPTIONS = {
    "tiny": {
        "theme": "silver",
        "height": 200,
        "menubar": "",
        "plugins": [],
        "toolbar": "bold italic | removeformat | unlink plonelink",
    },
}


class IRichDescriptionMarker(Interface):
    """Content Marker"""


@provider(IFormFieldProvider)
class IRichDescription(model.Schema):
    richdescription = RichTextField(
        title=_("label_description", default="Summary"),
        description=_(
            "help_description", default="Used in item listings and search results."
        ),
        required=False,
        missing_value="",
    )
    widget(
        "richdescription",
        RichTextFieldWidget,
        pattern_options=PATTERN_OPTIONS,
    )
    # Order after title from IDublinCore
    directives.order_after(richdescription="IDublinCore.title")
    directives.order_after(richdescription="IBasic.title")


@implementer(IRichDescription)
@adapter(IDexterityContent)
class RichDescriptionAdapter:
    def __init__(self, context):
        self.context = context

    @property
    def richdescription(self):
        ctx = self.context
        return getattr(ctx, "richdescription", getattr(ctx, "description", ""))

    @richdescription.setter
    def richdescription(self, value):
        if isinstance(value, RichTextValue):
            plain = value.raw
        else:
            plain = value
            value = RichTextValue(raw=value)
        self.context.richdescription = value
        self.context.description = strip_html(plain)


class ITitleAndRichDescriptionMarker(Interface):
    """Content Marker"""


@provider(IFormFieldProvider)
class ITitleAndRichDescription(model.Schema):
    title = schema.TextLine(title=_("label_title", default="Title"), required=True)
    richdescription = RichTextField(
        title=_("label_description", default="Summary"),
        description=_(
            "help_description", default="Used in item listings and search results."
        ),
        required=False,
        missing_value="",
    )
    widget(
        "richdescription",
        RichTextFieldWidget,
        pattern_options=PATTERN_OPTIONS,
    )

    textindexer.searchable("title")
    textindexer.searchable("richdescription")
    directives.order_before(title="*")
    directives.order_after(richdescription="ITitleAndRichDescription.title")


@implementer(ITitleAndRichDescription)
@adapter(IDexterityContent)
class TitleAndRichDescriptionAdapter(RichDescriptionAdapter):
    @property
    def title(self):
        return self.context.title

    @title.setter
    def title(self, value):
        self.context.title = value


class IOptionalTitleAndRichDescriptionMarker(Interface):
    """Content Marker"""


@provider(IFormFieldProvider)
class IOptionalTitleAndRichDescription(model.Schema):
    title = schema.TextLine(title=_("label_title", default="Title"), required=False)
    richdescription = RichTextField(
        title=_("label_description", default="Summary"),
        description=_(
            "help_description", default="Used in item listings and search results."
        ),
        required=False,
        missing_value="",
    )
    widget(
        "richdescription",
        RichTextFieldWidget,
        pattern_options=PATTERN_OPTIONS,
    )

    textindexer.searchable("title")
    textindexer.searchable("richdescription")
    directives.order_before(title="*")
    directives.order_after(richdescription="IOptionalTitleAndRichDescription.title")


@implementer(IOptionalTitleAndRichDescription)
@adapter(IDexterityContent)
class OptionalTitleAndRichDescriptionAdapter(TitleAndRichDescriptionAdapter):
    pass
