import os
import re

import setuptools

VERSION = '1.0.0.alpha1'

PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(PACKAGE_ROOT, 'readme.md')) as f:
  README = re.sub(r"]\(\./",
                  f"](https://github.com/cbuschka/gcloud-aio-run/blob/v{VERSION}/",
                  f.read())

with open(os.path.join(PACKAGE_ROOT, 'requirements.txt')) as f:
  REQUIREMENTS = [r.strip() for r in f.readlines()]

setuptools.setup(
    name='gcloud-aio-run',
    version=VERSION,
    description='Python Client for Google Cloud Run',
    long_description=README,
    long_description_content_type="text/markdown",
    namespace_packages=[
      'gcloud',
      'gcloud.aio',
    ],
    packages=setuptools.find_packages(exclude=('tests',)),
    python_requires='>= 3.6',
    install_requires=REQUIREMENTS,
    author='Cornelius Buschka',
    author_email='cbuschka@gmail.com',
    url='https://github.com/cbuschka/gcloud-aio-run',
    platforms='Posix; MacOS X; Windows',
    include_package_data=True,
    zip_safe=False,
    license='MIT License',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Topic :: Internet',
    ],
)
