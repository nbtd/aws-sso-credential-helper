from setuptools import setup, find_packages

def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    name='aws_sso_credential_helper',
    author='nbtd',
    author_email="baconss11@gmail.com",
    version='0.0.1',
    packages=find_packages(),
    install_requires=requirements_from_file('requirements.txt'),
)