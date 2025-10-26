from setuptools import setup, find_packages

setup(
    name="kitecmd-IR",
    version="0.1",
    author="coltonsr77",
    description="KiteCMD tool that checks, installs, and verifies InstallerReady.",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "kitecmd-IR=kitecmd_IR.main:main",
        ],
    },
    python_requires=">=3.8",
)
