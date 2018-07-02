import codecs
import os.path

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="gps-routes",
    use_scm_version={
        "root": here,
        "write_to": os.path.join(here, "gps_routes/_version.py"),
    },
    description="GPS Routes service",
    long_description=long_description,
    packages=find_packages(where=here),
    package_data={"gps_routes": ["swagger.yml"]},
    install_requires=["connexion", "flask", "gunicorn"],
    setup_requires=["setuptools_scm"],
    extras_require={
        "tests": [
            "flake8",
            "isort",
            "pytest",
            "pytest-cov",
            "unify",
        ],
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",

        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ],
)
