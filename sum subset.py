def sum_of_subsets(nums, target_sum):
    def backtrack(start, path, current_sum):
        if current_sum == target_sum:
            result.append(path[:])  # Append a copy of 'path'
            return
        if current_sum > target_sum or start == len(nums):
            return

        # Include the current element
        path.append(nums[start])
        backtrack(start + 1, path, current_sum + nums[start])
        path.pop()

        # Exclude the current element
        backtrack(start + 1, path, current_sum)

    result = []
    backtrack(0, [], 0)
    return result

# Example usage
nums = [2, 4, 6, 8]
target_sum = 8
print(sum_of_subsets(nums, target_sum))
