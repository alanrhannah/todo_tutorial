import json
import os
import pytest
import settings
from todo import (join_input,
                  parse_args,
                  create_default_json_dict,
                  create_task,
                  add_task)

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

def test_add_task():
    json_data = {"info": "This path is managed by Alan!",
                   "root": {
                     "children": []
                   }
                }
    task_dict = {
        "status": "open",
        "text": "a test string",
        "collapse": "false",
    }
    expected_dict = {"info": "This path is managed by Alan!",
                   "root": {
                     "children": [{
                       "status": "open",
                       "text": "a test string",
                       "collapse": "false",}]
                   }
                }
    assert add_task(task_dict, json_data) == expected_dict

def test_write_json_file(tmpdir):
    json_path = tmpdir.mkdir("data").join(settings.JSON_FILE)

    # json_path = os.path.join(tmp_dir, settings.JSON_FILE)
    # print json_path

    expected = {"info": "This path is managed by Alan!",
                   "root": {
                     "children": []
                   }
                }

    content = create_default_json_dict()
    with open(json_path.strpath, 'w+') as json_file:
        json.dump(content, json_file)

    assert json_path.read() == json.dumps(expected)
    assert len(tmpdir.listdir()) == 1
