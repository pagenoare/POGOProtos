from setuptools import setup, find_packages

requires = [
    'protobuf==3.0.0b3',
]

setup(
    name='pokemongoproto',
    version='0.1',
    description='pokemongoproto',
    classifiers=[],
    author='',
    author_email='',
    url='',
    keywords='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)