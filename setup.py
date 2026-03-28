from setuptools import setup, find_packages

setup(
    name="canoe-robot-lib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "robotframework",
        "py_canoe"
    ],
    author="Naresh Kothari",
    description="Robot Framework library for CANoe automation",
    python_requires=">=3.8",
)