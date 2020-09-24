import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
   name='StateGame-jean3108',
   version='1.0',
   author='Jean Soler',
   author_email='jean.soler3108@gmail.com',
   description='Basic architecture for two-player game',
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/jean3108/TwoPlayer-Game",
   packages=setuptools.find_packages(),
   install_requires=['abc'], 
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)