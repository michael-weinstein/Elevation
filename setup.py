import os, shutil
# from Cython.Build import cythonize
from setuptools import setup

import elevation

pj = lambda *paths: os.path.abspath(os.path.join(*paths))
repo_dir = os.path.abspath(os.path.dirname(__file__))

# initialize settings.py file.
if not os.path.exists(pj(repo_dir, "elevation/settings.py")):
    print("Using default settings_template.py")
    shutil.copyfile("elevation/settings_template.py", "elevation/settings.py")


setup(
    name='Elevation',
    version=elevation.__version__,
    author='Nicolo Fusi and Jennifer Listgarten',
    author_email="fusi@microsoft.com, jennl@microsoft.com",
    description=("Machine Learning-Based Predictive Modelling of CRISPR/Cas9 off-target effects"),
    packages=["elevation"],
    install_requires=['scipy==1.2.3', 'numpy', 'matplotlib==2.2.5', 'nose==1.3.7', 'scikit-learn>=0.18', 'pandas', 'joblib==0.12.5', 'mock==2.0.0', 'multiprocess==0.70.6.1', 'statsmodels==0.9.0', 'requests==2.18.4', 'xlrd==1.1.0'],
    license="BSD",
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'elevation-fixtures = elevation.cmds.fixtures:Fixtures.cli_execute',
            'elevation-fit = elevation.cmds.fit:Fit.cli_execute',
        ],
    }
)
