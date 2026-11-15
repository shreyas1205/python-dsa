class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        l = best = 0
        for r, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
