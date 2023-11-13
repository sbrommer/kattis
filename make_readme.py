from autokattis import Kattis
from os import listdir
from os.path import isfile

# read from kattis
kt = Kattis('suus', '3b^S!De?$W-e+*7w')

problems = kt.problems(show_partial=False)
df_problems = problems.to_df()[['name', 'difficulty', 'link']]

link_prefix = 'https://open.kattis.com/problems/'
link_names = set(link[len(link_prefix):] for link in df_problems['link'])
df_problems['link name'] = df_problems['link'].str[len(link_prefix):]

# get points distribution plot
kt.plot_problems(filepath='plot.png', show_partial=False)

# read from files
ignore = set(['.DS_Store', '.gitattributes', '.gitignore',
              'README.md', 'in.txt', 'ak.py', 'plot.png'])
file_names = set(f for f in listdir('.')
                 if isfile(f) and f not in ignore and f[-2:] != '.h')
files = {f.split('.')[0]: f.split('.')[1] for f in file_names}
base_names = set(files.keys())

if len(file_names) != len(base_names):
    print(f'{len(file_names)} files found (that are not ignored), but {len(base_names)} unique file base names found.')

elif (link_names - base_names) or (base_names - link_names):
    print(f'kattis found {len(link_names)} solved problems, but there are {len(base_names)} files found.')
    print(f'found in kattis but not in directory: {link_names - base_names}')
    print(f'found in directory but not in kattis: {base_names - link_names}')

# get file info into kattis data frame
df_problems['extension'] = df_problems['link name'].map(files)

# create READMIE
f = open('README.md', 'w')

print(f'[points distribution plot](https://github.com/sbrommer/kattis/blob/main/plot.png)')

print('|Problem|Difficulty|Solution|', file=f)
print('|---|---|---|', file=f)


problems = df_problems.T.to_dict().values()
problems = sorted(problems, key=lambda problem: problem['name'])

for p in problems:
    name = p['name']
    link = p['link']
    difficulty = p['difficulty']
    link_name = p['link name']
    extension = p['extension']
    python_link = f'https://github.com/sbrommer/kattis/blob/main/{link_name}.{extension}'
    print(f'|[{name}]({link})|{difficulty}|[Python3]({python_link})|', file=f)
f.close()
