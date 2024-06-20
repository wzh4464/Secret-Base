import glob
import os

###
 # File: /add_ctexart_comment.py
 # Created Date: Monday, June 17th 2024
 # Author: Zihan
 # -----
 # Last Modified: Friday, 21st June 2024 12:24:20 am
 # Modified By: the developer formerly known as Zihan at <wzh4464@gmail.com>
 # -----
 # HISTORY:
 # Date      		By   	Comments
 # ----------		------	---------------------------------------------------------
###

# Find all Markdown files recursively
md_files = glob.glob('**/*.md', recursive=True)

# Comment to be added
comment = '''---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
'''

comment_2 = '''---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
'''

# Add the comment to each file
for file in md_files:
  with open(file, 'r+') as f:
    content = f.read()
    # if already has ctexart comment, then skip
    if 'documentclass: "ctexart"' in content:
      continue
    f.seek(0, 0)
    # f.write(comment + content)
    # if the first line is '---', then remove the first line and add the comment_2
    if content.startswith('---'):
      content = content[content.find('\n') + 1:] # remove the first line
      f.write(comment_2 + content)
    else:
      f.write(comment + content)

# delete first blank lines
# for file in md_files:
#   with open(file, 'r+') as f:
#     content = f.readlines()
#     f.seek(0, 0)
#     for line in content:
#       if line.strip() != '':
#         f.write(line)
#     f.truncate()

# substitute all space in file name with '_'
# for file in md_files:
#   new_file = file.replace(' ', '_')
#   print(f'Renaming {file} to {new_file}')
#   os.rename(file, new_file)

# also for foler name
# folders = glob.glob('**/', recursive=True)
# for folder in folders:
#   new_folder = folder.replace(' ', '_')
#   print(f'Renaming {folder} to {new_folder}')
#   os.rename(folder, new_folder)
