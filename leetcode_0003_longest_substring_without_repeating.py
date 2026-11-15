# LeetCode 3. Longest Substring Without Repeating Characters (Medium)
# Pattern: Sliding Window + Hash Set
# Time: O(n)  |  Space: O(k), k = distinct characters


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        l = best = 0
        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            best = max(best, r - l + 1)
        return best
