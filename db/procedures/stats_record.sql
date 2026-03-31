CREATE OR REPLACE PROCEDURE stats_record(p_count INTEGER, p_bytes BIGINT)
LANGUAGE plpgsql AS $$
BEGIN
	INSERT INTO system_stats (photos_cleaned, bytes_removed, last_updated)
	VALUES (p_count, p_bytes, CURRENT_TIMESTAMP);
END;
$$;
