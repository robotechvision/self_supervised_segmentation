"""Check that the ROS 2 packaging of this repository stays consistent.

Deliberately imports nothing from `stego`: this has to pass in an environment that
can build the package but has not installed the learning stack yet.
"""

import os
import re
import xml.etree.ElementTree as ElementTree

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_NAME = "stego"


def test_manifest_name_matches_setup_py():
    """package.xml, setup.py and the ament resource marker must agree on the name."""
    manifest = ElementTree.parse(os.path.join(REPO, "package.xml")).getroot()
    assert manifest.findtext("name") == PACKAGE_NAME

    build_type = manifest.findtext("export/build_type")
    assert build_type == "ament_python", f"expected an ament_python package, got {build_type}"

    setup_py = open(os.path.join(REPO, "setup.py")).read()
    assert re.search(rf'^package_name = "{PACKAGE_NAME}"$', setup_py, re.MULTILINE)

    marker = os.path.join(REPO, "resource", PACKAGE_NAME)
    assert os.path.isfile(marker), f"missing the ament index marker {marker}"


def test_model_config_ships_with_the_package():
    """Stego() reads this file when constructed without a config, so it must install."""
    assert os.path.isfile(os.path.join(REPO, PACKAGE_NAME, "cfg", "model_config.yaml"))

    setup_py = open(os.path.join(REPO, "setup.py")).read()
    assert 'package_data={package_name: ["cfg/*.yaml"]}' in setup_py
