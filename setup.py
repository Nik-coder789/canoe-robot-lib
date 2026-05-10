from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="canoe-robot-lib",
    version="0.8s",
    packages=find_packages(),
    install_requires=[
        "robotframework",
        "py_canoe",
        "cantools"
    ],
    author="Naresh Kothari",
    description="Robot Framework library for CANoe automation",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/Nik-coder789/canoe-robot-lib",
    project_urls={
        "Documentation":"https://github.com/Nik-coder789/canoe-robot-lib/blob/main/KEYWORDS.md",
        "Homepage": "https://github.com/Nik-coder789/canoe-robot-lib",
        "Repository": "https://github.com/Nik-coder789/canoe-robot-lib",
    },

    keywords=["canoe", "robot framework", "automation", "automotive"],
    python_requires=">=3.7",
)