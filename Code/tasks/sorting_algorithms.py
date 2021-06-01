# Reference: https://stackabuse.com/sorting-algorithms-in-python



def bubble_sort(nums):
  print(nums)
  # We set swapped to True so the loop looks runs at least once
  swapped = True
  while swapped:
    swapped = False
    for i in range(len(nums) - 1): # [0,1,2,3]
      if nums[i] > nums[i + 1]:
        # Swap the elements
        temp = nums[i]
        nums[i] = nums[i + 1]
        nums[i + 1] = temp
        print(nums)
        # Set the flag to True so we'll loop again
        swapped = True




def selection_sort(nums):
  # This value of i corresponds to how many values were sorted
  for i in range(len(nums)):
    print(nums)
    # We assume that the first item of the unsorted segment is the smallest
    lowest_value_index = i
    # This loop iterates over the unsorted items
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[lowest_value_index]:
        lowest_value_index = j
    # Swap values of the lowest unsorted element with the first unsorted
    # element
    temp = nums[i]
    nums[i] = nums[lowest_value_index]
    nums[lowest_value_index] = temp


print("\nbubble_sort:")
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print("Final:", random_list_of_nums)


print("\nselection_sort:")
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print("Final:", random_list_of_nums)
