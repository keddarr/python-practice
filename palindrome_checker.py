n = input("What do you want to check if it is a Palindrome : ")
clean_text = n.lower().replace(" ", "")
reverse_text = clean_text[: : -1]
if clean_text == reverse_text :
    print("It is a Palindrome!")
else :
    print("Not a Palindrome")

