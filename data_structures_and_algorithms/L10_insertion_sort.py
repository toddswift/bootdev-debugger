def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while (j > 0) and (nums[j-1] > nums[j]):
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    return nums

if __name__ == "__main__":
    test_array = [5, 2, 8, 1, 9]
    print("Original:", test_array)
    sorted_array = insertion_sort(test_array)
    print("Sorted:", sorted_array)