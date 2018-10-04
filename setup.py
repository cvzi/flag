import setuptools
import os
import io

with io.open("README.md", encoding="utf-8") as f:
    long_description = f.read().strip()

version = None
with io.open(os.path.join("flag", "__init__.py"), encoding="utf-8") as f:
    for line in f:
        if line.strip().startswith("__version__"):
            version = line.split("=")[1].strip().replace('"', "").replace("'", "")
            break

setuptools.setup(
    name="emoji-country-flag",
    version=version,
    author="cuzi",
    author_email="cuzi@openmail.cc",
    description="En/Decode unicode country flags emoji",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cvzi/flag",
    packages=["flag"],
    zip_safe=True,
    test_suite="nose.collector",
    tests_require=["emoji", "nose"],
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Communications :: Chat",
        "Topic :: Printing",
        "Topic :: Text Processing :: General"
    ),
)