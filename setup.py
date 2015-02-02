from setuptools import find_packages, setup


author_email = __import__('couchdb').AUTHOR_EMAIL
author_name = __import__('couchdb').AUTHOR_NAME
description = __import__('couchdb').DESCRIPTION
lic = __import__('couchdb').LICENSE
version = __import__('couchdb').VERSION
URL = ''


setup(
    name='python3-couchdb',
    version=version,
    author=author_name,
    author_email=author_email,
    maintainer=author_name,
    maintainer_email=author_email,
    url=URL,
    description=description,
    long_description=description,
    download_url=URL,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: System :: Operating System Kernels :: Linux'],
    platforms=['linux2'],
    license=lic,
    packages=find_packages(),
)
