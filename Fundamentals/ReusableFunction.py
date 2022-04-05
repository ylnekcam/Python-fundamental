def emoji_converter(message):
    words = message.split(' ')# words will define with space
    emojis = {
        ":)": "smile",
        ":(": "sad" 
    }
    output = ""
    for word in words:
        output += emojis.get(word,word) + " "
    return output


message = input ("> ")# to indicate user to input data
print (emoji_converter(message))