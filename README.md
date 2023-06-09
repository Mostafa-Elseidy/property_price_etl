[![ETL with Python and Postgres with Github Actions](https://github.com/Mostafa-Elseidy/property_price_etl/actions/workflows/main.yml/badge.svg)](https://github.com/Mostafa-Elseidy/property_price_etl/actions/workflows/main.yml)

# property_price_etl
Apply ETL steps with Python and Postgres
1. extract
    - request and download data as zip file in source directory
    - unzip csv in raw directory
2. create Postgres tables
    - raw table
    - clean table
3. transform
    - lowercase fields
    - update date format, description, price 
4. load
    - insert new rows
    - delete any row not present in the last snapshot

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
### pull Postgres image
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
