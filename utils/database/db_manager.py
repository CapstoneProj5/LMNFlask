# from utils.database.connection import *
from utils.database import connection as db
from typing import Union
import datetime


def get_artist_primary_key_by_sk_id(sk_id: Union[int, str]) -> Union[int, None]:
    print("sk_id in get artist")
    print(sk_id)

    qry = "SELECT id FROM lmn_artist WHERE sk_id = %s"
    rs = db.get_rs(qry, (str(sk_id),))

    print("rs in get artist id")
    print(rs)

    return rs[0][0]
    # if len(rs) > 0:
    #     return rs[0][0]
    # else:
    #     return None


def get_venue_primary_key_by_sk_id(sk_id: Union[int, str]) -> Union[int, None]:
    if isinstance(sk_id, int):
        sk_id = str(sk_id)

    qry = "SELECT id FROM lmn_venue WHERE sk_id = %s"
    rs = db.get_rs(qry, (sk_id,))

    print("rs in ")
    print(rs)

    return rs[0][0]
    # if len(rs) > 0:
    #     return rs[0][0]
    # else:
    #     return None


def get_show_primary_key_by_sk_id(sk_id: Union[int, str]) -> Union[int, None]:
    if isinstance(sk_id, int):
        sk_id = str(sk_id)

    qry = "SELECT id FROM lmn_show WHERE sk_id = %s"
    rs = db.get_rs(qry, (sk_id,))
    if rs:
        return rs[0][0]
    else:
        return None


def insert_atrist(a):
    qry = "INSERT INTO lmn_artist (name, sk_id, picture) VALUES (%s, %s, '')"
    db.execute_quary(qry, (a["name"], a["sk_id"]))


def insert_venue(v):
    qry = "INSERT INTO lmn_venue (name, city, state, sk_id, picture) VALUES (%s, %s, %s, %s, '')"
    args = (v["name"], v["city"], v["state"], v["sk_id"])
    db.execute_quary(qry, args)


"""
[{'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 62202104}, {'time': '18:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 59969129}, {'time': '21:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 64396129}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 64131184}, {'time': '19:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 61896904}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 64269434}, {'time': '17:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 64193614}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 62963944}, {'time': '18:30:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 64158809}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 62500584}, {'time': '19:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 63888404}, {'time': '21:30:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 63156324}, {'time': '18:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 61430859}, {'time': '20:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 62172114}, {'time': '19:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 61903024}, {'time': '20:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 63427379}, {'time': '18:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 64463669}, {'time': '21:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 64078224}, {'time': '21:30:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 63442389}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 63904009}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 62515939}, {'time': '19:30:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 61809429}, {'time': '21:45:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 61809434}, {'time': '09:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 64316484}, {'time': None, 'date': '2018-04-13', 'venue': 1842483, 'artist': 62171209}, {'time': '21:30:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 63451629}, {'time': '19:30:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 63939109}, {'time': '19:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 62503364}, {'time': '19:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 64047914}, {'time': None, 'date': '2018-04-14', 'venue': 1842483, 'artist': 63099489}, {'time': '20:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 61927329}, {'time': '21:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 64038779}, {'time': '20:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 62125204}, {'time': '20:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 62841579}, {'time': '19:30:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 62970889}, {'time': '19:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 62910414}, {'time': None, 'date': '2018-04-14', 'venue': 1842483, 'artist': 62258714}, {'time': '20:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 62562914}, {'time': None, 'date': '2018-04-14', 'venue': 1842483, 'artist': 62932334}, {'time': '20:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 63655544}, {'time': '21:30:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 63772659}, {'time': '19:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 63558399}, {'time': '19:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 61809439}, {'time': '21:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 61809444}, {'time': '20:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 63103719}, {'time': '21:30:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 61809479}, {'time': '19:00:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 61417154}, {'time': None, 'date': '2018-04-14', 'venue': 1842483, 'artist': 62897509}, {'time': '19:30:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 61770154}, {'time': '18:30:00', 'date': '2018-04-14', 'venue': 1842483, 'artist': 63360529}]

{'time': '18:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 59969129}

"""


def insert_show(s):

    if s["time"] is not None:
        time_arr = s["time"].split(":")
    else:
        time_arr = [0, 0, 0]

    date_arr = s["date"].split("-")

    print(time_arr)
    time = datetime.time(int(time_arr[0]), int(time_arr[1]), int(time_arr[2]))

    print(date_arr)
    date = datetime.date(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]))

    print(time)
    print(date)

    dt = datetime.datetime(int(date_arr[0]), int(date_arr[1]), int(date_arr[2]),
                           int(time_arr[0]), int(time_arr[1]), int(time_arr[2]))
    print(dt)

    print("s[\"artist\"]")
    print(s["artist"])

    artist_id = get_artist_primary_key_by_sk_id(int(s["artist"]))
    venue_id = get_venue_primary_key_by_sk_id(s["venue"])

    print(s["artist"])
    print("artist_id")
    print(artist_id)

    print("s")
    print(s)

    qry = "INSERT INTO lmn_show (show_date, artist_id, venue_id, sk_id, picture) VALUES (%s, %s, %s, %s, '')"
    args = (dt, artist_id, venue_id, s["sk_id"])

    db.execute_quary(qry, args)


if __name__ == '__main__':
    print(get_artist_primary_key_by_sk_id(1234))
    tst_artist = {'name': 'Eli Conley', 'sk_id': 3822461}
    insert_atrist(tst_artist)

    tst_venue = {'name': 'Janet Wallace Fine Arts Center, Macalester College', 'city': 'Twin Cities', 'state': 'MN', 'sk_id': 795771}
    insert_venue(tst_venue)

    tst_show = {'time': '18:00:00', 'date': '2018-04-13', 'venue': 1842483, 'artist': 59969129, "sk_id": "1234"}

    insert_show(tst_show)
