import json
from pathlib import Path

import pytest

from gendiff import generate_diff

TEST_DATA = Path(__file__).parent / 'test_data'


def get_path(name):
    return TEST_DATA / name


def read_text(name):
    return get_path(name).read_text(encoding='utf-8').rstrip('\n')


@pytest.mark.parametrize('file1, file2, format_name, expected', [
    ('flat1.json', 'flat2.json', 'stylish', 'expected_flat_stylish.txt'),
    ('flat1.yml', 'flat2.yml', 'stylish', 'expected_flat_stylish.txt'),
    ('file1.json', 'file2.json', 'stylish', 'expected_stylish.txt'),
    ('file1.yml', 'file2.yaml', 'stylish', 'expected_stylish.txt'),
    ('file1.json', 'file2.yaml', 'plain', 'expected_plain.txt'),
    ('file1.yml', 'file2.json', 'plain', 'expected_plain.txt'),
])
def test_generate_diff(file1, file2, format_name, expected):
    diff = generate_diff(get_path(file1), get_path(file2), format_name)
    assert diff == read_text(expected)


def test_generate_diff_default_format():
    diff = generate_diff(get_path('file1.json'), get_path('file2.json'))
    assert diff == read_text('expected_stylish.txt')


@pytest.mark.parametrize('file1, file2', [
    ('file1.json', 'file2.json'),
    ('file1.yml', 'file2.yaml'),
])
def test_generate_diff_json(file1, file2):
    diff = generate_diff(get_path(file1), get_path(file2), 'json')
    assert json.loads(diff) == json.loads(read_text('expected_json.json'))
