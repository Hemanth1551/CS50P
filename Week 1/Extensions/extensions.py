input=input("Enter input type: ")
list=[".gif",".jpg",".jpeg",".png",".pdf",".txt",".zip",".bin"]
x = input.replace("."," .").lower() # replace the string with the " . "
y = x.split() #split the string
y = y[-1]     #get the last element in list
if y in list:
    match y:
        case ".gif":
            print("image/gif")
        case ".jpg" | ".jpeg":
            print("image/jpeg")
        case ".png":
            print("image/png")
        case ".txt":
            print("text/plain")
        case ".pdf" | ".zip":
            print("application/"+y.replace(".",""))
        case ".bin" | "":
            print("application/octet-stream")
else:
    print("application/octet-stream")
