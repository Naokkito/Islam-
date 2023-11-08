def chop(lst):
    if len(lst) >= 2:
        del lst[0]
        del lst[-1]
def middle(lst):
    if len(lst) >= 2:
        return lst[1:-1]
    else:
        return []

my_list = [1, 2, 3, 4]

print("my list before calling chop function =>", my_list)
chop(my_list)
print("my list after calling chop function =>", my_list)
my_list = [1, 2, 3, 4]
print("\nmy list before calling middle function =>", my_list)
new_list = middle(my_list)
print("my list after calling middle function =>", my_list)
print("new list after calling middle function =>", new_list)
/////////////////////////////
file_name = "romeo.txt"
word_list = []
try:
    with open(file_name, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                if word not in word_list:
                    word_list.append(word)
    word_list.sort()
    print(word_list)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    ////////////////////////////////
sender_list = []
file_name = "mbox.txt"
line_count = 0
try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("From "):
                words = line.split()
                if len(words) > 1:
                    sender = words[1]
                    sender_list.append(sender)
    for sender in sender_list:
        print(sender)
    line_count = len(sender_list)
    print(f"Total {line_count} lines were printed")
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    //////////////////////////
numbers = []
while True:
    user_input = input("Please enter an integer (type 'done' to exit): ")
    if user_input == 'done':
        break
    try:
        number = int(user_input)
        numbers.append(number)
        average = sum(numbers) / len(numbers)
        print(f"{numbers} , average = {average:.2f}")
    except ValueError:
        print("Invalid input. Please enter an integer or 'done' to exit.")
print("Bye!!")