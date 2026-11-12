# LeetCode 242. Valid Anagram (Easy) - Arrays & Hashing
# https://leetcode.com/problems/valid-anagram/
# Approach: count letters of both strings in hash maps and compare.
# Time: O(n), Space: O(1) (at most 26 letters)

class Solution(object):
    def isAnagram(self, s, t):
        countS, countT = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1

        return countS == countT
