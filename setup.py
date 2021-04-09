from setuptools import setup, find_packages

version = '3.0'

long_description = "{}\n{}".format(
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
    keywords='plone richtext dublincore',
    author='Johannes Raggam',
    author_email='raggam-nl@adm.at',
    url='https://pypi.python.org/pypi/collective.richdescription',
    license='GPLv2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.component',
        'zope.interface',
        'plone.app.dexterity',
        'plone.app.textfield',
        'plone.behavior',
        'plone.autoform',
        'plone.dexterity',
        'plone.supermodel',
    ],
    extras_require={
    },
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
