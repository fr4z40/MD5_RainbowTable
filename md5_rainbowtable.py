#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Eduardo Frazão
# 16/07/2014
from hashlib import md5
from argparse import ArgumentParser

def usage():
    print('\t./script.py PasswordsList RainbowTable')
    quit()

def writer(x,y):
    with open(y, 'a') as outp:
        outp.write(x)
        outp.close()

parser = ArgumentParser()
parser.add_argument('input', help='save the output', type=str)
parser.add_argument('-o', '--output', help='save the output', type=str)
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

for pswd in pass_list:
    pswd = (((pswd.replace('\r', '')).replace('\n', '')).replace('\t', ''))
    outp = ('%s:%s\n' % (((md5(bytes(pswd, 'utf8'))).hexdigest()), pswd))

    if args.output:
        try:
            writer(outp, args.output)
        except Exception as error:
            print('\n\n%s\n\n' % str(error))
    print(outp.strip('\n'))
