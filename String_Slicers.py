# here you will learn how to slice strings in python
# Project of Email Slicer

word = "abasdfbibhusipunasdfdsfefdivnorhvgdeeksha"

print(word[0])
print(word[4])

# Format = word[start:end:step]

print(word[6:16:1]) # output bibhusipun

print(word[0:10:2]) # with a step of 2

print(word[6:]) # from a postition to end

print(word[6::2]) # from a postition to end with a step

print(word[:16]) # from starting till a position

print(word[::-1]) # Reverse the whole string in just one line of code

print(word[-2]) # printing from last using - sign

print(word.index("bibhusipun")) # using index() fucntion can find the postition of string

print(word[word.index("bibhu"):word.index("deeksha")]) # print from a string to a string

print(word[word.index("deeksha"):]) # you want to go from a string to end

# now lets do a project of Email Slicer
# ========================================

# get user email address

email = input("What is your email address?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1 :]

# format message

output = "Your username is {} and your domain name is {}".format(user, domain)

# display output message 

print(output)


