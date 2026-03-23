CREATE OR REPLACE PROCEDURE stats_record(p_bytes INTEGER)
LANGUAGE plpgsql AS $$
BEGIN
	UPDATE system_stats
	SET photos_cleaned = photos_cleaned + 1,
		bytes_removed = bytes_removed + p_bytes,
		last_updated = CURRENT_TIMESTAMP
	WHERE id = (SELECT id FROM system_stats LIMIT 1);
END;
$$;
