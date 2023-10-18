while True:
    user_input = input("Please enter two words :")
    if user_input == "done" or not user_input:
        print("Bye!!")
        break
    words = user_input.split()
    if len(words) == 1:
        word1 = word2 = words[0]
    elif len(words) == 2:
        word1, word2 = words[0], words[1]
    else:
        print("enter one or two word")
        continue
    if word1 < word2:
        print(f'{word1} come first')
    elif word1 > word2:
        print(f'{word2} come first')
/////////////////////

user_input = input("Enter a string: ")
print("Input string =" + user_input)

index = len(user_input) - 1

while index >= 0:
    print(user_input[index])
    index -= 1
    ////////////////////////////////////////
user_input = input("please enter a string:")
upper_case = 0
lower_case = 0
numbers = 0
other_character = 0
for i in user_input:
    if i.isupper():
        upper_case +=1
    else:
        if i.islower():
            lower_case += 1
        else:
            if i.isdigit():
                numbers += 1
            else:
                other_character += 1
print(f"Upper case:{upper_case}")
print(f"Lower case:{lower_case}")
print(f"Numbers:{numbers}")
print(f"other characters:{other_character}")
//////////////
while True:
    user_input = input("Please enter a string:")
    if user_input.lower() == "done":
        print("bye!")
        break
    special_characters = [":",",","!","?","."]
    cleaning = ''.join(char for char in user_input if char not in special_characters)
    print(cleaning)
