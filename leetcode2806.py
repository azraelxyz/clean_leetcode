# https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        balance = 100
        roundedAmount = self.rounding(purchaseAmount)
        return balance - roundedAmount

    def rounding(self, amount):
        remainder = amount % 10
        quotient = amount // 10
        ret = quotient * 10
        if remainder >= 5:
            ret += 10
        return ret

