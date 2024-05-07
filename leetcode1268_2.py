# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def __init__(self):
        self.MAX_PARTIAL_RETURN = 3

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ret = []
        for i in range(len(searchWord)):
            key = searchWord[:i+1]
            partial_ret, non_prefix_indices = self.linearSearch(products, key)
            ret.append(partial_ret)
            products = self.removeNonCandidate(products, non_prefix_indices)
        return ret

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

