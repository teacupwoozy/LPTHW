try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Stacy Montemayor",
    "url": "URL to get it at.",
    "download_url": "Where to download it.",
    "author_email": "email",
    "license": "license information"
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["ex47"],
    "scripts": [],
    "Ex47": "projectname"
}

setup(**config)