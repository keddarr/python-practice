st = input("Enter a sentence to check number of words : ")
words = st.split()
print(f"The number of words in {st} is {len(words)}.")
maxi = max(words)
mini = min(words)
print(f"The largest word in the sentence is : {maxi}.")
print(f"The smallest word in the sentence is : {mini}.")
    
