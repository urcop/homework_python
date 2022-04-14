import os
import sys
import tarfile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--directory', '-dir', default='/home/sirius/projects/homework_python')
parser.add_argument('--archive', '-ar', default='directory.tar.gz')
args = parser.parse_args(sys.argv[1:])


def archive(args):
    tar = tarfile.open(args.archive, 'w|gz')
    for root, dir, files in os.walk(args.directory):
        for file in files:
            tar.add(os.path.join(root, file))
    tar.close()


if __name__ == '__main__':
    archive(args)
