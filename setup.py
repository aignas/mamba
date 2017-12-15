# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from mamba import __version__

setup(name='mamba',
      version=__version__,
      description="The definitive testing tool for Python. Born under the banner of Behavior Driven Development.",
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Programming Language :: Python',
          'Programming Language :: Python::2.7',
          'Programming Language :: Python::3.6',
          'Programming Language :: Python :: Implementation',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'
      ],
      keywords='',
      author=u'Néstor Salceda',
      author_email='nestor.salceda@gmail.com',
      url='http://nestorsalceda.github.io/mamba',
      license='MIT/X11',
      packages=find_packages(exclude=['ez_setup', 'examples', 'spec', 'spec.*']),
      include_package_data=True,
      zip_safe=False,
      install_requires=['clint', 'coverage'],
      test_require=['expect', 'doublex', 'doublex-expects', 'mock'],
      entry_points={
          'console_scripts': [
              'mamba = mamba.cli:main'
          ]
      })
