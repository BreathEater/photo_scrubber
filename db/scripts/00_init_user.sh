#!/bin/bash
set -e

# Use the environment variables injected by Docker
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER $BAU_DB_USER WITH PASSWORD '$BAU_DB_PASSWORD';
	GRANT ALL PRIVILEGES ON DATABASE $POSTGRES_DB TO $BAU_DB_USER;
EOSQL


