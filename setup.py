# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in themes/__init__.py
from themes import __version__ as version

setup(
	name='themes',
	version=version,
	description='Theme application for erpnext ourway.me',
	author='Lium Kattan',
	author_email='liumkattan@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
