import json

import yaml

PARSERS = {
    'json': json.loads,
    'yaml': yaml.safe_load,
}


def parse(content, data_format):
    return PARSERS[data_format](content)
