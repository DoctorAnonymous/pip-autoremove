from setuptools import setup, find_packages


setup(name='pip-autoremove',
      version='1.0.0',
      description='Remove a package and its unused dependencies.',
      url='https://github.com/DoctorAnonymous/pip-autoremove.git',
      author='zcmscy',
      author_email='zcmscy@icloud.com',
      license='Apache',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'pip-autoremove = pip_autoremove:main',
          ],
      }
      )
