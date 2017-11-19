# -*- coding: utf-8 -*-
import os
import fileinput

def loop_files(path):
	for root, dirs, filenames in os.walk(path):
		for file_name in filenames:
			if ".md" in file_name:
				file_root = root + '/' + file_name
				change_hash(file_root)
                add_br_at_endline(file_name)
		print('done')

def change_hash(file_name):
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)

    for line in lines:
      if len(line) > 2:
        if line[1] != '#' :
          f.writelines(line.replace('#', '##'))
        elif line[2] == '#':
          f.writelines(line.replace('###', '##'))
        else:
          f.writelines(line)
      else:
        f.writelines(line)
    f.truncate()

def add_br_at_endline(file_name):
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
      if '#' in line:
        f.writelines(line)
      elif '<br>' in line:
        f.writelines(line)
      elif len(line) == 1:
        f.writelines(line)
      else:
        f.writelines(line.replace('\n', '<br>\n'))

def change_summary(file_name):
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)

    for line in lines:
      if '[' not in line:
        f.writelines(line)
      else:
        square_end = line.index(']')
        title = line[3:square_end]
        new_line = '- [' + title + '](' + title + '.md)\n'
        f.writelines(new_line)
    f.truncate()

path = '/Users/willbeethoven/GitBook/Poetry'
loop_files(path)
chang_summary('SUMMARY.md')
