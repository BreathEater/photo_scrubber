CREATE OR REPLACE FINCTION stats_summary_read()
RETURNS TABLE(cleaned INTEGER, bytes BIGINT) AS $$
BEGIN
	RETURN QUERY SELECT photos_cleaned, bytes_removed FROM system_stats LIMIT 1;
END;
$$ LANGUAGE plpgsql;
