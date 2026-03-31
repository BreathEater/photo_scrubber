   #!/bin/bash
   set -e

   # This shell script will now correctly 'see' your .env variables!
   psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
       CREATE TABLE IF NOT EXISTS system_stats(
           id SERIAL PRIMARY KEY,
           photos_cleaned INTEGER DEFAULT 0,
           bytes_removed BIGINT DEFAULT 0,
           last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
       );

       INSERT INTO system_stats (photos_cleaned, bytes_removed)
   VALUES (0,0);

       GRANT ALL PRIVILEGES ON TABLE system_stats TO $BAU_DB_USER;
       GRANT USAGE, SELECT ON SEQUENCE system_stats_id_seq TO
   $BAU_DB_USER;

       GRANT EXECUTE ON ALL ROUTINES IN SCHEMA public TO
   $BAU_DB_USER;

       ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT EXECUTE ON
   ROUTINES TO $BAU_DB_USER;
EOSQL


