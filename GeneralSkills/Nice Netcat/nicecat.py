f= open("nicenetcat","r")
lines =f.readlines()
result=""
for line in lines:
	result+=chr(int(line.strip("\n")))
print(result)
