email = input("Enter your email address: ").strip()

# slice out user name 

username = email[:email.index('@')]

# slice out domain name

domain = email[email.index('@') + 1:]

# format output consisting of UN and DN

result = "Your username = {}\nYour domain = {}".format(username, domain)

# print result

print(result)
