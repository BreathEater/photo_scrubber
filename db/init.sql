\c scrubber_db

CREATE TABLE IF NOT EXISTS system_stats(
	id SERIAL PRIMARY KEY,
	photos_cleaned INTEGER DEFAULT 0,
	bytes_removed BIGINT DEFAULT 0,
	last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);

INSERT INTO system_stats (photos_cleaned, bytes_removed) VALUES (0,0);

GRANT ALL PRIVILEGES ON TABLE system_stats OWNER TO scrubber_app_user;
GRANT USAGE, SELECT ON SEQUENCE system_stats_id_seq OWNER to scrubber_app_user;
