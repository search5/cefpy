from setuptools import Extension, setup

USE_CYTHON = True
ext = '.pyx' if USE_CYTHON else '.c'
extensions = [Extension("cefpython", ["cef/hello" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    ext_modules = extensions
)
