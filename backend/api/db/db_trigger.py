from db_connection import get_db_connection

def trigger_db_procedure(procedure_name: str, *args):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            placeholders = ", ".join(["%s"] * len(args))
            cur.execute(f"CALL {procedure_name}({placeholders});", args)
            conn.commit()

def trigger_db_function(func_name: str):
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {func_name}();")
            return cur.fetchone()

