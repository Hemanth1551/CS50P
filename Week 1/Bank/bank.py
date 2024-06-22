input=input("Enter input:")
if input.lower().strip() == "hello":
        print("$0")
elif input[0].lower() == "h":
      if input[0:5].lower() == "hello":
            print("$0")
      else:
            print("$20")
else:
      print("$100")


