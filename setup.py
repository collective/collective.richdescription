from setuptools import find_packages
from setuptools import setup


version = "3.0.0"

long_description = "{}\n{}".format(
    open("README.rst").read(), open("CHANGES.rst").read()
)

setup(
    name="collective.richdescription",
    version=version,
    description="Turns the Plone 'Description' field into Richtext/HTML",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="plone richtext dublincore",
    author="Johannes Raggam",
    author_email="raggam-nl@adm.at",
    url="https://github.com/collective/collective.richdescription",
    license="GPLv2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["collective"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "zope.component",
        "zope.interface",
        "plone.app.dexterity",
        "plone.app.textfield",
        "plone.behavior",
        "plone.autoform",
        "plone.dexterity",
        "plone.supermodel",
    ],
    extras_require={},
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
