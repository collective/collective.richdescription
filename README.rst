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


Source Code and Contributions
=============================

If you want to help with the development (reporting, improvement, update, bug-fixing, ...) of ``collective.richdescription`` this is a great idea!

Please file any issues or ideas for enhancement at the `issue tracker <https://github.com/collective/collective.richdescription`_.

The code is located in the `github collective <https://github.com/collective/collective.richdescription`_.

You can clone it or `get access to the github-collective <http://collective.github.com/>`_ and work directly on the project.

Maintainer is Johannes Raggam and the BlueDynamics Alliance developer team. We appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us `dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

