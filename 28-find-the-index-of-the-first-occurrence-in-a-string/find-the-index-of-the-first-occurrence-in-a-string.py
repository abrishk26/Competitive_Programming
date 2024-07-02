class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0

        while len(haystack[i:len(needle) + i]) >= len(needle):
            if haystack[i: len(needle) + i] == needle:
                return i
            else:
                i += 1

        return -1
        