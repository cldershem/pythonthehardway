try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Cameron Dershem',
	'url': 'http://github.com/cldershem/'
	'download_url': 'http://github.com/cldershem/'
	'author_email': 'cldershem+project@gmail.com'
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': []
	'name': 'projectname'
	}

setup(**config)
