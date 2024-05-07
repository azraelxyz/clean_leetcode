# https://leetcode.com/problems/search-suggestions-system/

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        ret = []
        MAX_PARTIAL_RETURN = 3
        for i in range(len(searchWord)):
            partial_ret = []
            non_prefix_indices = []
            key = searchWord[:i+1]
            for i, product in enumerate(products):
                if len(partial_ret) >= MAX_PARTIAL_RETURN:
                    break
                if product.startswith(key):
                    partial_ret.append(product)
                else:
                    non_prefix_indices.append(i)
            for i in range(len(non_prefix_indices)-1, 0, -1):
                index = non_prefix_indices[i]
                del products[index]
            ret.append(partial_ret)
        return ret

