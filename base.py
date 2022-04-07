# Import Necessary Library
import os
import argparse
import sys
import math
import time
import datetime

# Contains general function


def length(arr: list) -> int:
    count = 0

    for i in arr:
        count += 1
    return count


def addObj(arr: list, param) -> list:
    return arr + [param]
