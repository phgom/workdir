import argparse
import sys


parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# parser.add_argument('--Test', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
parser.add_argument("-snd", help='sender email address', required=True)
parser.add_argument("-rcv", help='receiver email address', nargs='*', required=True)
parser.add_argument("-cc",  help='cc email address', nargs='*')
parser.add_argument("-path", help='attached file path', required='-file' in sys.argv)
parser.add_argument("-file", help='attached file name', required='-path' in sys.argv)
parser.add_argument("contents", help='email contents')
args = parser.parse_args()
print(args.snd)
print(args.rcv)
print(args.cc)
print(args.path)
print(args.file)