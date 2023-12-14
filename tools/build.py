import os
import shutil
from typing import Dict, Any

from setuptools.command.build_ext import build_ext
from setuptools import Distribution, Extension
from Cython.Build import cythonize

from cmake_extension import CMakeExtension, ExtensionBuilder

compile_args = ["-march=native", "-O3"]
link_args = []
include_dirs = []
libraries = ["hello"]


def get_numpy_include():
    import builtins

    builtins.__NUMPY_SETUP__ = False
    try:
        import numpy as np
    except ImportError:
        raise SystemExit("CEFSpark requires NumPy for setup")
    return np.get_include()


def build() -> None:
    extensions = [
        Extension(
            "hello2",
            ["native/*.pyx"],
            extra_compile_args=compile_args,
            extra_link_args=link_args,
            include_dirs=[get_numpy_include(), "."],
            libraries=libraries,
        )
    ]
    # cython_modules = cythonize(
    #     extensions,
    #     include_path=include_dirs,
    #     compiler_directives={"binding": True, "language_level": 3},
    # )

    cmake_modules = [
        CMakeExtension("build", sourcedir="native")]
    # ext_modules = cython_modules + cmake_modules
    # ext_modules = cmake_modules + cython_modules
    # ext_modules = cmake_modules
    # setup_kwargs.update(
    #     {
    #         "ext_modules": ext_modules,
    #         "cmdclass": dict(build_ext=ExtensionBuilder),
    #         "zip_safe": False,
    #     }
    # )

    distribution = Distribution({"name": "extended", "ext_modules": cmake_modules})
    # distribution.package_dir = {"extended": "extended"}

    cmd = ExtensionBuilder(distribution)
    cmd.ensure_finalized()
    cmd.run()

    print('-' * 80)
    print(cmd.get_outputs())
    print('-' * 80)
    #
    # # Copy built extensions back to the project
    # for output in cmd.get_outputs():
    #     relative_extension = os.path.relpath(output, cmd.build_lib)
    #     shutil.copyfile(output, relative_extension)
    #     mode = os.stat(relative_extension).st_mode
    #     mode |= (mode & 0o444) >> 2
    #     os.chmod(relative_extension, mode)


if __name__ == "__main__":
    build()
