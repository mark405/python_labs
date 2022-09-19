import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-W", dest="capacity", type=int)
parser.add_argument("-w", dest="bars", type=int, nargs="*")
parser.add_argument("-n", dest="number", type=int)

args = parser.parse_args()


def calculate_max_weight_of_gold(capacity, list_of_bars, number_of_bars):
    rucksack = [[0 for x in range(capacity + 1)] for x in range(number_of_bars + 1)]
    for i in range(number_of_bars + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                rucksack[i][w] = 0
            elif list_of_bars[i - 1] <= w:
                rucksack[i][w] = max(rucksack[i - 1][w], rucksack[i - 1][w - list_of_bars[i - 1]] + list_of_bars[i - 1])
            else:
                rucksack[i][w] = rucksack[i - 1][w]
    return rucksack


k_list = calculate_max_weight_of_gold(args.capacity, args.bars, args.number)

print(k_list[args.number][args.capacity])
