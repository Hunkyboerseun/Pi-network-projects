import os
from fastapi import APIRouter, HTTPException
from app.database import get_db_connection

router = APIRouter()

MIGRATION_TOKEN = os.getenv("MIGRATION_TOKEN", "default")

@router.post("/run-migration")
def run_migration(token: str):
    if token != MIGRATION_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized migration token")

    sql_file_path = os.path.join(os.path.dirname(__file__), "..", "sql", "schema.sql")
    sql_file_path = os.path.abspath(sql_file_path)

    if not os.path.exists(sql_file_path):
        raise HTTPException(status_code=404, detail=f"SQL file not found: {sql_file_path}")

    # Load SQL
    with open(sql_file_path, "r") as file:
        sql_script = file.read()

    # Execute SQL
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(sql_script)
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Migration failed: {str(e)}")
    finally:
        cur.close()
        conn.close()

    return {"status": "success", "message": "Migration executed successfully"}
