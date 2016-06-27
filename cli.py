import argparse
from dbutil import DBUtil

parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', help = 'full sql path')
parser.add_argument('-i', '--insert', help = 'insert new row. usage: -i -name NAME -age AGE -club CLUB', action = 'store_true')
parser.add_argument('-d', '--delete', help = 'delete a certain row. usage: -d -column COLUMN -value VALUE', action = 'store_true')
parser.add_argument('-q', '--query', help = 'run a sql query. usage: -q -columnList ONE TWO', action = 'store_true')
parser.add_argument('-u', '--update', help = 'update a certain row. usage: -u -setColumn SET -setValue SET -whereColumn WHERE -whereValue WHERE', action = 'store_true')

parser.add_argument('-setColumn', help = 'used in update')
parser.add_argument('-setValue', help = 'used in update')
parser.add_argument('-whereColumn', help = 'used in update')
parser.add_argument('-whereValue', help = 'used in update')

parser.add_argument('-column', help = 'used in delete arg')
parser.add_argument('-value', help = 'used in delete arg')

parser.add_argument('-columnList', help = 'used in query arg (use wildcard in quotes)', nargs = '*');

parser.add_argument('-name', help = 'used in insert arg')
parser.add_argument('-age', type = int, help = 'used in insert arg')
parser.add_argument('-club', help = 'used in insert arg')

args = parser.parse_args()

if args.path:
	p = args.path
	db = DBUtil(p)

if args.insert:
	db.insert(args.name, args.age, args.club)

if args.delete:
	db.delete(args.column, args.value)

if args.query:
	print(args.columnList)
	for i in db.query(args.columnList):
		print(i)

if args.update:
	db.update(args.setColumn, args.setValue, args.whereColumn, args.whereValue)
