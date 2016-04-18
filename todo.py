import argparse
import json
import os
import sys

import settings


def main():
	if not os.path.exists(settings.JSON_PATH):
		json_data = create_default_json_dict()
		write_json_file(json_data)

	json_data = load_json_data_from_file(settings.JSON_PATH)

	if args.add_task:
		task_to_add = join_input(args.add_task, ' ')
		task_dict = create_task(task_to_add)
		updated_json_data = add_task(task_dict, json_data)
		write_json_file(updated_json_data)
		print_task_list(updated_json_data)

	if args.delete_task:
		indexes_to_delete = parse_task_indexes(args.delete_task)
		updated_json_data = delete_task_by_index(indexes_to_delete)
		write_json_file(updated_json_data)
		print_task_list(updated_json_data)
		print args.delete_task

	if args.toggle_task:
		print args.toggle_task

def delete_task_by_index(indexes_to_delete):
	json_data = load_json_data_from_file(settings.JSON_PATH)

	for list_of_task_indexes in indexes_to_delete:
		for index, value in enumerate(list_of_task_indexes):
			list_of_task_indexes[index] = int(value) - 1

	for index in list_of_task_indexes:
		del json_data['root']['children'][index]

	return json_data

def parse_task_indexes(arguments):
	indexes = []
	for argument in arguments:
		indexes.append(argument.split('.'))
	return indexes

def join_input(argument, connector):
	"""
	Return a string from a list of values
	
	:param argument:        a list of arguments from args
	:param connector:       a string to connect with
	:returns joined_string: a string
	"""
	joined_string = connector.join(argument)
	return joined_string 

def write_json_file(json_data):
	"""
	Create a default json file with the task list data

	:calls create_default_json_dict:
	"""
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

def create_task(task_string):
	task_dict = {
		"status": "open",
		"text": "{}".format(task_string),
		"collapse": "false",
	}
	return task_dict

def add_task(task_dict, json_data):
	"""
	Add a task to the json file. 

	:param task_string: a string to be added to the json file.
	:param json_data:   a dictionary of json data 
	"""
	json_data['root']['children'].insert(0, task_dict)
	return json_data

def print_task_list(json_data):
	for index, task in enumerate(json_data['root']['children']):
		if task['status'] == 'open':
			print_string = "{} {}".format(index + 1, task['text'])
			print(print_string)

def parse_args(args):
	parser = argparse.ArgumentParser()
	parser.add_argument('-a',
						'--add_task',
						help='some help',
						nargs='*',
						type=str)
	parser.add_argument('-d', '--delete_task', nargs=1, type=str)
	parser.add_argument('-t', '--toggle_task', nargs=1, type=str)
	
	return parser.parse_args(args)

if __name__ == '__main__':
	args = parse_args(sys.argv[1:])
	main()
