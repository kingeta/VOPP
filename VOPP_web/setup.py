from setuptools import setup

setup(
    name = 'VOPP_web',
    packages = ['VOPP_web'],
    include_package_data = True,
    install_requires=[
        'flask',
    ],
)