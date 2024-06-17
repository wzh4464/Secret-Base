import glob

###
 # File: /add_ctexart_comment.py
 # Created Date: Monday, June 17th 2024
 # Author: Zihan
 # -----
 # Last Modified: Monday, 17th June 2024 4:31:23 pm
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

# Add the comment to each file
for file in md_files:
  with open(file, 'r+') as f:
    content = f.read()
    f.seek(0, 0)
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