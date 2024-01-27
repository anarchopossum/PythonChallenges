# # You are given a list X, which is a sequence composed exclusively of 0s and 1s.
# The task is to compute the length of the longest subsequence within this array that 
# alternates between Os and 1s.

# A subsequence is a sequence that can be derived from the original array by deleting 
# some or none of the elements, ensuring the order of the remaining elements is maintained.
# An alternating subsequence is one where no two adjacent elements are the same. 
# In simpler terms, the elements of the subsequence alternate between 0 and 1.

# Examples:
# 1. Input X = [0, 1, 0, 1, 0]
# output: 5
# 2. Input X = [0]
# output: 1

def alt_sub(input: list):
   cur_counter = 1
   top_counter = 0
   if len(input) == 1:
       return 1
   else:
        for value in range(1, len(input)):
            if input[value] is not input[value-1]:
                cur_counter += 1
                print(f"{input[value]} compared to {input[value-1]} | {cur_counter}")
            else:
                top_counter = cur_counter
                cur_counter = 1
                print(top_counter)
            if cur_counter > top_counter:
                top_counter = cur_counter
        return top_counter


def test_alt_sub_multi():
    assert alt_sub([0,1,0,1,0]) == 5
 
def test_alt_sub_sing():
    assert alt_sub([0]) == 1

print(alt_sub([0,1,0,1,0]))
