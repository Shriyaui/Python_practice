class Solution:
    def combinationSum2(self, arr, target):
        arr.sort()
        ans = []

        def backtrack(idx, curr, target):
            if target == 0:
                ans.append(curr[:])
                return
            
            if target < 0 or idx == len(arr):
                return

            # pick
            curr.append(arr[idx])
            backtrack(idx + 1, curr, target - arr[idx])
            curr.pop()

            # skip duplicates
            while idx + 1 < len(arr) and arr[idx] == arr[idx + 1]:
                idx += 1

            # not pick
            backtrack(idx + 1, curr, target)

        backtrack(0, [], target)
        return ans
        