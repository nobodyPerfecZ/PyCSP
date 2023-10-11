from setuptools import setup, find_packages

# Load the requirements from requirements.txt
with open('requirements.txt') as f:
    req = f.read().splitlines()

setup(
    name="PyCSP",
    version="0.1",
    author=["Dennis J.", "Patrick B."],
    python_requires=">=3.10",
    packages=find_packages(
        exclude=[
            "tests",
            "tests.*",
        ]
    ),
    install_requires=req,
    include_package_data=True,
)
