import argparse
import json
import os

import settings

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--add_task', help='some help', nargs='*', type=str)
parser.add_argument('-d', '--delete_task', nargs=1, type=str)
parser.add_argument('-t', '--toggle_task', nargs=1, type=str)

def main():
	if os.path.exists(settings.JSON_PATH):
		json_data = load_json_data_from_file(settings.JSON_PATH)
		import ipdb; ipdb.set_trace()
	else:
		create_default_json_file()

	if args.add_task:
		task_to_add = join_input(args.add_task)
		add_task(task_to_add)

	if args.delete_task:
		print args.delete_task

	if args.toggle_task:
		print args.toggle_task

def join_input(argument, connector):
	"""
	Return a string from a list of values
	
	:param argument:        a list of arguments from args
	:param connector:       a string to connect with
	:returns joined_string: a string
	"""
	joined_string = argument.join(connector)
	return joined_string 

def create_default_json_file():
	"""
	Create a default json file with the task list data

	:calls create_default_json_dict:
	"""
	json_data = create_default_json_dict()
	with open(settings.JSON_PATH, 'w+') as json_file:
		json.dump(json_data, json_file)

def create_default_json_dict():
	"""
	Create the default task list dictionary.

	:returns tasks_dict:  a dictionary of dictionaries
	"""
	tasks_dict = {"info": "This path is managed by Alan!",
				  "root": {
				  	"children": []
				  }}
	return tasks_dict

def load_json_data_from_file(file_path):
	"""
	Doc string

	:param filepath: the location of the json file to load data from
	:returns tasks_dict: a dictionary
	"""
	with open(file_path, 'r') as json_file:
		tasks_dict = json.load(json_file)

	return tasks_dict

def add_task(task_string):
	"""
	Add a task to the json file. 

	:param task_string:  a string to be added to the json file.
	"""
	pass


if __name__ == '__main__':
	args = parser.parse_args()
	main()
