import argparse
import operator
import math

parser = argparse.ArgumentParser()

parser.add_argument("operation")
parser.add_argument("x")
parser.add_argument("y")

args = parser.parse_args()

calc_dict = {
    "add": [operator.add, 2],
    "sub": [operator.sub, 2],
    "mult": [operator.mul, 2],
    "truediv": [operator.truediv, 2],
    "floordiv": [operator.floordiv, 2],
    "mod": [operator.mod, 2],
    "pow": [operator.pow, 2],
    "sin": [math.sin, 1],
    "cos": [math.cos, 1],
    "log": [math.log, 2],
    "sqrt": [math.sqrt, 1],
    "exp": [math.exp, 1],
}

result = calc_dict.get(args.operation)

if result:
    try:

        if result[1] == 1:
            print(result[0](args.x + args.y))
        elif result[1] == 2:
            print(result[0](args.x, args.y))
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print("ZeroDivisionError")
else:
    print("Invalid argument")
