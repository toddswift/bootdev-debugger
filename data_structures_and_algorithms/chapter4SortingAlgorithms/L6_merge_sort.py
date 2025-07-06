def split_list(lst):
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]
    
def merge_sort(nums):
    if len(nums) < 2:
        return nums
  
    first_half, second_half = split_list(nums)

    sorted_left_side = merge_sort(first_half)
    sorted_right_side = merge_sort(second_half)

    return merge(sorted_left_side, sorted_right_side)
   
def merge(first, second):
    final_list = [] 
    i = 0 
    j = 0 

    while i < len(first) and j < len(second):
            if first[i] <= second[j]:
                final_list.append(first[i])
                i += 1
            else:
                final_list.append(second[j])
                j += 1

    while i < len(first):
        final_list.append(first[i])
        i += 1
    
    while j < len(second):
        final_list.append(second[j])
        j += 1
        
    return final_list


import time

run_cases = [([3, 2, 1], [1, 2, 3]), ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5])]

submit_cases = run_cases + [
    ([], []),
    ([7], [7]),
    ([4, -7, 1, 0, 5], [-7, 0, 1, 4, 5]),
    ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting: {expected_output}")
    start = time.time()
    result = merge_sort(input1)
    end = time.time()
    timeout = 1.00
    if (end - start) < timeout:
        print(f"test completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        print(f"Actual: {result}")
        print("Fail")
        return False
    else:
        print(f"test took longer than {timeout * 1000} milliseconds!")
        print(f"Actual: {result}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
