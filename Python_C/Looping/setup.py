from distutils.core import setup, Extension
setup(name='loop', version='1.0',ext_modules=[Extension('loop', ['loop.c'])])