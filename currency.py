class Currency:
    def __init__(self, denominations):
        self.denominations = denominations

    # number of ways to make change for amount
    def num_ways(self, amount):
        coins = self.denominations
        dp = [0] * (amount + 1)
        dp[0] = 1
        for d in coins:
          for i in range(1, len(dp)):
              if i - d >= 0:
                dp[i] += dp[i - d]
        return dp[-1] % (10 ** 9 + 7)

    # minumum number of coins required to make change for amount
    def min_change(self, amount):
        self.amount = amount
        print(self.denominations)
        coins = self.denominations
        
        '''def bin_sea(self.denominations, self.amount):'''
        n = 0
        low = 0
        
        if amount == 0 :
          return 0
        if min(coins) > amount:
          return -1
        dp = [-1 for i in range(0, amount + 1)]
        for i in coins:
          if i > len(dp) - 1:
              continue
          dp[i] = 1
          for j in range(i + 1, amount + 1):
              if dp[j - i] == -1:
                continue
              elif dp[j] == -1:
                dp[j] = dp[j - i] + 1
              else:
                dp[j] = min(dp[j], dp[j - i] + 1)
          #print(dp)
        return dp[amount]
