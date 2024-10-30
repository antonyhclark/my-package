from setuptools import setup

setup(name='my_package', # name of top level folder containing __init__.py
      version='0.0.1',
      description='Perform and visualize a text analysis.',
      author='ahc',
      # as name plus sub folders containing __init__.py files i.e. sub-packages
      packages=['my_package', 'sub_package'])
