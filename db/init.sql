CREATE TABLE IF NOT EXISTS system_stats(
	id SERIAL PRIMARY KEY,
	photos_cleaned INTEGER DEFAULT 0,
	bytes_removed BIGINT DEFAULT 0,
	last_updated TIMESTAMP DEAFULT CURRENT_TIMESTAMP
	);

INSERT INTO system_stats (photos_cleaned, bytes_removed) VALUES (0,0);
