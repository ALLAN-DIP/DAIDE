import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DAIDE",
    version="0.0.1",
    author="Sander Schulhoff",
    author_email="sanderschulhoff@gmail.com",
    description="DAIDE parsing stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="NO",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)