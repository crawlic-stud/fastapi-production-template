# Fastapi production template

This project is inspired by [fastapi-alembic-sqlmodel-async](https://github.com/jonra1993/fastapi-alembic-sqlmodel-async) template

### Features:

- [X] Fully Dockerized
- [X] bitnami PostgreSQL
- [X] SQLModel (SQLAlchemy)
- [X] Alembic
- [X] Starlette-admin with Auth
- [X] Basic JWT Auth service
- [X] Basic Email service for confirmation codes
- [X] Caddy reverse proxy
- [ ] gunicorn support
- [ ] pgadmin
- [ ] Celery + Redis
- [ ] Optional: MinIO storage
- [ ] Optional: Telemetry with Prometheus and Grafana


### Commands:

1. ```make install``` - install dependencies (recommended to only use in venv)
1. ```make install-venv``` - create venv and install dependencies
1. ```make run-dev``` - run development server with auto-reload
1. ```make run-prod``` - run production server 
1. ```make revision msg="revision text"``` - create autogenerated alembic revision with specified message
1. ```make upgrade``` - run alembic migrations
1. ```make downgrade``` - undo latest alembic migration
1. ```make help``` - view all commands