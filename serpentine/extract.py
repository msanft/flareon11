import argparse

# Infer base of integer literals
def auto_int(x):
    return int(x, 0)

parser = argparse.ArgumentParser( prog='extract', description='Extracts data out of files to other streams')
parser.add_argument('input', type=argparse.FileType('rb'), help='Input file to read data from')
parser.add_argument('output', type=argparse.FileType('wb'), help='Output file to write data to')
parser.add_argument("--offset", type=auto_int, help='Offset to start reading from')
parser.add_argument("--length", type=auto_int, help='Number of bytes to read')

args = parser.parse_args()

if args.offset is None:
    args.offset = 0

if args.length is None:
    args.length = -1

args.input.seek(args.offset)
data = args.input.read(args.length)

if data:
    args.output.write(data)
