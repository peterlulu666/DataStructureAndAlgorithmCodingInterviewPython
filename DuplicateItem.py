# Find the duplicate item
# arrayOne = ['a', 'b', 'c']
# arrayTwo = ['x', 'u', 'c']
# Return true
# arrayOne = ['a', 'b', 'c']
# arrayTwo = ['x', 'y', 'z']
# Return false

# Compare 'a' with 'x'
# Compare 'a' with 'u'
# Compare 'a' with 'c'
# Compare 'b' with 'x'
# Compare 'b' with 'u'
# Compare 'b' with 'c'
# Compare 'c' with 'x'
# Compare 'c' with 'u'
# Compare 'c' with 'c'
# Time complexity is O(n^2)

def duplicate_item():
    is_duplicate = False
    array_one = ['a', 'b', 'c']
    array_two = ['x', 'u', 'c']
    for array_one_item in array_one:
        for array_two_item in array_two:
            if array_one_item == array_two_item:
                is_duplicate = True
    if is_duplicate:
        print("Found item")
    else:
        print("There is no duplicated item.")


# Create a hashMap
# 'a' 'b' 'c' are the key
# true and false are value
# Check hashMap['x'] is true or false
# Check hashMap['u'] is true or false
# Check hashMap['c'] is true or false
# Time complexity is O(n)

def duplicate_element():
    letter_dict = dict()
    is_duplicate = False
    array_one = ['a', 'b', 'c']
    array_two = ['x', 'y', 'z']
    for array_one_item in array_one:
        if array_one_item not in letter_dict:
            letter_dict[array_one_item] = True
    for array_two_item in array_two:
        # Check key in dictionary
        if array_two_item in letter_dict.keys():
            is_duplicate = True
    if is_duplicate:
        print("Found duplicate")
    else:
        print("There is no duplicated item.")


def main():
    duplicate_item()
    duplicate_element()


main()
