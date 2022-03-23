Changelog
=========

3.0.0 (2022-03-23)
------------------

- Add ``collective.richdescription.title`` as a drop in replacement for ``plone.basic``.
  Also add ``collective.richdescription.optionaltitle`` as a variant for file/image.
  [jensens]

- Add patchable ``PATTERN_OPTIONS`` global to ``collective.richdescription.behavior`` in order to be able to set reduced options here (default).
  [jensens]

- Python 3 compatibility - remove Archetypes support.
  [agitator]


2.0 (2014-11-11)
----------------

- Cleaning up.
  [jensens]

- Add Dexterity support.
  [thet]

- Refactoring.
  [thet]

1.0.1 (2014-06-13)
------------------

- Metadata update.
  [thet]

1.0 (2012-11-07)
----------------

- Initial release
  [thet]

1.0pre
------

- When no description is set, return a BaseUnit as fallback. Fixes
  AttributeError, where original_encoding was tried to accessed on a string
  value.
  [thet]

- Register the skins folder for any theme.
  [thet]

- Initial version on 2010-10-05 for sfd.at.
