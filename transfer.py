#Break
print("***************break****************************")
for i in range(11):
    if i==3:
        break
    print(f"print last item processed{i}")

    emp_data=["bhargavi","Hema","chaitu","nagadevi"]
    print("bhargavi"in emp_data)

    for item in emp_data:
        if item=="bhargavi":
            print(item)
            break
        print(f"item last processed {item}")

        #Continue
        print("******************************Continue*************************")

        for a in range(10):
            if a==3:
                print(a)
                continue
            print(f"last processed{a}")
            #pass
            print("*******************pass**********************")
            for b in range(10):
                if b==4:
                    pass
                print(f"last processed b value is {b}")


    #Coding Exercise
    print("****************Coding Exercise*****************")

# Write a Python program that takes a list of numbers as input
#numbers=[25,30,45,35,10] and prints the sum of the numbers
#however,if the sum exceeds 100,stop adding numbers and print "sum exceeded 100"

print("******************sum of value exceeding 100******************")
sum=0
num1=[4,8,12,16,20,24,28,32,36,40]
for c in num1:
    sum+=c
    if sum>85:
        print("Sum exceeding 100")
        break
    print(c)
    print(f"sum value is{c}")

    ''''''
    #Write a Python script the uses a for loop to iterate through numbers from 1 to 600.
    #print only the odd numbers,skipping the even ones using the continue statement
    ''''''

    print("1 to 600 odd numbers printing started")
    for j in range(600):
        if j%2==0:
            continue
        print(j)

        ''''''

#Write a Python script that checks if a number is even or odd.if a number is even,print "Even";if odd,do nothing(use the pass statement)
    ''''''

    print("****************Even number printing")
    number=int(input("Enter the number"))
    if number % 2==0:
        print(f"Entered number {number} is even")
    else:
        pass

    ''''''
    #Write a Python script that iterates through  a list of words.If the word is "break",
    #exit the loop using the break statement.If the word is "skip",skip the rest of the code for the current StopIteration
    #using the continue statement.For any other word,print the word

    ''''''
    print("***************Combining Transfer Statemnets****************")
    input1=["Apple","Banana","Grape","ice","coke","carrot"]
    input2=["Apple","coke","Grape","carrot","Banana","ice"]

    for word in input2:
    if word=="break":
        break
    if word=="skip":
        continue
    print(word)
