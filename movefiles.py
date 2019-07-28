import os
from shutil import move

filetypes = ['pdf', 'epub', 'mobi']

p = (os.getcwd())

def make_dirs():

    for dir in filetypes:
      try:
          os.mkdir(os.path.join(p, '_' + dir))
      except:
        print("except " + dir)
        pass

def move_files():

    for filetype in filetypes:
        for path, subdirs, files in os.walk(p):
            for f in files:
                dest = str(p + '_' + filetype + '/' + f)
                if f.endswith('.' + filetype):
                    print(f)
                    try:
                        move(str(path + '/' + f), dest)
                    except:
                        pass


def main():
    make_dirs()
    move_files()

if __name__ == '__main__':
    main()
