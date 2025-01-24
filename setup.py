from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='esolangGenerator',
    version='0.1.0',
    description='Small package to design simplistic esolangs',
    long_description=readme,
    author='Yash Tiwari',
    author_email='yashvtiwari04@gmail.com',
    url='https://github.com/Yash-V-Tiwari/EsolangGenerator',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)