from setuptools import setup, find_packages
from setuptools.command.install import install

from compile import compile

requires = [
    'protobuf==3.0.0b3',
]


class BuildProto(install):

    def run(self):
        compile('python', 'pokemongoproto')
        install.run(self)


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
    cmdclass={'install': BuildProto}
)
