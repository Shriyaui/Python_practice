class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1  # convert to 0-based index
        ans = []

        for i in range(n, 0, -1):
            idx = k // fact
            ans.append(nums.pop(idx))

            k %= fact

            if i > 1:
                fact //= (i - 1)

        return "".join(ans)