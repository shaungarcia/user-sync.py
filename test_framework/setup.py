# Copyright (c) 2016-2017 Adobe Systems Incorporated.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup

version_namespace = {}
with open('user_sync_test/version.py') as f:
    exec(f.read(), version_namespace)

setup(name='user-sync-test',
      version=version_namespace['__version__'],
      description='Application for synchronizing customer directories with the Adobe Enterprise Admin Console',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: MIT License',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
      ],
      url='https://github.com/adobe-apiplatform/test_framework/user-sync-test.py',
      maintainer='Daniel Brotsky',
      maintainer_email='dbrotsky@adobe.com',
      license='MIT',
      packages=['user_sync_test'],
      install_requires=[
          'PyYAML',
      ],
      setup_requires=[],
      tests_require=[
      ],
      entry_points={
          'console_scripts': [
              'user_sync_test = user_sync_test.app:main'
          ]
      },
      zip_safe=False)
