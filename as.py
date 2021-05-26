intro = input("Enter Your Introduction: ")
print(intro)
wordCount = 1
characterCount = 0
for i in intro:
    characterCount+=1
    if i == " ":
        wordCount+=1
print("number Of characters ",characterCount)
print("number Of word ",wordCount)
