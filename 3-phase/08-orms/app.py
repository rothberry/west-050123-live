#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

sql = """
    DROP TABLE IF EXISTS pets
    DROP TABLE IF EXISTS owner
"""

CURSOR.execute(sql)


import ipdb; ipdb.set_trace()