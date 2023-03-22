memo = {}

def fibonacci(num):
    answer = None
    # Write your code here
    if num in memo:
        answer = memo[num]
    elif num == 0 or num == 1:
        answer = num
    else:
        answer = fibonacci(num - 1) + fibonacci(num - 2)
        memo[num] = answer
    return answer

# Test your code with calls here:
print(fibonacci(20))
print(fibonacci(200))


# while left_pointer < right_pointer
#   if the height at left_pointer <= the height at right_pointer
#      - update the left_bound to be the greater value between the current left_bound and the height at left_pointer
#      - increment total_water to be the difference between left_bound and the height at left_pointer
#      - move left_pointer forward by one
#   else
#      - update the right_bound to be the greater value between the current right_bound and the height at right_pointer
#      - increment total_water to be the difference between right_bound and the height at right_pointer
#      - move right_pointer back by one 

# return total_water