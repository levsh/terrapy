from setuptools import setup, find_packages

from terrapy import __version__


setup(
    name='terrapy',
    version=__version__,
    author='Roma Koshel',
    author_email='roma.koshel@gmail.com',
    license='MIT',
    entry_points={
        'console_scripts': ['terrapy=terrapy.app:main'],
    },
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
    ],
)
