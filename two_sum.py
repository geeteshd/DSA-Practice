def two_sum(nums,target):
    emp_dict = {}

    for i, num in enumerate(nums):
        result = target - num
        if result in emp_dict:
            return [emp_dict[result], i]
        else:
            emp_dict[num] = i


#Test Cases
print(two_sum([2,7,6,5,4],9))
print(two_sum([2,4,3,7],5))