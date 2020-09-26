import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
   name='twoPlayerAiGame',
   version='1.0',
   author='Jean Soler',
   author_email='jean.soler3108@gmail.com',
   description='Basic architecture for two-player game and AI algorithms',
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/jean3108/TwoPlayer-Game",
   packages=setuptools.find_packages(),
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'abc'
    ]
)