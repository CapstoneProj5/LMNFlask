from sqlalchemy.engine import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
from LMNFlask import app
from typing import Union

# from utils.database.schema import schema
schema = ["SELECT id FROM lmn_artist WHERE sk_id = %s"]

DB_URL = app.config["DB_CONN"]
engine = create_engine(DB_URL, echo=True)


def execute_quary(qry: str, params: Union[list, tuple]=None) -> None:
    """ executes a single command with no return value """
    with engine.connect() as conn:
        if params is not None:
            try:
                conn.execute(qry, params)
            except SQLAlchemyError as e:
                print(e)
        else:
            try:
                conn.execute(qry)
            except SQLAlchemyError as e:
                print(e)


def get_rs(qry: str, params: Union[list, tuple]=None) -> Union[tuple, None]:
    """ executes a single command and returns a data set """
    with engine.connect() as conn:
        if params is not None:
            try:
                # conn.
                rs = conn.execute(qry, params).fetchall()
                print("rs in db.get_rs()")
                print(rs)
                if len(rs) > 0:
                    return rs
                else:
                    return None
            except SQLAlchemyError as e:
                print(e)
        else:
            try:
                rs = conn.execute(qry).fetchall()
                print(rs)
                if len(rs) > 0:
                    return rs
                else:
                    return None
            except SQLAlchemyError as e:
                print(e)


def init_db():
    # for qry in schema:
    #     print(get_rs(qry))
    #     test_rs = get_rs(qry)
    #     print(test_rs)
        # print(test_rs[1])
    test_rs = get_rs(schema[0], 59969129)
    print(test_rs)


if __name__ == '__main__':
    init_db()
