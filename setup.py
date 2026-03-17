from setuptools import setup, find_packages

setup(
    name="mlops_db_utils",
    version="0.1.0",
    description="MLOps utility for MongoDB connection and data handling",
    author="Sunila",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pymongo", "pandas"],
    python_requires=">=3.9",
)