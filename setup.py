# -*- coding: utf-8 -*-
"""
Touch_Sensor_Proj
Processing data for kirigami touch sensor
"""
from setuptools import setup
import versioneer

DOCLINES = __doc__.split("\n")

setup(
    # Self-descriptive entries which should always be present
    name='touch_sensor_proj',
    author='minjcha',
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='MIT',

    # Which Python importable modules should be included when your package is installed
    packages=['touch_sensor_proj'],

    # Optional include package data to ship with your package
    # Comment out this line to prevent the files from being packaged with your software
    # Extend/modify the list to include/exclude other items as need be
    package_data={'touch_sensor_proj': ["data/*.dat"]
                  },

    entry_points={'console_scripts': ['data_proc = touch_sensor_proj.data_proc:main',
                                      ],
                  },     package_dir={'touch_sensor_proj': 'touch_sensor_proj'},

    test_suite='tests', install_requires=['rampy', 'numpy']
    # Additional entries you may want simply uncomment the lines you want and fill in the data
    # author_email='me@place.org',      # Author email
    # url='http://www.my_package.com',  # Website
    # install_requires=[],              # Required packages, pulls from pip if needed; do not use for Conda deployment
    # platforms=['Linux',
    #            'Mac OS-X',
    #            'Unix',
    #            'Windows'],            # Valid platforms your code works on, adjust to your flavor
    # python_requires=">=3.5",          # Python version restrictions

    # Manual control if final package is compressible or not, set False to prevent the .egg from being made
    # zip_safe=False,

)
