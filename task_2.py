num = int(input("please enter your age for authentication: "))
if num%2==0 and num!=0 and num >=18:
    print("Is positive and has right to vote: ",num)
elif num%2!=0 and num !=0 and num>=18:
    print("Is negitive number and has right to vote: ", num)
else:
    print("Not a valid age: ")
