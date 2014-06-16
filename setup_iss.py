import sys
import os
import sysconfig
import string
import argparse

from suzu import version

setup_root = os.path.abspath(os.path.dirname(__file__))

python_version = sysconfig.get_python_version()
python_platform = sysconfig.get_platform()
suzu_version = version.__version__

build_directory = os.path.join(setup_root, 'build',
        'exe.{}-{}'.format(python_platform, python_version))

dist_directory = os.path.join(setup_root, 'dist')

# architecture
architecture = ''
if python_platform == 'win-amd64':
    architecture = 'x64'
    architecture_install = 'x64'
else:
    architecture = 'x86'
    architecture_install = ''

parser = argparse.ArgumentParser()
parser.add_argument('infile', type=argparse.FileType('rt'), nargs='?',
        default=sys.stdin, help='input template file (default: stdin)')
parser.add_argument('outfile', type=argparse.FileType('wt'), nargs='?',
        default=sys.stdout, help='output file (default: stdout)')

args = parser.parse_args()

args.outfile.write(
        string.Template(args.infile.read()).substitute(
            setup_root=setup_root,
            python_version=python_version,
            python_platform=python_platform,
            suzu_version=suzu_version,
            build_directory=build_directory,
            dist_directory=dist_directory,
            architecture=architecture,
            architecture_install=architecture_install))
