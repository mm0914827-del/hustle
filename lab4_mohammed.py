# mohammed [ lab 4 ] intro to python

# ticket 1
ages = [17.11, 25, 13, 9]

for age in ages:
    if age >= 13:
        print(f'{age} - Access granted')
    else:
        print(f'{age} - Too young')
# prediction: ages : 17,25 and 13 will print "Access granted" and age 9 will print "Too young"
# explain: the for loop iterates through each age in the ages list. The if statement checks if the age is greater than or equal to 13. If it is, it prints "Access granted"; otherwise, it prints "Too young".

# ticket 2
keep_checking = "yes"

while keep_checking == "yes":
    age = int(input("Enter your age: "))
    if age >= 13:
        print(f'{age} - Access granted')
    else:
        print(f'{age} - Too young')
    keep_checking = input("Do you want to check another age? (yes/no): ")
# prediction: the loop will continue to prompt the user for ages until they enter "no" when asked if they want to check another age.
# explain: the while loop continues to run as long as keep_checking is "yes". Inside the loop, it prompts...

# ticket 3
while True:
    user_input = input("enter your age or type 'stop' :")
    if user_input.lower() == "stop":
        break
    age = int(user_input)
    if age >= 13:
        print(f'{age} - Access granted')
    else:
        print(f'{age} - Too young')
# prediction: the loop can continue to prompt the user for ages until they type "stop".
# explain: the while loop runs indefinitely until the user types "stop". Inside the loop, it prompts the user for their age, checks if it's greater than or equal to 13, and prints the appropriate message. The loop breaks when the user inputs "stop".

# ticket 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False
# using the function to check the original ages list
ages = [17, 11, 25, 13, 9]
for age in ages:
    if can_access(age):
        print(f'{age} - Access granted')
    else:
        print(f'{age} - Too young')
# prediction: ages 17,25 and 13 will print "Access granted" and age 11 and 9 will print "Too young"
# explain: the function can_access takes an age as input and returns True if the age is greater than or equal to 13, and False otherwise. The for loop iterates through the ages list, calling the can_access function for each age and printing the appropriate message based on the returned value.

# ticket 5
def signup_report(age_list):
    print("-- streampass signup report --")
    approved = 0
    # enumerate starts at index 0, so we add 1 to get signup #1,2, etc.
    for index, age in enumerate(age_list):
        if can_access(age):
            print(f'Signup #{index + 1}: {age} - Access granted')
            approved += 1
        else:
            print(f'Signup #{index + 1}: {age} - Too young')
    print(f"\napproved: {approved} out of {len(age_list)}")
# test list provided in the lab instructions
