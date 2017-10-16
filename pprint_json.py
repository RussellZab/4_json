import json
import pprint as pp


def load_data(filepath):
    return open(filepath,'r')


def pretty_print_json(data):
    pass


if __name__ == '__main__':
    f = load_data('test.json')
    pp.pprint(f.read())