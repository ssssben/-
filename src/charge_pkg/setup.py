from setuptools import setup, find_packages

package_name = 'charge_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bun',
    maintainer_email='vlongbf@gmail.com',
    description='パソコンの充電残量を知らせる',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'battery_talker = charge_pkg.battery_talker:main',
        ],
    },
    package_data={
        '': ['package.xml'],
    },
    include_package_data=True,
)

