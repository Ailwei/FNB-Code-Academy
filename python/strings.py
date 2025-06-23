# strings

message = " Hello World "
message1 ="bob's world"
message2 = """ hello bob's
world
""" 

print(message)
print(message1)
print(message2)

#advanced concepts - strings

print(message[0])
print(message[1])


#string lenth
print(len(message))


# to remove trailing whitw space
print(message.strip())

#convert charatcter to lowercase
print(message.lower())

#split strings
message_a= "Hello, World"
print(message_a.split(','))

#replace 
print(message_a.replace(',', ''))
