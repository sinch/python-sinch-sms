from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
  name = 'sinchsms',
  version = '1.0',
  description = 'A module to send sms using the Sinch REST apis, www.sinch.com',
  long_description = readme(),
  author = 'Slava Savitskiy',
  author_email = 'slava@sinch.com',
  url = 'https://github.com/sinch/python-sinch-sms.git',
  keywords = ['sms', 'sinch'],
  install_requires = ['requests'],
  classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apple Public Source License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications",
        "Development Status :: 4 - Beta"
  ],
)
