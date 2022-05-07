{{ cookiecutter.project_name }} Project
==============

This is a Docker (with docker-compose) environment for {{ cookiecutter.project_name }} Project.

# Installation

1. First, clone this repository:

```bash
git clone https://github.com/<repository-slug-here>
```
2. Copy the environment vars:

```bash
cp .env.dist .env
```
3. Init project
```bash
make
```
4. Show containers:
```bash
make ps
```
This results in the following running containers:
```bash
docker-compose ps
  Name                Command                  State               Ports
---------------------------------------------------------------------------------
core       /bin/sh -c flask db upgrad ...   Up             0.0.0.0:5000->5000/tcp
postgres   docker-entrypoint.sh postgres    Up (healthy)   0.0.0.0:5432->5432/tcp                    Exit 0
```
5. Testing features:
```bash
make test
```
6. Managing dependencies with Poetry:
```bash
### To add
docker-compose run --rm core poetry add <dependenciy_name>

### To remove
docker-compose run --rm core poetry remove <dependenciy_name>
```
