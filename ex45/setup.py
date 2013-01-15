try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex45',
	'author': 'Cameron Dershem',
	'url': 'http://github.com/cldershem/'
	'download_url': 'http://github.com/cldershem/'
	'author_email': 'cldershem+project@gmail.com'
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex45'],
	'scripts': []
	'name': 'ex45'
	}

setup(**config)
