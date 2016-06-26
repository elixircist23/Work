import argparse
from dbutil import DBUtil

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--insert', help = 'insert new row')
parser.add_argument('-d', '--delete', help = 'delete a certain row')
parser.add_argument('-q', '--query', help = 'run a sql query')
parser.add_argument('-u', '--update', help = 'update a certain row')
parser.add_argument('-name')
parser.add_argument('age')
parser.add_argument('club')

args = parser.parse_args()

print(args)
