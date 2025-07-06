def triplet_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if i != j and j != k and i != k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)
    return result

print(triplet_sum([-1, 0, 1, 2, -1, -4]))
