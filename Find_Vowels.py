string = input("Enter your sentence : ")

vowels = 0
consonants = 0
string.lower()

for i in string:
    if(i == 'a' or i == 'e' or i == 'i' or i =='o' or i =='u'):
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print("Total number of Vowels in the sentence = ", vowels)
print("Total number od consonants in the sentence = ", consonants)
