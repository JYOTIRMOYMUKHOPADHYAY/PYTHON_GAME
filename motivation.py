an_letter = "aeiou"
print("I will cheer for you @(-_-)@ ")
n = input("what is ur goal : ")
x = input("What is you name ? ")
y = int(input("Give us a rating how much u like to cheer 1 to 10: "))
decision = input("Are you depressed ? yes or no : ")
i = 0
if decision == "yes":
    while i < len(n):
        char = n[i]
        if char in an_letter:
            print("Give me an " + char + " !!! " + char)
            print("yes you can do it")
        else:
            print("Give me a " + char + " !!! " + char)
            print("yes you can do it")
        i += 1
else:
    print("congratulations you are ok")
print("ok then lets practice more !!!!!")
for s in range(y):
    print(x , "You can do it")
