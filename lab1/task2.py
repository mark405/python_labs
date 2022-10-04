import argparse
import operator
import math

parser = argparse.ArgumentParser()

parser.add_argument("operation")
parser.add_argument("x")
parser.add_argument("y")

args = parser.parse_args()

operation = args.operation


def func(action):
    return getattr(math, action, None) or getattr(operator, action, None) or None


result = func(operation)

try:
    if not result:
        print("Function doesnt exists")
    else:
        print(result(float(args.x), float(args.y)))
except TypeError:
    print(result(float(args.x) + float(args.y)))
except ValueError:
    print("ValueError")
