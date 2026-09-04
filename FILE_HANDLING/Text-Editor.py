while True:
     print("Welcome to the text editor")
     print("1. Read file")
     print("2. Write file")
     print("3. append in file")
     print("Exit ")

     Your_choice = int(input("Enter your choice"))

     if Your_choice == 1:
          with open("f1.txt", "r") as f:
               content = f.read()
               print(content)
     elif Your_choice == 2:
          text = input("THE TEXT YOU WANT TO ADD")
          with open("f1.txt", "w") as f:
               f.write(text)   
          print("File written successfully.")

     elif Your_choice == 3:
             text = input("Enter the text to add: ")
    
             with open("file.txt", "a") as f:
              f.write("\n" + text)

              print("Text added successfully.")

     elif Your_choice == 4:
        print("Exiting Text Editor...")
        break

     else:
        print("Invalid choice!")     

     