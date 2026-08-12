#
# Copyright (c) 2022-2024, ETH Zurich, Piotr Libera, Jonas Frey, Matias Mattamala.
# All rights reserved. Licensed under the MIT license.
# See LICENSE file in the project root for details.
#
#
import os

from .data import UnlabeledImageFolder, DirectoryDataset, ContrastiveSegDataset
from .stego import Stego


STEGO_ROOT_DIR = os.environ.get("STEGO_ROOT_DIR") or os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
"""Absolute path to the stego repository.

This is where the pre-trained weights are looked up, under ``models/``. It is
derived from the location of this file, which only holds as long as the package
still sits in the checkout -- true for a source tree, a ``pip install -e`` and a
``colcon build --symlink-install``, but not for an installation that copies the
package out of it. Set the ``STEGO_ROOT_DIR`` environment variable to point at the
directory holding ``models/`` in that case.
"""
