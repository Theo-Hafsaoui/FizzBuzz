import sqlite3

__CON = None
DB_PATH = "./stat.db"
CREATE_QUERRY = """
CREATE TABLE IF NOT EXISTS request (
  Int1 TEXT,
  Int2 TEXT,
  Str1 TEXT,
  Str2 TEXT,
  Limit_request TEXT,
    Hit INTEGER DEFAULT 1,
  PRIMARY KEY (Int1, Int2, Str1, Str2, Limit_request)
);

"""
# CREATE INDEX idx_hit_desc ON request(Hit DESC);

GET_QUERRY = """
SELECT *
FROM request
ORDER BY Hit DESC
LIMIT 1;
"""

SAVE_QUERRY = """
INSERT INTO request(Int1, Int2, Str1, Str2, Limit_request, Hit)
VALUES (?, ?, ?, ?, ?, 0)
ON CONFLICT(Int1, Int2, Str1, Str2, Limit_request)
DO UPDATE SET Hit = request.Hit + 1;
"""


def connect():
    """
    Give the connection to the database
    """
    global __CON
    if __CON is None:
        __CON = sqlite3.connect(DB_PATH, check_same_thread=False)
    return __CON


def init():
    """
    Init the connection to the database
    """
    print("--INIT DB--")
    db_connection = connect()
    with db_connection:
        try:
            db_connection.execute(CREATE_QUERRY)
        except Exception as ex:
            print(f"Err:{ex}")


async def save_querry(int1: str, int2: str, str1: str, str2: str, limit: str):
    """
    Save a querry in the database
    """
    db_connection = connect()
    with db_connection:
        try:
            db_connection.execute(SAVE_QUERRY, (int1, int2, str1, str2, limit))
        except Exception as ex:
            print(f"Err:{ex}")


def get_most_used_querry():
    """
    Querry the database to obtain the most used querry in the databse
    """
    db_connection = connect()
    res = ""
    with db_connection:
        try:
            res = db_connection.execute(GET_QUERRY).fetchone()
        except Exception as ex:
            print(f"Err:{ex}")
            return ""
    return res


init()
