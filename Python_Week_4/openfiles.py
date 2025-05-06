# Open the file in read mode
try:
    with open('example.txt', 'r') as file:
        content = file.read()

    # Print the content of the file
    print(content)

except FileNotFoundError:
    print("The file was not found.")
