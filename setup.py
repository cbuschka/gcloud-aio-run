import os
import subprocess
import re

import setuptools


def get_readme(version):
  with open("readme.md", "r", encoding='utf-8') as f:
    return re.sub(r"]\(\./",
                  f"](https://github.com/cbuschka/gcloud-aio-run/blob/{version}/",
                  f.read())


def get_version():
  proc = subprocess.Popen(['git', 'describe', '--exact-match', '--tags'],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
  stdout, stderr = proc.communicate()
  result = re.search('^v([^\n]+)\n$', stdout.decode("utf-8"), re.S)
  if not result:
    raise ValueError("Invalid version: '{}'.".format(result))
  return result.group(1)


version = get_version()
long_description = get_readme(version)
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(PACKAGE_ROOT, 'requirements.txt')) as f:
  REQUIREMENTS = [r.strip() for r in f.readlines()]

setuptools.setup(
    name='gcloud-aio-run',
    version=version,
    description='Python Client for Google Cloud Run',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=('tests',)),
    namespace_packages=[
      'gcloud',
      'gcloud.aio',
    ],
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
