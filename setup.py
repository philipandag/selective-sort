# setup.py
from setuptools import setup, find_packages

setup(
           # the name must match the folder name 'verysimplemodule'
        name="selective-sort", 
        version="0.1.0",
        author="todo",
        author_email="todo",
        description="Selectively sorts given file in marked sections only",
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python'],
        classifiers= [

        ]
)
