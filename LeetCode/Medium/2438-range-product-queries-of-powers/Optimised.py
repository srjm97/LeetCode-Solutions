from functools import cache

MOD = 10**9 + 7
class Solution:

    @cache
    def modinv(self, x):
        return pow(x, MOD-2, MOD)

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [1 << i for i in range(n.bit_length()) if (n >> i) & 1]
        l = len(powers)
        prefix_product = [powers[0]] * l
        for i in range(1, l):
            prefix_product[i] = (prefix_product[i-1] * powers[i]) % MOD

        answers = []
        for left, right in queries:
            result = prefix_product[right]
            if left > 0:
                result = (result * self.modinv(prefix_product[left-1])) % MOD
            answers.append(result)
        return answers
