# -*- coding: utf-8 -*-
import os

def rename_file(file_name, title, suffix):
	title = title.rstrip().replace('#', '').replace(' ', '')
	title += suffix
	print (title)
	os.rename(file_name, title)

def read_file(file_name):
	with open(file_name) as f:
		for i, line in enumerate(f):
			if i == 0 and line != '':
				rename_file(file_name, line, '.md')

def rename_path_files(path):
	for root, dirs, filenames in os.walk(indir):
	    for f in filenames:
	        if isEnglish(f) and '.md' in f:
	            read_file(f)


def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True

indir = '/Users/Will/GitHub/The-Poem-of-Will/'
rename_path_files(indir)
