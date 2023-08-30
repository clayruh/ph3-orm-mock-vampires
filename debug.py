#!/usr/bin/env python3

import ipdb
from lib import CONN, CURSOR
from lib.classes.vampire import Vampire
from lib.classes.castle import Castle

if __name__ == '__main__':
    # testing data
    castle1 = Castle.query_all()[0]
    castle2 = Castle.query_all()[1]

    ipdb.set_trace()
