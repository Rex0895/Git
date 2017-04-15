# !/usr/bin/python
BOARD = "board"
BCM = "bcm"
OUT = "out"
IN = "in"
PUD_DOWN = "pud_down"

def input(num):
    # print("input ", num % 2)
    return num % 2

def output(pin, value):
    print(pin, ":", value)

def setmode(mode):
    print(mode)

# def setup(pin,value):
#   print(pin, ":", value, "pull_none")

def setup(pin, value, pull_up_down="pull_none"):
    print(pin, ":", value, " ", pull_up_down)

def cleanup():
    print("clean-up")

# End