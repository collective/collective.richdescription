from .behaviors import IOptionalTitleAndRichDescriptionMarker
from .behaviors import IRichDescriptionMarker
from .behaviors import ITitleAndRichDescriptionMarker
from plone.indexer.decorator import indexer


def _base_indexer(obj):
    return obj.richdescription.output


@indexer(IRichDescriptionMarker)
def richdescription(obj):
    return _base_indexer(obj)


@indexer(ITitleAndRichDescriptionMarker)
def titleandrichdescription(obj):
    return _base_indexer(obj)


@indexer(IOptionalTitleAndRichDescriptionMarker)
def optionaltitleandrichdescription(obj):
    return _base_indexer(obj)
