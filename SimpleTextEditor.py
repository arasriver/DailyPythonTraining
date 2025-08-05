import os

file_name = input("Enter the file name to open or create: ").strip().lower()
if os.path.exists(file_name):
    with open(f"{file_name}","r") as f:
        print(f.read())


text_content = ""

while True:
    text_content = input("Enter your text (type Save on a new line to save and exit): ")
    if text_content != "save":
        with open(f"{file_name}", "a") as f:
            f.write(f"{text_content}\n")
    else:
        break


print(f"{file_name} saved.")
