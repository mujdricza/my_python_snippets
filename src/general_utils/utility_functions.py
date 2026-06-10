"""
Utility functions for general purposes.
"""

import subprocess
import sys
from typing import Dict, List


def sorted_stringlist_case_insensitive(stringlist: List[str]) -> List[str]:
    return sorted(stringlist, key=lambda x: x.lower())


def sorted_dict_case_insensitive(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items(), key=lambda x: x[0].lower()))


def install_if_needed(package_name: str) -> None:
    """Install a package if not yet installed.

    Use it only for experimental code, prefer setup scripts (e.g. pyproject.toml, setup.py) instead.

    :param package_name: Name of the package to install.
    """
    try:
        subprocess.run([sys.executable, "-c", "import", package_name], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                       )
    except subprocess.CalledProcessError:
        subprocess.call([sys.executable, "-m", "pip", "install", package_name],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
