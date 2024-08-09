class Solution:
    def is_nice(self, window_set):
        for ch in window_set:
            if ch.lower() not in window_set or ch.upper() not in window_set:
                return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        max_len = 0
        max_substr = ""

        for start in range(n):
            window_set = set()
            for end in range(start, n):
                window_set.add(s[end])
                if self.is_nice(window_set):
                    if end - start + 1 > max_len:
                        max_len = end - start + 1
                        max_substr = s[start:end + 1]
        
        return max_substr

        
            