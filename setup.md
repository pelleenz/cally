# Requirement

- Docker daemon installed on local system
- Extension Pack "Remote Development" installed in VSCode

# Setting up a Dev Container

1. copy Dev Container to a new Projec folder
2. declare desired VSCode Extensions in devcontainer.json under "extensions"
3. declare needed Python Packets in requirements.txt
4. start Docker daemon on local system
5. start Container with VSCode Command "Dev Containers: Rebuild and Reopen in Container"
6. Python Debugger Extension needs to be installed separatly

# Pushing to Production

1. Uncomment the ENTRYPOINT Lines in all Dockerfiles
2. Uncomment ADD Line in all Dockerfiles
3. delete sleep infinity command from Docker-Compose file
4. delete volume mount from Docker-Compose file
5. build Container Image standalone or use the Docker-Compose file
