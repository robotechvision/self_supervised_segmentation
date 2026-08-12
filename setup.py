#
# Copyright (c) 2022-2024, ETH Zurich, Piotr Libera, Jonas Frey, Matias Mattamala.
# All rights reserved. Licensed under the MIT license.
# See LICENSE file in the project root for details.
#
#
import os

from setuptools import find_packages, setup

package_name = "stego"

# Dependencies for a plain `pip install -e .`. colcon does not install these: an
# ament_python build runs `setup.py install --single-version-externally-managed`,
# which skips dependency resolution, so a ROS 2 workspace build only needs them to
# be importable already.
INSTALL_REQUIRES = [
    # generic
    "numpy",
    "tqdm",
    "kornia>=0.6.5",
    "pip",
    "torchvision",
    "torch>=1.21",
    "torchmetrics",
    "pytorch_lightning>=1.6.5",
    "pytest",
    "scipy",
    "scikit-image",
    "scikit-learn",
    "matplotlib",
    "seaborn",
    "pandas",
    "pytictac",
    "torch_geometric",
    "omegaconf",
    "optuna",
    "neptune",
    "fast-slic",
    "hydra-core",
    "prettytable",
    "termcolor",
    "pydensecrf@git+https://github.com/lucasb-eyer/pydensecrf.git",
    "liegroups@git+https://github.com/mmattamala/liegroups",
    "opencv-python",
    "wget",
    "rospkg",
    "wandb",
    "gdown",
]

setup(
    name=package_name,
    version="0.0.1",
    author="Piotr Libera, Jonas Frey, Matias Mattamala",
    author_email="plibera@student.ethz.ch, jonfrey@ethz.ch, matias@leggedrobotics.com",
    packages=find_packages(exclude=["scripts", "scripts.*"]),
    # Stego() falls back to stego/cfg/model_config.yaml when it is constructed
    # without a config, so the file has to travel with the installed package.
    package_data={package_name: ["cfg/*.yaml"]},
    python_requires=">=3.8",
    description="Self-supervised semantic segmentation package based on the STEGO model",
    license="MIT",
    install_requires=INSTALL_REQUIRES,
    # Makes `colcon test` run pytest, which honours the `testpaths` in
    # pyproject.toml and so only looks at test/. The alternative, unittest
    # discovery, imports every package it descends into and would need the whole
    # learning stack just to find that there are no tests.
    tests_require=["pytest"],
    # Makes the checkout a ROS 2 (ament_python) package as well, so that a ROS 2
    # workspace can build it with colcon rather than pip installing it separately.
    data_files=[
        ("share/ament_index/resource_index/packages", [os.path.join("resource", package_name)]),
        (os.path.join("share", package_name), ["package.xml"]),
    ],
)
