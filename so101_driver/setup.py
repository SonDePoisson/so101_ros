from setuptools import find_packages, setup

package_name = "so101_driver"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools", "st3215"],
    zip_safe=True,
    maintainer="clement",
    maintainer_email="clement.poissoncornu@gmail.com",
    description="TODO: Package description",
    license="TODO: License declaration",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "so101_joint_trajectory_controller = so101_driver.so101_joint_trajectory_controller:main",
        ],
    },
)
