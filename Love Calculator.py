print("Love calculator")
name1 = str(input("Male name: "))
name2 = str(input("Female name: "))
combined = name1 + name2
combined_lower = combined.lower()
t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")
true = (t+r+u+e)
l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")
love = (l+o+v+e)
score = str(true) + str(love)
if (int(score) <= 10) or (int(score)>= 90):
    print("The love Score is",score, " you both go like coke and mentos")
elif (int(score) > 10) or (int(score) < 90):
    print("Your Score is",score," you are alright together")
else:
    print("Your Scores is",score)
