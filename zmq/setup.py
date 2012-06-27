from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("cython_client",
              ["zmq-client.pyx"],
              libraries=["zmq"]) # Unix-like specific
]

setup(
  name = "cython_client",
  cmdclass = {"build_ext": build_ext},
  ext_modules = ext_modules
)
