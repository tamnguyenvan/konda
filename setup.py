from setuptools import setup, find_packages

setup(
    name="konda",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'konda=konda.__main__:main',
        ],
    },
    author="Tam Nguyen",
    author_email="tamnvhustcc@gmail.com",
    description="A wrapper for conda commands with automatic Miniconda installation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tamnguyenvan/konda",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)