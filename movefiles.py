import os
import pathlib

OLD_DIR = 'files'
filetypes = ['pdf', 'epub', 'mobi']

p = pathlib.Path(os.getcwd())

def make_dirs():

    for dir in NEW_DIRS:
      try:
        os.mkdir(p, dir)
      catch:
        pass

def move_files():

    for filetype in filetypes:
        for f in p.glob('**/*.' + filetype):
            new_name = '{}_{}'.format(f.parent.name, f.name)
            f.rename(os.path.join('_' + filetype, new_name))


def main():
    make_dirs()
    move_files()

if __name__ == '__main__':
    main()
