# -*- coding: utf-8 -*-
import os

def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

indir = '/Users/Will/GitHub/The-Poem-of-Will/'
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        if isEnglish(f) and '.md' in f:
            print(f)
