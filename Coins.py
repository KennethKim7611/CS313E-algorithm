import sys

'''
Input:  coins is a dictionary representing how many of each type of coin you have (value -> amount)
        amount is the target amount you want to make change for
Output: True if it possible to make exact change using the coins provided, False otherwise
'''

def canMakeChange(coins, amount):
    lst =[]
    for i in coins:
        for j in range(coins[i]):
            lst.append(i)
    newlst = combination(lst)
    for i in range(len(newlst)):
        sum = 0
        for j in range(len(newlst[i])):
            sum+=newlst[i][j]
        if sum==amount:
            return True
    return False


def combination(lst):
    if lst:
        result = combination(lst[:-1])
        return result + [c + [lst[-1]] for c in result]
    else:
      return [[]]


def main():
    f = sys.stdin
    num_coins, amount = [int(x.strip()) for x in f.readline().split()]
    coins = {}
    for _ in range(num_coins):
        coin_val, coin_amt = [int(x.strip()) for x in f.readline().split()]
        coins[coin_val] = coin_amt
    print(canMakeChange(coins, amount))

if __name__ == "__main__":
    main()