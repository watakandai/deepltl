from setuptools import setup, find_packages

setup(
    name='deepltl',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.19.5',
        'matplotlib',
        'tensorflow==2.2.0',
        'py-aiger',
        'py-aiger-sat',
        'protobuf==3.20.*'
    ],
    python_requires='>=3.7'
)
