import argparse
import logging

from importlib import import_module

### INIT
parser = argparse.ArgumentParser()
parser.add_argument('-d', default=1, type=int, help='which day of advent')
parser.add_argument('-p', default=1, type=int, help='which part of problem')
parser.add_argument('-v', default=False, action='store_true', help='verbose')
args = parser.parse_args()

# set debug level
level = (logging.INFO, logging.DEBUG)[args.v]
logging.basicConfig(format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s", datefmt='%m-%d %H:%M', level=level)

### CLASSES
class dotDict(dict):
    def __init__(self, *args, **kwargs):
        super(dotDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

### MAIN
if __name__ == "__main__":
    try:
        d, p = (f'Day{args.d}', f'Part{args.p}')
        module = import_module(d)
        res = getattr(module, p)()

        # Display results
        print(f'{d}, {p}: {res}')

    except Exception as e:
        print(f'An error occured:\n{e}')
