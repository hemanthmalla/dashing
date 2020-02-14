from setuptools import setup, find_packages

version = '0.2'

setup(name='py-dashing',
      version=version,
      description="High-level terminal-based dashboard - Forked from FedericoCeratto/dashing",
      long_description="""\
Easily create dashboards""",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
      ],
      keywords='dashboard terminal',
      author='Federico Ceratto',
      author_email='federico@debian.org',
      url='https://github.com/hemanthmalla/dashing',
      license='LGPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'blessed'
      ],
      )
