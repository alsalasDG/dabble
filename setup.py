
from setuptools import setup
from setuptools.command.test import test as TestCommand

import sys

# Testing
class PyTest(TestCommand):

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run(self):
        import pytest
        errno = pytest.main()
        sys.exit(errno)

packages = ['Dabble', 'Dabble.param']
scripts = ['dabble', 'get_restraint_mask.py', 'convert_step5_to_dabble.py',
           'amber_rst2cms_v_noparams.py']
package_data = {
        'Dabble' : ['lipid_membranes/*.mae'],
        'Dabble.param' : ['charmm_parameters/*'],
        }

setup(name='dabble',
      version='2.7.7',
      description='Membrane protein system builder',
      author='Robin Betz',
      author_email='robin@robinbetz.com',
      url='http://robinbetz.com',
      license='GPLv2 or later',
      package_data=package_data,
      packages=packages,
      scripts=scripts,
      install_requires=["numpy",
                        "networkx>=1.11",
                        "pydot",
                        "vmd-python>=2.0.4",
                        "parmed"],
      tests_require=["pytest"],
      cmdclass = {'test': PyTest}
     )

