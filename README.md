# ETL pipeline
Apply ETL steps
1. extract
2. create Postgres tables
3. transform
4. load

```
.
├── README.md
├── data
│   ├── raw
│   │   └── downloaded_at=2021-02-01
│   │       └── ppr-all.csv
│   └── source
│       └── downloaded_at=2021-02-01
│           └── PPR-ALL.zip
└── scripts
    ├── common
    │   ├── base.py
    │   └── tables.py
    ├── create_tables.py
    ├── execute.py
    ├── extract.py
    ├── load.py
    └── transform.py
```

## try it
### Create a virtual environment
```sh
python -m venv .property_price_etl
source .property_price_etl/bin/activate
pip install -r requirements.txt
```
### pull Posgres image
```sh
docker pull postgres:alpine
```
### Run Postgres on docker
```sh
docker run -it \
    --name "property_price" \
    -e POSTGRES_USER="admin"\
    -e POSTGRES_PASSWORD="admin"\
    -e POSTGRES_DB="property_price"\
    -p 5432:5432 \
    postgres:alpine
```
### execute etl pipeline
```sh
python scripts/execute.py
```

### pgcli from other terminal
```sh
pgcli postgresql://admin:admin@localhost:5432/property_price
```
check tables
```sh
\dt
```
show first 5 rows
```sh
SELECT * FROM ppr_clean_all LIMIT 5;
```