# replace (README.html, README-ja.html) -> (index.html, index-ja.html)
# sed may be better but .. for windows ...

import sys
import locale
import argparse
import io

parser = argparse.ArgumentParser()
parser.add_argument('input', type=argparse.FileType('rb'),
        nargs='?',
        default=sys.stdin.buffer, help='input file')
parser.add_argument('--input-encoding', '--ienc', type=str,
        default=locale.getpreferredencoding(False),
        help='input file encoding (default: %(default)s)')
parser.add_argument('output', type=argparse.FileType('wb'),
        nargs='?',
        default=sys.stdout.buffer, help='output file')
parser.add_argument('--output-encoding', '--oenc', type=str,
        default=locale.getpreferredencoding(False),
        help='output file encoding (default: %(default)s)')

args = parser.parse_args()

text = io.TextIOWrapper(args.input, encoding=args.input_encoding).read()
text = text.replace('README.html', 'index.html').replace('README-ja.html', 'index-ja.html')
io.TextIOWrapper(args.output, encoding=args.output_encoding).write(text)
