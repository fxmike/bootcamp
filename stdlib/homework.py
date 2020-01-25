import sys
import pathlib
import argparse

def print_dir(path, prefix=''):
    items_count = len(list(path.iterdir()))
    for n, x in enumerate(path.iterdir()):
        if n == items_count - 1:
            marker = "  └ "
            next_marker = "   "
        else:
            marker  = "  ├ "
            next_marker = "  │"

        if x.is_dir():
            print(prefix + marker + '\033[1m' + f'  ├ [{x.name}]' + '\033[0m')
            print_dir(x, prefix + next_marker)
        else:
            if x.suffix == '.py':
                print(prefix + marker + '\033[94m' + x.name + '\033[0m')
            else:
                print(prefix + marker + x.name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()