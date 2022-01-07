#!/Users/juan/miniconda3/bin/python3

import os
from datetime import datetime

## FUNCTIONS

def display(path, root):
    print((len(path) - 2) * '---', os.path.basename(root), f'[directory]')

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def count_files(files:list)->int:
    return len([file for file in files if 'py' in file or '.ipynb' in file])

def write_readme_file(file_output:str, records:list):
    with open(file_output, 'w') as outfile:
        # loop of records
        for r in records:
            outfile.write(f'{r}\n')


## MAIN FUNCTION

def main(file_output:str):
    # initialize
    omossions_root = ['.', '.ipynb_checkpoints']
    omossions_in_path = ['.git']
    records = list()
    stab = ' '
    url_root = "https://github.com/jmquintana79/utilsDS/blob/master"

    # header
    records.append('# Tools for a Data Science projects')

    # introduction
    records.append("This repository is a compendium of notebooks and scripts to be used in my daily work for Data Science projects. I will try to use this landscape as reference:")
    # add picture
    records.append('&nbsp;&nbsp;')
    records.append("![DS Landscape](.img/DS_picture.jpg)")
    # add content title
    records.append('## Content')

    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk("."):
        # get path (splitted root)
        path = root.split(os.sep)
        # build name
        name = os.path.basename(root)
        if name == 'nlp' or name == 'ADA' or name == 'gam' or name == 'EDA' or name == 'KDE':
            s_name = name.upper()
        else:
            s_name = f"{name.replace('_', ' ').capitalize() }"
        # build counter files
        nfiles = count_files(files)
        s_nfiles = f'*[{count_files(files)}]*'
        # number of tabs
        ntabs = len(path)-2
        if ntabs >= 2:
            ntabs = 2**(ntabs - 1)
        # build url
        url = os.path.join(url_root, root[2:])
        # build name with url
        s_name_url = f'[{s_name}]({url})'
        # omit folders in path
        if len(intersection(path, omossions_in_path)) > 0:
            pass
        else:
            # omit folders
            if not os.path.basename(root) in omossions_root:
                # display
                display(path, root)
                # add sub-headers
                if ntabs == 0:
                    records.append(f'### {s_name_url}')
                elif ntabs == 1:
                    records.append(f'- {s_name_url} *[{nfiles}]*')
                else:
                    records.append(f'{ntabs*stab}- {s_name_url} {s_nfiles}')

    # foot
    s_foot = f'> Updated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    records.append(s_foot)

    ## WRITE FILE
    write_readme_file(file_output, records)




## MAIN ENV
if __name__ == '__main__':
    # output file
    file_output = 'README.md'
    # launching
    main(file_output)
    # end
    quit('done')