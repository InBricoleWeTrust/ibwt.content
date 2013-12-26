from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='ibwt.content',
      version=version,
      description="ibwt content types",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone dexterity',
      author='jpcw',
      author_email='jp.camguilhem@gmail.com',
      url='https://github.com/InBricoleWeTrust/ibwt.content',
      license='bsd',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ibwt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok, relations]',
          'plone.app.relationfield',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
