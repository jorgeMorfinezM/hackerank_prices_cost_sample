#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculate_amount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calculateAmount' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

os.environ['OUTPUT_PATH'] = "/root/PycharmProjects/minimum_prices_costs/output.txt"


def calculate_amount(prices):
    # Write your code here

    minimun_loss = max(prices)

    print("1st minimun_loss: ", minimun_loss)

    n = len(prices)

    print("1st n value len(prices): ", n)

    i = 0

    # for i in range(1, n):
    #    if (prices[i] - prices[i-1]) < minimun_loss:
    #        if prices[i] < prices[i-1]:
    #            minimun_loss += prices[i] - prices[i-1]
    #        minimun_loss += i
    #    i += 1
    # return minimun_loss

    costs_list = [None] * n
    discount_list = [None] * n
    prices_other = []
    discount = []

    for i in range(0, n):
        if i == 0:
            minimun_loss += prices[i]
            discount_list[i] = 0
            costs_list[i] = prices[i]
            prices_other.append(prices[i])

        elif i == 1:
            prices_other.append(prices[i])
            discount_list[i] = prices[i-1]
            costs_list[i] = prices[i + 1] - discount_list[i]
            # minimun_loss += costs_list[i]
        elif i < n and (i != 1 and i != 0):
            prices_other.append(prices[i])
            discount.append(prices[i-2])
            print("descuento_temporal: ", discount)
            discount_list[i] = min(discount)
            costs_list[i] = prices_other[-1] - discount_list[i]
            # minimun_loss += costs_list[i]
        elif i == n-1:
            prices_other.append(prices[i])
            discount.append(prices[i])
            discount.append(prices_other[i-1])
            print("       descuento_temporal: ", discount)
            discount_list[i] = min(discount)
            costs_list[i] = prices_other[-1] - discount_list[i]
            # minimun_loss += costs_list[i]

        print("       i=={}, prices[i]: {}"
              "       prices_other[i]: {}"
              "       discount_list[i]: {}, "
              "       costs_list[i]: {}, "
              "       minumum_loss: {},".format(i,
                                                prices[i],
                                                prices_other[i],
                                                discount_list[i],
                                                costs_list[i],
                                                minimun_loss))

        minimun_loss += (discount_list[i] - costs_list[i])

        # print("2nd minimun_loss: ", minimun_loss)

    return abs(minimun_loss)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    result = calculate_amount(prices)

    print("Result is: ", result)

    fptr.write(str(result) + '\n')

    fptr.close()


