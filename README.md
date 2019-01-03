## Car notifier webapp

# Build an run the application
```bash
sudo apt install docker-compose -y
docker-compose up --detach --build && sensible-browser localhost
```

# Todo
The migrations directory from flask-migrate gets generated in the root directory
However if it is generated using the `--directory` flag. It seems to stop working

The contradiction here is that it cannot be added to the docker image out of context.
The current workaround is to mount it as a volume
