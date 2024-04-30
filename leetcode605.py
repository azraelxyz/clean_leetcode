# https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i, x in enumerate(flowerbed):
            if x == 0:
                if i == len(flowerbed)-1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1

        return count >= n

