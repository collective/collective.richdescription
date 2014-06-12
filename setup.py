from setuptools import setup, find_packages

version = '1.0.1'

setup(name='collective.richdescription',
      version=version,
      description="Richtext/HTML Description field for Archetypes",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'zope.component',
          'zope.interface',
          'archetypes.schemaextender',
          'Products.Archetypes',
      ],
      extras_require={'test': ['interlude',]},
      )
