# import pytest
from todo import join_input, parse_args, create_default_json_dict, create_task

def test_parse_args_add_task():
	args = parse_args(['-a', 'this', 'is', 'a', 'test', 'string'])
	assert args.add_task == ['this', 'is', 'a', 'test', 'string']

def test_parse_args_delete_task():
	args = parse_args(['-d', '1.0'])
	assert args.delete_task == ['1.0']

def test_parse_args_toggle_task():
	args = parse_args(['-t', '2.0'])
	assert args.toggle_task == ['2.0']

def test_join_input():
	argument = ['this', 'is', 'a', 'test']
	connector = ' '
	assert join_input(argument, connector) == 'this is a test'

def test_create_default_json_dict():
	expected_dict = {"info": "This path is managed by Alan!",
				  	   "root": {
				  	     "children": []}}
	assert create_default_json_dict() == expected_dict

def test_create_task():
	expected_dict = {
		"status": "open",
		"text": "a test string",
		"collapse": "false",
	}
	assert create_task("a test string") == expected_dict