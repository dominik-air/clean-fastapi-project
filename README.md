# clean-fastapi-project

## Docker commands for running the project

Create user defined network:

```docker
docker create network <network_name>
```

For each Dockerfile build an image:

```docker
docker build -t <image_name> <Dockerfile_directory_path>
```

Run containers and connect them to the user defined network:

```docker
docker run --name <container_name> --network <network_name> -d -p <external_port>:<internal_port> <image_name>
```

I still have to improve the networking since it's linked kinda dirty right now :)
