# https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        balance = 100
        roundedAmount = self.rounding(purchaseAmount)
        return balance - roundedAmount

    def rounding(self, amount):
        remaining = amount % 10
        ret = (amount // 10) * 10
        if remaining >= 5:
            ret += 10
        return ret
