import argparse

import settings

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add_task', help='some help', nargs='*', type=str)
parser.add_argument('-d', '--delete_task', nargs=1, type=str)
parser.add_argument('-t', '--toggle_task', nargs=1, type=str)

def main():
	if args.add_task:
		print args.add_task

	if args.delete_task:
		print args.delete_task

	if args.toggle_task:
		print args.toggle_task

if __name__ == '__main__':
	args = parser.parse_args()
	main()
