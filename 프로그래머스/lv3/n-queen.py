res = 0


def solution(n):
    def dfs(nums, index):
        global res
        if index == len(nums):
            res += 1
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if valid(nums, index):  # pruning
                dfs(nums, index + 1)

    # check whether nth queen can be placed in that column
    def valid(nums, n):
        for i in range(n):
            if abs(nums[i] - nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

    dfs([-1] * n, 0)

    return res
