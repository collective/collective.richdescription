from setuptools import setup, find_packages

version = '2.0dev'

long_description = "%s\n%s" % (
    open("README.rst").read(),
    open("CHANGES.rst").read()
)

setup(
    name='collective.richdescription',
    version=version,
    description="Turns Plone 'Description' field into Richtext/HTML",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='plone richtext',
    author='Johannes Raggam',
    author_email='raggam-nl@adm.at',
    url='https://pypi.python.org/pypi/collective.richdescription',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.interface',
    ],
    extras_require={
        'archetypes': [
            'archetypes.schemaextender',
            'Products.Archetypes',
        ],
        'dexterity': [
            'plone.app.dexterity',
            'plone.app.textfield',
            'plone.behavior',
            'plone.autoform',
            'plone.dexterity',
            'plone.supermodel',
        ],
    },
)
