from setuptools import setup
import os
from glob import glob

package_name = "so101_description"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        # URDF
        (os.path.join("share", package_name, "urdf"), glob("urdf/*.urdf")),
        # Meshes (urdf/assets)
        (os.path.join("share", package_name, "urdf/assets"), glob("urdf/assets/*")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Clément Poisson",
    maintainer_email="clement.poissoncornu@gmail.com",
    description="SO101 Description with URDF and STL meshes",
    license="MIT",
)
