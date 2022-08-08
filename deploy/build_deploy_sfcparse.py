import sys
import os
import subprocess

# Setup
SFCPARSE_VERSION = "1.3.1"
DEPLOY_API_TOKEN = f"{sys.argv[1]}"
DEPLOY_SSH_KEY = f"{sys.argv[2]}"
USER_HOMEPATH = os.getenv('HOME')
USER_PYPI_CFG_FILE = f"{USER_HOMEPATH}/.pypirc"
PYPI_UNIQUE_ID = "__token__"
USER_GITHUB_CFG_FILE = f"{USER_HOMEPATH}/.gitconfig"
USER_SSH_KEY_FILE = f"{USER_HOMEPATH}/.ssh/id_ssh.deploy"
USER_SSH_CFG_FILE = f"{USER_HOMEPATH}/.ssh/config"
GITHUB_SFCPARSE_REPO = "git@github.com:aaronater10/sfcparse.git"

# Create SSH Path, Key File, and Set Permissions
subprocess.run(f'mkdir -p "{USER_HOMEPATH}/.ssh"', shell=True)
with open(USER_SSH_KEY_FILE, 'w') as f:
    f.write(DEPLOY_SSH_KEY)
    subprocess.run(f'chmod 600 "{USER_SSH_KEY_FILE}"', shell=True)

# Create SSH Config File for SSH Auth
with open(USER_SSH_CFG_FILE, 'w') as f:
    f.write(
f"""
Host github.com-sfcparse
    Hostname github.com
    IdentityFile {USER_SSH_KEY_FILE}
    IdentitiesOnly yes
"""
)

# Create PyPI Config File for API Auth
with open(USER_PYPI_CFG_FILE, 'w') as f:
    f.write(f"""[distutils]
index-servers =
    pypi
    sfcparse

[pypi]
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}

[sfcparse]
  repository = https://upload.pypi.org/legacy/
  username = {PYPI_UNIQUE_ID}
  password = {DEPLOY_API_TOKEN}
"""
)

# Create GitHub Config File for SSH Auth
with open(USER_GITHUB_CFG_FILE, 'w') as f:
    f.write(
"""[user]
    email = dev_admin@dunnts.com
    name = aaronater10

[url "git@github.com:"]
    insteadOf = https://github.com/
"""
)


# Attempt to Deploy, if ANY FAILURES, report and always remove API Token file
try:
    # Change to Deploy Dir
    os.chdir('deploy/')

    ### PYPI ###
    # Prep sfcparse Files for Build
    subprocess.run("cp -f -r ../src/sfcparse/ .", shell=True)
    subprocess.run("cp -f ../README.md .", shell=True)

    # Build Wheel from Setup, then Publish to PyPI
    subprocess.run(f"python3 -B setup.py {SFCPARSE_VERSION} sdist bdist_wheel", shell=True)
    subprocess.run(f'python3 -B -m twine upload --repository "sfcparse" dist/* --verbose', shell=True)
    subprocess.run('echo "SUCCESS: sfcparse deployment"', shell=True)

    ### GITHUB ###
    # Clone and Tag New Release Number
    subprocess.run(f"git clone {GITHUB_SFCPARSE_REPO}", shell=True)
    os.chdir('sfcparse/')
    subprocess.run(f"git tag v{SFCPARSE_VERSION} -m 'Release v{SFCPARSE_VERSION}'", shell=True)
    subprocess.run(f"git push origin v{SFCPARSE_VERSION}", shell=True)
    os.chdir('..')
except:
    subprocess.run('echo "FAILED: sfcparse deployment"', shell=True)
finally:
    # Cleanup PyPI Config with API Token
    subprocess.run(f"rm -f {USER_PYPI_CFG_FILE}", shell=True)
    # Cleanup SSH Key File
    subprocess.run(f"rm -f {USER_SSH_KEY_FILE}", shell=True)
