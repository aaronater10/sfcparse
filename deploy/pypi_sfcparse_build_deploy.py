import sys
import os
import subprocess

# Setup
SFCPARSE_VERSION = "1.3.0"
DEPLOY_API_TOKEN = f"{sys.argv[1]}"
USER_HOMEPATH = os.getenv('HOME')
USER_PYPI_CFG_FILE = f"{USER_HOMEPATH}/.pypirc"
PYPI_UNIQUE_ID = "__token__"

# Create PyPI Config File for API Auth
with open(USER_PYPI_CFG_FILE, 'w') as f:
    file_Data = f.write(f"""[distutils]
index-servers =
    pypi
    sfcparse

[pypi]
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}

[sfcparse]
  repository = https://upload.pypi.org/legacy/
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}"""
)

# Attempt to Deploy, if ANY FAILURES, report and always remove API Token file
try:
    # Change to Deploy Dir
    os.chdir('deploy/')

    # Prep sfcparse Files for Build
    subprocess.run("cp -f -r ../src/sfcparse/ .", shell=True)
    subprocess.run("cp -f ../README.md .", shell=True)

    # Build Wheel from Setup, then Publish to PyPI
    subprocess.run(f"python3 -B setup.py {SFCPARSE_VERSION} sdist bdist_wheel", shell=True)
    subprocess.run(f'python3 -B -m twine upload --repository "sfcparse" dist/* --verbose', shell=True)
    subprocess.run('echo "SUCCESS: sfcparse deployment"', shell=True)
except:
    subprocess.run('echo "FAILED: sfcparse deployment"', shell=True)
finally:
    # Cleanup PyPI Config with API Token
    subprocess.run(f"rm -f {USER_PYPI_CFG_FILE}", shell=True)
