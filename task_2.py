num = int(input("please enter your age for authentication: "))
if num%2==0 and num!=0:
    print("Is positive and has right to vote: ",num)
elif num%2!=0 and num !=0:
    print("Is negitive number and has right to vote: ", num)
else:
    print("enter valid number: ")
