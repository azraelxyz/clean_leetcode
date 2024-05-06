# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ret = []
        MAX_PARTIAL_RETURN = 3
        for i in range(len(searchWord)):
            partial_ret = []
            key = searchWord[:i+1]
            for product in products:
                if len(partial_ret) >= MAX_PARTIAL_RETURN:
                    break
                if product.startswith(key):
                    partial_ret.append(product)
            ret.append(partial_ret)
        return ret

