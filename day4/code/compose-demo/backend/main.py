import os

import pymysql
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Items API")


def get_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "app"),
        password=os.getenv("DB_PASSWORD", "apppass"),
        database=os.getenv("DB_NAME", "shop"),
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT id, name, price FROM items ORDER BY id")
            return cur.fetchall()
    except pymysql.MySQLError as exc:
        raise HTTPException(status_code=503, detail=f"database error: {exc}")
