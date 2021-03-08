# https://leetcode.com/problems/valid-parentheses/

class Solution:
    open_bracket = ["(", "[", "{"]
    close_bracket = [")", "]", "}"]

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.open_bracket:
                stack.append(char)
            if char in self.close_bracket:
                top_of_stack = stack.pop() if stack else "E"
                if self._bracket_match(top_of_stack, char) is False:
                    return False
        return not stack

    def _bracket_match(self, open_bracket, close_bracket):
        if open_bracket == "(":
            return close_bracket == ")"
        elif open_bracket == "[":
            return close_bracket == "]"
        elif open_bracket == "{":
            return close_bracket == "}"
        else:
            return False

