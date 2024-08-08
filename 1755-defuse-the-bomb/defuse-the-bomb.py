class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        if k > 0:
            window_sum = sum(code[1 : k + 1])
            for i in range(n):
                result[i] = window_sum
                window_sum -= code[(i + 1) % n]
                window_sum += code[(i + k + 1) % n]

        if k < 0:
            k = -k
            window_sum = sum(code[-k:])  # Initial window sum
            for i in range(n):
                result[i] = window_sum
                window_sum -= code[(i - k) % n]
                window_sum += code[i % n]
    
        return result
        