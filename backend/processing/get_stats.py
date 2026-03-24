from db_connection import get_db_connection

def get_photos_cleaned_count() -> int:

    with get_db_connection() as conn:
        with conn.cursor() as cur:

            cur.execute("SELECT COUNT(photos_cleaned) FROM system_stats;")

            result = cur.fetchone()
            return result[0] if result else 0

        
