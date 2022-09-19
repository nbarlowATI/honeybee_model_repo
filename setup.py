#!/usr/bin/env python
from setuptools import find_packages, setup

requirements = []
with open("requirements.txt") as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

setup(
    name="honeybee_model_repo",
    version="0.0.1",
    description="scivision plugin, using EfficientNetB3 model",
    url="https://github.com/nbarlowATI/honeybee_model_repo",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",
)
