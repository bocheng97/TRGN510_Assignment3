#!/usr/bin/python
import sys
import re
file =open ('/home/boc/TRGN510_Assignment3/phonenumber.txt')
for line in file:
    area_codes = re.findall("\(.*?\)",line)
    print(area_codes)
file.close()
