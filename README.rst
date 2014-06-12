Introduction
============

Adds the new html-formatable textfield "richdescription" to Archetypes based
content types and hides the description field from ExtensibleMetadata. When the
field is saved, the contents are also stored in the "description" field, but
without html-formating. A Metadata index is provided, so that "richdescription"
can be used with catalog brains.
There is no folder_listing template yet, but if you want to have HTML formated
descriptions in folder_listing, then use something like this::

    <tal:block
      tal:define="item_description item/richdescription|nothing;
                  item_description python:item_description or item.Description;">
      <p class="akaDescription"
        tal:condition="item_description"
        tal:content="structure item_description">DESCRIPTION</p>
    </tal:block>


Warning
=======

Although there are no big issues with this package, use it at your own risk!
The description field wasn't meant to hold HTML data. People may tend to write
long essays in the description field, which is not what you want, probably.
Some use cases require this functionality though, so have fun.


Migration?
==========

There should be no need for a specific migration step. When no richdescription
field is available for a content type, it falls back to the normal description
field. When saving a content type, the richdescription field is set and the
catalog's metadata richdescription column is filled.


Compatibility
=============

Tested with Plone 4


Author
======

Johannes Raggam <johannes@raggam.co.at>
