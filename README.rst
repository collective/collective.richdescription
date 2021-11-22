Introduction
============

Adds the new html-formatable textfield ``richdescription`` content types can use.

There are two behaviors provided:

``collective.richdescription``
    The single `richdescription` field.

``collective.titleandrichdescription``
    A drop-in replacement for `plone.basic`.

- When the field is saved, the contents are also stored in the classic dublincore ``description`` field, but without html-formating.
- A metadata index is provided, so that ``richdescription`` can be read directly from catalog brains.

There is **no** ``folder_listing`` template yet.
If you want to have HTML formated descriptions in ``folder_listing`` use something like this

.. code-block: XML

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
The description field wasn't meant to hold HTML data.
People may tend to write long essays in the description field, which is not what you want, probably.
Some use cases require this functionality though, so have fun.


Migration?
==========

There should be no need for a specific migration step.
When no richdescription field is available for a content type, it falls back to the normal description field.
When saving a content type, the richdescription field is set and the catalog's metadata richdescription column is filled.


Compatibility
=============

Tested with Plone 6


Author
======

Johannes Raggam <johannes@raggam.co.at>
Peter Holzer <peter.holzer@agitator.com>
Jens Klein <jk@kleinundaprtner.at>


Source Code and Contributions
=============================

If you want to help with the development (reporting, improvement, update, bug-fixing, ...) of ``collective.richdescription`` this is a great idea!

Please file any issues or ideas for enhancement at the `issue tracker <https://github.com/collective/collective.richdescription`_.

The code is located in the `github collective <https://github.com/collective/collective.richdescription`_.

You can clone it or `get access to the github-collective <http://collective.github.com/>`_ and work directly on the project.

Maintainer is Johannes Raggam and the BlueDynamics Alliance developer team. We appreciate any contribution and if a release is needed to be done on pypi,
please just contact one of us `dev@bluedynamics dot com <mailto:dev@bluedynamics.com>`_

