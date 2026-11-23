# CyberIncident API

A simple REST API prototype for simulated cybersecurity incident reporting. Built for the PWL UTS project with Flask, SQLAlchemy ORM, SQLite, and an MVC-style separation (models, controllers, routes).


## Features
- CRUD for users, assets, incident categories, and incidents
- Incident handling history
- Search by incident title, filter by status/severity, pagination
- Input validation and consistent JSON error responses
- Pytest automated tests

## Requirements
Python 3.10+ recommended.

## Run locally (macOS/Linux)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed.py
python run.py
```
API base URL: `http://127.0.0.1:5000/api/v1`

## Database migrations (Flask-Migrate)
```bash
export FLASK_APP=run.py
flask db init       # run once only to create migrations folder
flask db migrate -m "initial tables"
flask db upgrade
```
For a quick local prototype, `python seed.py` creates tables and example data automatically. Migration commands are included for the required migration workflow; don't run `flask db init` repeatedly if migrations folder already exists.

## Seed demo data
```bash
python seed.py
```
Creates example user, asset, category, and incident (id values depend on database state). All data is simulation-only; IP `192.0.2.10` is reserved for documentation.


## Test
```bash
pytest -v
```

## API endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/health` | Health check |
| GET/POST | `/api/v1/users` | List/create user |
| GET/PUT/DELETE | `/api/v1/users/{id}` | Retrieve/update/delete user |
| GET/POST | `/api/v1/assets` | List/create asset |
| GET/PUT/DELETE | `/api/v1/assets/{id}` | Retrieve/update/delete asset |
| GET/POST | `/api/v1/categories` | List/create category |
| GET/PUT/DELETE | `/api/v1/categories/{id}` | Retrieve/update/delete category |
| GET/POST | `/api/v1/incidents` | List/create incident |
| GET/PUT/DELETE | `/api/v1/incidents/{id}` | Retrieve/update/delete incident |
| POST | `/api/v1/incidents/{id}/updates` | Add handling update and change incident status |
| GET | `/api/v1/incidents/{id}/updates` | List incident handling history |

### Incident list query options
- `search`: partial title match, e.g. `?search=phish`
- `status`: `open`, `investigating`, `resolved`, `closed`
- `severity`: `low`, `medium`, `high`, `critical`
- `page`: page number (default 1)
- `per_page`: results per page (default 10, max 100)
Example: `/api/v1/incidents?status=open&severity=high&page=1&per_page=10`


## Sample request bodies

### Create user
```json
{"name":"Alya","email":"alya@example.com","role":"reporter"}
```
Roles: `reporter`, `analyst`, `admin`.

### Create asset
```json
{"asset_name":"Lab Server","asset_type":"server","ip_address":"192.0.2.20","description":"Simulated test asset"}
```

### Create category
```json
{"name":"Malware","description":"Malicious software incident"}
```

### Create incident
```json
{"title":"Suspicious login","description":"Repeated failed login attempts in simulated environment","severity":"high","status":"open","user_id":1,"asset_id":1,"category_id":1}
```
Severity: `low`, `medium`, `high`, `critical`. Status: `open`, `investigating`, `resolved`, `closed`.

### Add incident update
```json
{"user_id":1,"status":"investigating","note":"Reviewing simulated event logs."}
```

## Typical response
```json
{"success":true,"message":"User berhasil dibuat","data":{"id":1,"name":"Alya","email":"alya@example.com","role":"reporter","created_at":"2026-01-01T00:00:00+00:00"}}
```

## HTTP codes
- `200`: request success
- `201`: created
- `400`: invalid input
- `404`: missing resource/reference
- `409`: duplicate or conflict
- `500`: server error

## Data model (5 tables)
- `users`: reporter/analyst identity
- `assets`: simulated device/server/web asset
- `incident_categories`: incident classification
- `incidents`: reported incident, references user, asset, category
- `incident_updates`: status/action history, references incident and user


## Safety and scope
This application uses fictional/simulated records only. Do not use it to scan, test, or attack systems you do not own or have permission to assess. No real scanning or exploit functions are included.


## Future UAS scope
- JWT authentication and role-based access
- Deployment and environment configuration hardening
- API documentation UI/OpenAPI improvements
- Frontend dashboard/visualization
- More comprehensive test coverage

