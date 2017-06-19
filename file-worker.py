# -*- coding: utf-8 -*-
import os

def loop_files(path):
	for root, dirs, filenames in os.walk(path):
		for file_name in filenames:
			if ".md" in file_name:
				rename_file(file_name)

def rename_title(file_name, index, title, suffix):
	if index == 0 and title != '':
		title = title.rstrip().replace('#', '').replace(' ', '')
		title += suffix
		return title

def rename_file(file_name):
	with open(file_name) as f:
		for index, line in enumerate(f):
			title = rename_title(file_name, index, line, '.md')
		os.rename(file_name, title)

def remove_empty_lines(file_name):
  """Overwrite the file, removing empty lines and lines that contain only whitespace."""
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    f.writelines(line for line in lines if line.strip())
    f.truncate()

def remove_dash(file_name):
  with open(file_name, 'r+') as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
      f.writelines(line.replace('---', ''))
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

def change_readme(file_name):
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

def create_directory(indir):
  for year in range(2010,2018):
    year_dir = indir + str(year)
    os.makedirs(year_dir)
    os.makedirs(year_dir + "/古诗")
    os.makedirs(year_dir + "/现代诗")

def isEnglish(s):
  try:
    s.encode('ascii')
  except UnicodeEncodeError:
    return False
  else:
    return True

indir = '/Users/Will/Poetry/'
loop_files(indir)
