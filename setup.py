from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="repo-spendy",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "gitpython>=3.1.40",
        "rich>=13.7.0",
        "click>=8.1.7",
        "plotext>=5.2.8",
        "python-dateutil>=2.8.2",
    ],
    entry_points={
        "console_scripts": [
            "repo-spendy=repo_spendy.cli:cli",
        ],
    },
    author="Kushal Sharma",
    author_email="kushalsharma0702@users.noreply.github.com",
    description="Automatically track your coding time from Git commits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kushalsharma0702/Repo-spendy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    python_requires=">=3.8",
)