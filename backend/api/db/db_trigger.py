from db_connection import get_db_connection

def trigger_db_operation(procedure_name: str, *args):

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"CALL {procedure_name}(%s);", args)
            conn.commit()
