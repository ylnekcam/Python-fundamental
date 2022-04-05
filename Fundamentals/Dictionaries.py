#key value pairs
#define varialbe not allowed duplication

customer = {
    "name":"John Smith",
    "age": 29,
    "is_verified":True
}

#acessing the value
print(customer.get("name"))
#if the value is none can set the value
print(customer.get("Birthdate","Jan 1 1990"))
#updating data
customer["name"]="Jack Smith"
print(customer.get("name"))


#sample
phone = input("Phone: ")
digits_mapping = {
    "1":"one ",
    "2":"two ",
    "3":"three "
}
output =""
for num in phone:
    output += digits_mapping.get(num,"? ")

print(output)

#using split

message = input ("> ")# to indicate user to input data
words = message.split(' ')# words will define with space
emojis = {
    ":)": "smile",
    ":(": "sad" 
}
output = ""
for word in words:
    output += emojis.get(word,word) + " "
print (output)
