# LeetCode 20: Valid Parentheses (Stack)

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs={'}':'{',')':'(',']':'['}
        pile=[]
        for c in s:
            if c in pairs:
                if not pile:
                    return False
                top=pile.pop()
                if top != pairs[c]:
                    return False
            else:
                pile.append(c)
        return len(pile)==0
