CREATE USER scrubber_app_user WITH PASSWORD 'scrubber_app_P@$$1994';

\c scrubber_db

CREATE TABLE IF NOT EXISTS system_stats(
	id SERIAL PRIMARY KEY,
	photos_cleaned INTEGER DEFAULT 0,
	bytes_removed BIGINT DEFAULT 0,
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);

INSERT INTO system_stats (photos_cleaned, bytes_removed) VALUES (0,0);

ALTER TABLE system_stats OWNER TO scrubber_app_user;
ALTER SEQUENCE system_stats_id_seq OWNER to scrubber_app_user;
