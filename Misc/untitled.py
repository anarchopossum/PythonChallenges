def calculate_time(start, end):
    """
    Function to calculate the time taken to move from one index to another.
    """
    print(f"{end}-{start} = {end-start}")
    return abs(end - start)  # Calculate the absolute difference between the start and end indices.

def time_to_type(digits, num):
    """
    Function to calculate the total time required to type a number with one finger.
    """
    total_time = 0  # Initialize the total time accumulator.
    current_index = 0  # Initialize the current index as 0.
    
    for digit in num:  # Iterate through each digit in the input number.
        target_index = digits.index(digit)  # Find the index of the current digit in the digits string.
        print(f"current Index: {current_index}\ttarget: {target_index}\ttotal time: {total_time}")
        total_time += calculate_time(current_index, target_index)  # Calculate the time taken to move to the index of the current digit and add it to the total time.
        current_index = target_index  # Update the current index to the index of the current digit.
        print(f"{'#' * 20 }\ncurrent Index: {current_index}\ttarget: {target_index}\ttotal time: {total_time}")
    
    return total_time  # Return the total time required.

# Example usage:
digits = "0123456789"
num = "210"
print(time_to_type(digits, num))  # Output: 4
print('=' * 30)
digits = "139820"
print(time_to_type(digits,num))

print('=' * 30)
print('=' * 30)

def time_to_typez(digits, num):
    total_time = 0
    current_index = 0
    for i in num:
        # grabs the next index number via index()
        next_digit_index = digits.index(i)
        # next_digit_index = digits.index(num[i + 1])
        #compares current_index - next_digit_index
        total_time += abs(current_index - next_digit_index)
        print(f"{total_time} = {current_index} - {next_digit_index}\ti: {i}")
        # makes the current_index the next_digit_index we used to update for
        # the next itteration
        current_index = next_digit_index
    return total_time

# Example usage:
digits = "0123456789"
num = "210"
print(time_to_typez(digits, num))  # Output: 4
