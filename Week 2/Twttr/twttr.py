checked_list = ['a','e','i','o','u']
input_text = input("Input:")
for i in input_text:
    c = i  # store uppercase letter
    i = i.lower() # change uppercase to lowercase
    if i in checked_list:
        input_text  = input_text.replace(c,"")
print(input_text)
