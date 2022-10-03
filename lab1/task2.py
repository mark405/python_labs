import argparse
import operator
import math

parser = argparse.ArgumentParser()

parser.add_argument("operation")
parser.add_argument("x")
parser.add_argument("y")

args = parser.parse_args()

operation = args.operation

response = getattr(math, operation, "not")
try:
    if response == "not":
        response_two = getattr(operator, operation)
        print(response_two(float(args.x), float(args.y)))
    else:
        print(response(float(args.x) + float(args.y)))
except ValueError:
    print("ValueError")
except AttributeError:
    print("AttributeError")
except TypeError:
    print("TypeError")
