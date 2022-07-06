#!/usr/bin/python3
"""
add arguments of python list
"""

import sys


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

ls = []
try:
    ls = load_json("add_item.json")
except Exception:
    ls = []
ls += sys.argv[1:]
save_json(ls, "add_item.json")
