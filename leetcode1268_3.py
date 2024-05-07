# https://leetcode.com/problems/search-suggestions-system/
#
# Beats 98.65% of users with Python3 using binary search and elimation 

class Solution:
    def __init__(self):
        self.MAX_PARTIAL_RETURN = 3

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ret = []
        for i in range(len(searchWord)):
            key = searchWord[:i+1]
            startIndex = self.binarySearch(products, key)
            partial_ret, non_prefix_indices = self.linearSearch(products, key)
            ret.append(partial_ret)
            non_prefix_index = [i for i in range(startIndex)] + non_prefix_indices
            products = self.removeNonCandidate(products, non_prefix_indices)
        return ret

    def binarySearch(self, products, search):
        low, high = 0, len(products)
        while low < high:
            mid = low + high >> 1
            if search > products[mid]:
                low = mid + 1
            else:
                high = mid
        return low

    def linearSearch(self, products, key):
        non_prefix_indices = []
        partial_ret = []
        for i, product in enumerate(products):
            if len(partial_ret) >= self.MAX_PARTIAL_RETURN:
                break
            if product.startswith(key):
                partial_ret.append(product)
            else:
                non_prefix_indices.append(i)
        return partial_ret, non_prefix_indices

    def removeNonCandidate(self, products, non_prefix_indices):
        for i in range(len(non_prefix_indices)-1, 0, -1):
            index = non_prefix_indices[i]
            del products[index]
        return products

