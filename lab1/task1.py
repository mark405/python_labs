import argparse

parser = argparse.ArgumentParser()

parser.add_argument("x")
parser.add_argument("y")
parser.add_argument("operation")

args = parser.parse_args()


def summarize(a, b):
    if not is_type_is_equal_to_int_or_float(a) or not is_type_is_equal_to_int_or_float(b):
        raise TypeError

    return float(a) + float(b)


def subtract(a, b):
    if not is_type_is_equal_to_int_or_float(a) or not is_type_is_equal_to_int_or_float(b):
        raise TypeError

    return float(a) - float(b)


def multiplicate(a, b):
    if not is_type_is_equal_to_int_or_float(a) or not is_type_is_equal_to_int_or_float(b):
        raise TypeError

    return float(a) * float(b)


def divide(a, b):
    if not is_type_is_equal_to_int_or_float(a) or not is_type_is_equal_to_int_or_float(b):
        raise TypeError
    if isinstance(a, int) and isinstance(b, int) and not b:
        raise ZeroDivisionError

    return float(a) / float(b)


def is_type_is_equal_to_int_or_float(a):
    if not float(a):
        return False
    return True


calc_dict = {
    "+": summarize,
    "-": subtract,
    "*": multiplicate,
    "/": divide,
}

result = calc_dict.get(args.operation)

if result:
    try:
        print(result(args.x, args.y))
    except ZeroDivisionError:
        print("Second argument can't be zero")
    except ValueError:
        print("Invalid type")
else:
    print("Invalid third argument")
