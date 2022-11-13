# Google Artifact Registry 

## Content 
- Artifact Registry Python Repo
- Artifact Registry Docker Repo
- Artifact Registry Node.js Repo

## About
Artifact Registry enables you to centrally store artifacts and build dependencies as part of an integrated Google Cloud experience.


## Getting Started Python Repo 
```bash
# create python repo
./init-python-repo.sh

# create packages and modules
cd python
mkdir my_packages_1
mkdir my_packages_1/yu_lib_1
touch my_packages_1/yu_lib_1/__init__.py

# create package relevant files
touch my_packages_1/yu_lib_1/setup.cfg
touch my_packages_1/yu_lib_1/setup.py
VERSION
```
