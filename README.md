# Template

---

_version 0.0.1_

_date 26.08.2023_

---

## Back-end | REST | API | Fast API

### Overview
1. Setup

### Setup
1. Clone project
2. Install Pipenv
3. Install dependencies `pipenv install`
4. Add and edit environment file `.env`. Optional `.env.prod` can be added
5. Configure run script (IDE)
6. Run application `pipenv run main.py`

### Run docker
1. Install **make** utility
2. Run `make build`
3. Run `make run`

### Create Database Postgres(Linux)
1. `sudo apt update`
2. `sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib`
3. `sudo -u postgres psql`
4. `CREATE DATABASE myproject;`
5. `CREATE USER myprojectuser WITH PASSWORD 'password';`
6. `ALTER ROLE myprojectuser SET client_encoding TO 'utf8';`
7. `ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';`
8. `ALTER ROLE myprojectuser SET timezone TO 'UTC';`
9. `GRANT ALL ON DATABASE mydb TO admin;`
10. `ALTER DATABASE mydb OWNER TO admin;`
11. `GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;`

### Make migrations

#### Option 1 - Pipenv run scripts

1. Run `pipenv run auto_migration`
2. Run `pipenv run migrate`

#### Option 2 - Makefile run scripts

1. Run `make migrate`
