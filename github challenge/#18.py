# Question:
# A website requires the users to input username and password to register. Write a program
# to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according
# to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
q = input("Username: ")

pswrd = input("""Password criteria:
    1. At least 1 letter between [a-z]
    2. At least 1 letter between [A-Z]
    3. At least 1 number between [0-9]
    4. At least 1 character from [$#@]
    5. Minimum length of transaction password: 6
    6. Maximum length of transaction password: 12
    
    Please provide password: """)

lst = pswrd.split(",")
first_crit = []
for word in lst:
    for let in word:
        if let.isdigit() and let.isupper() and let.islower() and let == "$" or let == "#" or let == "@":
            first_crit.append(word)

for fst_crt_word in first_crit:
    if len(fst_crt_word) >= 6 and len(fst_crt_word) <= 12:
        print(fst_crt_word)



#DONE!!@#!#@ WOW, duma



