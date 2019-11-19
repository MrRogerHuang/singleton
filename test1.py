#!/usr/bin/python3
from Logger1 import *
from Logger2 import *

def Log_2_1():
  Logger2.log('Hello\n')

def Log_2_2():
  Logger2.log('World\n')

def Log_1_1():
  l1 = Logger1()
  l1.log('Hello\n')

def Log_1_2():
  l1 = Logger1()
  l1.log('World\n')

Log_2_1()
Log_2_2()
Log_1_1()
Log_1_2()
