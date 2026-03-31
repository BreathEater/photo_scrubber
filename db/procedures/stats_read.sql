CREATE OR REPLACE FUNCTION stats_read()
RETURNS TABLE(cleaned BIGINT, bytes BIGINT) AS $$
BEGIN
	RETURN QUERY SELECT 
	sum(photos_cleaned)::BIGINT,
	sum(bytes_removed)::BIGINT
	FROM system_stats;
END;
$$ LANGUAGE plpgsql;
