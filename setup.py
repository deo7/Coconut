from setuptools import setup

setup(
   name='Coconut',
   version='1.0',
   description='Password system',
   author='Déodorant',
   author_email='deodev@protonmail.com',
   url='https://github.com/deo7/Coconut',
   packages=['Coconut'],
   install_requires=['pyfiglet', 'colorama', 'passpwnedcheck'], #external packages as dependencies
)