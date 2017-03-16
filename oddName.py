name = input("Enter your name: ")

count = 1

if len(name) < 1:
    print("Error, name cannot be blank")
else:
    for char in name:
        if count % 2 == 1:
            print(char)
        count += 1
    else:
        count += 1