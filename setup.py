from setuptools import setup, find_packages

setup(
    name="kitecmd-IR",
    version="0.2",
    author="coltonsr77",
    description="A KiteCMD extension that installs and verifies InstallerReady and kitecmd.",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "kitecmd>=0.8",        # ensures kitecmd is installed
    ],
    entry_points={
        "console_scripts": [
            "kitecmd-IR=kitecmd_IR.main:main",
        ],
    },
)
