from sqlalchemy.engine import create_engine
from LMNFlask import app
from typing import Union
# from utils.database.schema import schema
schema = ["SELECT * FROM pg_catalog.pg_tables"]

DB_URL = app.config["DB_CONN"]
engine = create_engine(DB_URL, echo=True)


def execute_quary(qry: str, params: Union[list, tuple]=None):
    """ executes a single command with no return value """
    with engine.connect() as conn:
        if params is not None:
            try:
                conn.execute(qry, params)
            except Exception as e:
                print(e)
        else:
            try:
                conn.execute(qry)
            except Exception as e:
                print(e)


def get_rs(qry: str, params: Union[list, tuple]=None) -> Union[tuple, None]:
    with engine.connect() as conn:
        if params is not None:
            try:
                rs = conn.execute(qry).fetchall()
                print(rs)
                if len(rs) > 0:
                    return rs
                else:
                    return None
            except Exception as e:
                print(e)
        else:
            try:
                rs = conn.execute(qry).fetchall()
                print(rs)
                if len(rs) > 0:
                    return rs
                else:
                    return None
            except Exception as e:
                print(e)


def init_db():
    for qry in schema:
        execute_quary(qry)


if __name__ == '__main__':
    init_db()

