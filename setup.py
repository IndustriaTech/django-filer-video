# encoding=utf8
import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')

setup(
    name="django-filer-video",
    version="0.0.1",
    url='http://github.com/MagicSolutions/django-filer-video',
    description="Extending django-filer and add suppor for Video Files",
    long_description=README,

    author='Venelin Stoykov',
    author_email='venelin@magicbg.com',
    packages=[
        'filer_video',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'django>=1.3',
        'django-filer>=0.9',
    ],
)
