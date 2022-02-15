# Ask users for a number

Get_number = int(input("Choose a number? "))
# Multiply the number by 5
times_five = Get_number * 5

answer = "{} times five is equal to " \
         "{}".format(Get_number, times_five)

# Output the result
print(answer)


# Get name until an exit code is entered...

name = ""
while name != "xxx":
    who = input("who are you? ")
    print(who)

    print ()
    
print("We are done!")