import string
my_string = input("Put your string here: ")

format_string = my_string.title()
format_string = format_string.replace(" ",'')
for punctuation in string.punctuation:
    format_string = format_string.replace(punctuation,'')
result = "#" + format_string
max_length = 140
if len(result) > max_length:
    result = result[:max_length]

print(result)