## Docker & Docker Compose tips

### Create a new Docker based Rails app

[Check this Rails 6 Docker example](https://github.com/jensendarren/rails6-docker-demo)

### Basic commands

A good image to use for playing around with Docker and Docker Compose is `tutum/hello-world`

NOTE 1 : If there is a `.env` file in the project directory then it's values will be picked up by compose.

NOTE 2: If there is a `docker-compose.override.yml` file in the same directory then running `docker-compose up` will merge the two files together to create a single config. The override file could be put into a .gitignore file thus allowing developers to make speciif local only changes there without causing issues with others.

`docker-compose exec <service-name> bash`

`docker network ls`

`docker network inspect <name>`

`docker inspect <container-name>`

`docker inspect --format '{{.LogPath}}' <container-name>`

`docker-compose logs -f`

`docker volume ls`

`docker-compose config` #verifies the config is valid

`docker system prune`

`docker-compose up --build clik.apps.crm`

* Stop and remove all Docker containers

`docker stop $(docker ps -a -q)
docker rm -f $(docker ps -a -q)`

* Remove all untagged images

`docker rmi -f $(docker images | grep "<none>" | awk "{print \$3}")`

### Run a command in a running *container* overriding the default entrypoint
`docker run -it --entrypoint bash ff095591b4d6`

### Run a command from starting up a new container *from an image* and overriding the default entrypoint
`docker run -it --entrypoint bash clik/crm:77ad795`

Another example (without using the --entrypoint flag):

`docker run -di rails6-demo_web bash`

### Run a commmand from a Docker image that requires mounting the local file structure (example below is using terraform)

`docker run -it --rm -v $(pwd):/tf -w /tf hashicorp/terraform:light init`

### Attach a debugger to a running Docker Container

Follow these steps:

1. Put the breakpoint in the code
1. Attach to the running docker container like so `docker attach CONTAINER_ID`
1. Execute the action which will cause the breakpoint to hit

### ... via Docker Compose

Esentially you need to add the following to the docker compose service that you want to debug:

```
stdin_open: true
tty: true
```

Then you simply run `docker attach CONTAINER_ID` and run the code / hit the end point that will cause the debugger to start.

NOTE: To DETACH from the running container WITHOUT stopping it follow the CTRL-p + CTRL-q key sequence

See [this example](https://blog.lucasferreira.org/howto/2017/06/03/running-pdb-with-docker-and-gunicorn.html) for more details.

### Running Postgres in a Docker Container

Run a postgres instance in Docker like so:

`docker run --name postgres_server -e POSTGRES_PASSWORD=mysecretpassword -v postgres_data:/var/lib/postgresql/data -d -p 5432:5432 postgres:10.6`

Now connect to the running server instance `docker exec -it postgres_server_container_id bash;`

...and create the database like so:

```
su - postgres
psql
create database "mycooldb";
```

Test connecting to the database server via the host (i.e. from outside the running db container):

`psql -h localhost -p 5432 -U postgres`

You will be asked for the Postgres server password which is set in the `docker run` command as an environment variable above.

Given the psql CLI connects to the database, the following general psql connection string should also work:

`postgresql://postgres:mysecretpassword@localhost:5432/pyapi-development`

### Let's say you want to test some sql file or data dump someone sent you
### Fire up Postgres instance mounting the folder where the sql files are (e.g. Downloads)

`docker run -v ~/Downloads:/var/data -d postgres:10.6`

### Connect to the running instance using your shortcut

`dexec CONTAINER_ID`

### In postgres you may need to create the database first and then run the folling

`psql -U postgres -d some_database -a -f some_dump_file.sql`

### Copy file from running container to local file system:

`docker cp <containerId>:/file/path/within/container /host/path/target`

### Build a new image from a Dockerfile

To build a new image locally use `docker build` as follows

```
docker build -t name:v1 .
```

### Build a new image from a Specific Dockerfile

```
docker build -t mycoolimage:v1 -f custom.Dockerfile .
```

### Check the SHA256 of an image

The SHA256 is useful to verify if the image you have is the one you expect!

```
docker inspect image-name | grep sha256
```

## Docker Compose

### Using Docker Compose to start all services in the docker-compose.yml file

```
docker-compose up
```

### Using Docker Compose to start a specific service

```
docker-compose start mycoolservice
```

### Docker Compose to stop a specific service

```
docker-compose stop mycoolservice
```

### Docker Compose to remove the container created for the service

```
docker-compose rm -f -v mycoolservice
```

### Docker Compose to create a new container created for the service

```
docker-compose create --force-recreate mycoolservice
```