#!/usr/bin/env python

"""latexpkges: LaTeX package cleanup utility

Find packages included in your LaTeX document but not actually used.
"""

__version__ = "0.1.0a1"

from distutils.core import setup
try:
    import py2exe
except ImportError:
    pass

doclines = __doc__.splitlines()
name, short_description = doclines[0].split(": ")
long_description = "\n".join(doclines[2:])

if __name__ == "__main__":
    setup(name=name,
          version=__version__,
          description=short_description,
          long_description=long_description,
          python_requires='>=2, <3',
          options={'py2exe': {'bundle_files': 1, 'compressed': True}},
          console=['LaTeXpkges.py'],
          scripts=['LaTeXpkges.py'])
