def max_subarray_sum_fixed(arr, k):
    max_sum = float("-inf")  # Floating-point value representing negative infinity
    current_sum = 0

    for i in range(k):
        current_sum += arr[i]
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i]
        current_sum -= arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum


def length_of_longest_substring(s: str):
    char_index_map = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        right_char = s[right]
        # If the character is already in the window, move 'left' past the last occurrence
        if right_char in char_index_map and char_index_map[right_char] >= left:
            left = char_index_map[right_char] + 1

        # Update character's index
        char_index_map[right_char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def test_max_subarray_sum_fixed():
    """Tests for max_subarray_sum_fixed function."""
    print("=== Testing max_subarray_sum_fixed ===")
    
    # Test case 1: Basic positive numbers
    print("\n1. Basic case: [2, 1, 5, 1, 3, 2], k=3")
    arr1 = [2, 1, 5, 1, 3, 2]
    k1 = 3
    result1 = max_subarray_sum_fixed(arr1, k1)
    print(f"Input: {arr1}, k={k1}")
    print(f"Expected: 9 (subarray [5, 1, 3])")
    print(f"Actual: {result1}")
    
    # Test case 2: Array with negative numbers
    print("\n2. With negatives: [2, -1, 2, -3, 1], k=2")
    arr2 = [2, -1, 2, -3, 1]
    k2 = 2
    result2 = max_subarray_sum_fixed(arr2, k2)
    print(f"Input: {arr2}, k={k2}")
    print(f"Expected: 1 (subarray [2, -1])")
    print(f"Actual: {result2}")
    
    # Test case 3: All negative numbers
    print("\n3. All negatives: [-1, -2, -3, -4], k=2")
    arr3 = [-1, -2, -3, -4]
    k3 = 2
    result3 = max_subarray_sum_fixed(arr3, k3)
    print(f"Input: {arr3}, k={k3}")
    print(f"Expected: -3 (subarray [-1, -2])")
    print(f"Actual: {result3}")
    
    # Test case 4: Edge case - k equals array length
    print("\n4. k equals length: [1, 2, 3], k=3")
    arr4 = [1, 2, 3]
    k4 = 3
    result4 = max_subarray_sum_fixed(arr4, k4)
    print(f"Input: {arr4}, k={k4}")
    print(f"Expected: 6 (entire array)")
    print(f"Actual: {result4}")


def test_length_of_longest_substring():
    """Tests for length_of_longest_substring function."""
    print("\n\n=== Testing length_of_longest_substring ===")
    
    # Test case 1: Basic case with repeating characters
    print("\n1. Basic case: 'abcabcbb'")
    s1 = "abcabcbb"
    result1 = length_of_longest_substring(s1)
    print(f"Input: '{s1}'")
    print(f"Expected: 3 (substring 'abc')")
    print(f"Actual: {result1}")
    
    # Test case 2: All same characters
    print("\n2. All same: 'bbbbbb'")
    s2 = "bbbbb"
    result2 = length_of_longest_substring(s2)
    print(f"Input: '{s2}'")
    print(f"Expected: 1 (any single 'b')")
    print(f"Actual: {result2}")
    
    # Test case 3: No repeating characters
    print("\n3. No repeats: 'abcdefg'")
    s3 = "abcdefg"
    result3 = length_of_longest_substring(s3)
    print(f"Input: '{s3}'")
    print(f"Expected: 7 (entire string)")
    print(f"Actual: {result3}")
    
    # Test case 4: Empty string
    print("\n4. Empty string: ''")
    s4 = ""
    result4 = length_of_longest_substring(s4)
    print(f"Input: '{s4}'")
    print(f"Expected: 0")
    print(f"Actual: {result4}")
    
    # Test case 5: Complex case
    print("\n5. Complex case: 'pwwkew'")
    s5 = "pwwkew"
    result5 = length_of_longest_substring(s5)
    print(f"Input: '{s5}'")
    print(f"Expected: 3 (substring 'wke')")
    print(f"Actual: {result5}")
    
    # Test case 6: Single character
    print("\n6. Single char: 'a'")
    s6 = "a"
    result6 = length_of_longest_substring(s6)
    print(f"Input: '{s6}'")
    print(f"Expected: 1")
    print(f"Actual: {result6}")


def debug_max_subarray_sum_fixed(arr, k):
    """
    Debug version of max_subarray_sum_fixed with step-by-step output.
    Set breakpoints here to watch the algorithm in action.
    """
    print(f"\n=== DEBUG: max_subarray_sum_fixed({arr}, {k}) ===")
    
    if len(arr) < k:
        print("Error: k is larger than array length")
        return None
    
    max_sum = float("-inf")
    current_sum = 0
    
    # Calculate sum of first window
    print(f"Step 1: Calculate initial window sum (first {k} elements)")
    for i in range(k):
        current_sum += arr[i]
        print(f"  Adding arr[{i}] = {arr[i]}, current_sum = {current_sum}")
    
    max_sum = current_sum
    print(f"Initial max_sum = {max_sum}")
    
    # Slide the window
    print(f"\nStep 2: Slide window through remaining elements")
    for i in range(k, len(arr)):
        old_left = arr[i - k]
        new_right = arr[i]
        
        print(f"\nWindow [{i-k+1}:{i+1}]:")
        print(f"  Remove arr[{i-k}] = {old_left}")
        print(f"  Add arr[{i}] = {new_right}")
        
        current_sum += new_right
        current_sum -= old_left
        
        print(f"  New current_sum = {current_sum}")
        print(f"  Current window: {arr[i-k+1:i+1]}")
        
        if current_sum > max_sum:
            max_sum = current_sum
            print(f"  NEW MAXIMUM! max_sum = {max_sum}")
        else:
            print(f"  max_sum remains {max_sum}")
    
    print(f"\nFinal result: {max_sum}")
    return max_sum


def debug_length_of_longest_substring(s):
    """
    Debug version of length_of_longest_substring with step-by-step output.
    Set breakpoints here to watch the algorithm in action.
    """
    print(f"\n=== DEBUG: length_of_longest_substring('{s}') ===")
    
    char_index_map = {}
    max_length = 0
    left = 0
    
    print(f"Initial state: left=0, max_length=0, char_index_map={{}}")
    
    for right in range(len(s)):
        right_char = s[right]
        print(f"\nStep {right + 1}: Processing s[{right}] = '{right_char}'")
        
        # Check if character is already in current window
        if right_char in char_index_map and char_index_map[right_char] >= left:
            old_left = left
            left = char_index_map[right_char] + 1
            print(f"  Character '{right_char}' found at index {char_index_map[right_char]}")
            print(f"  Moving left pointer from {old_left} to {left}")
        else:
            print(f"  Character '{right_char}' not in current window")
        
        # Update character's index
        char_index_map[right_char] = right
        print(f"  Updated char_index_map: {char_index_map}")
        
        # Calculate current window length
        current_length = right - left + 1
        current_window = s[left:right+1]
        print(f"  Current window: '{current_window}' (length = {current_length})")
        
        if current_length > max_length:
            max_length = current_length
            print(f"  NEW MAXIMUM LENGTH! max_length = {max_length}")
        else:
            print(f"  max_length remains {max_length}")
        
        print(f"  State: left={left}, right={right}, max_length={max_length}")
    
    print(f"\nFinal result: {max_length}")
    return max_length


if __name__ == "__main__":
    # Run all tests
    test_max_subarray_sum_fixed()
    test_length_of_longest_substring()
    
    print("\n" + "="*60)
    print("DEBUG EXAMPLES - Set breakpoints in these functions!")
    print("="*60)
    
    # Run debug examples
    debug_max_subarray_sum_fixed([2, 1, 5, 1, 3, 2], 3)
    debug_length_of_longest_substring("abcabcbb")
