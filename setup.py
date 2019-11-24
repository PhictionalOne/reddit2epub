from setuptools import setup

setup(
    name='reddit2epub',
    version='0.1.0',
    description='A CLI to convert reddit series into epub files',
    url='https://github.com/mircohaug/reddit2epub.git',
    author='Mirco Haug',
    author_email='python@mircohaug.de',
    packages=[],
    scripts=['reddit2epub.py'],
    install_requires=[
        'click==7.*',
        'praw==6.*',
        'EbookLib==0.17.*',
    ],
    entry_points={
        "console_scripts": ['reddit2epub = reddit2epub:main']
    },
    # from https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop"
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Utilities"
    ],
)