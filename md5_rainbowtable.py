#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Eduardo Frazão  ( http://github.com/fr4z40 )
# 16/07/2014

from hashlib import md5
from argparse import ArgumentParser

def writer(x,y):
    with open(y, 'a') as outp:
        outp.write(x)
        outp.close()

parser = ArgumentParser()
parser.add_argument('input', help='example: md5_rainbowtable.py /path/wordlist.ext', type=str)
parser.add_argument('-o', '--output', help='save in a file. --output=/path/path/path/file.ext', type=str)
args = parser.parse_args()

try:
    with open(args.input, 'r') as file_in:
        pass_list = file_in.readlines()
        file_in.close()
except Exception as erro:
    print('\n\n%s\n' % erro)
    quit()

pass_list = list(set(pass_list))
pass_list.sort()


print('|%sHash%s|  String\n' % ((' '*15),(' '*15)))

for pswd in pass_list:
    pswd = (((pswd.replace('\r', '')).replace('\n', '')).replace('\t', ''))
    outp = ('%s:%s\n' % (((md5(bytes(pswd, 'utf8'))).hexdigest()), pswd))
    out = ((outp.strip('\n')).split(':'))

    if args.output:
        try:
            writer(outp, args.output)
        except Exception as error:
            print('\n\n%s\n\n' % str(error))

    print('| %s |  %s' % (out[0], out[1]))
    
