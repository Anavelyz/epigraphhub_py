# type: ignore[attr-defined]
"""Epigraphhub Python package"""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "2.0.5"  # changed by semantic-release


version: str = get_version()
__version__: str = version
