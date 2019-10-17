#!/usr/bin/python3
""" Module that finds a string in the heap of a running
process and replaces it
"""
import sys


if __name__ == "__main__":
    if len(sys.argv) is not 4:
        sys.stdout.write("Usage: read_write_heap.py pid search_string")
        sys.stdout.write(" replace_string\n")
        sys.exit(1)
