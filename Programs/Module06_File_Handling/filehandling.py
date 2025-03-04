import os
from time import sleep

def createfile():
    """
        create a new file
    :return: None
    """

    file = open("sample1.txt", "w")
    # file = open(
    #     "C:/Users/gdevid/OneDrive - athenahealth/Backup/Devid/Training/PythonTutorial/Module04_Control_Flow/sample1.txt",
    #     "w"
    # )
    file.write("This is first line.\n")
    file.write("This is second line.\n")
    file.write("This is third line.\n")
    content = """This is forth line.
This is fifth line.\n"""
    file.write(content)
    file.close()

    file2 = open("sample2.txt", "w")
    file2.write("File to rename & delete.")
    file2.close()

def readfile():
    # file = open("sample1.txt", "r")
    # content = file.read()
    # file.close()
    # return content

    with open("sample1.txt", "r") as file:
        return file.read() # Reads all the content inside a file

def appendfile():
    # Appends content to existing file
    with open("sample1.txt", "a") as file:
        file.write("This is sixth line.")

    # Newer file is created and content is written
    with open("sample3.txt", "a") as file:
        file.write("Newer file is created and content is written.")

def readoperations():
    with open("sample1.txt", "r") as file:
        print(file.read(10)) # Reads first 10 characters in a file
        print(file.tell())
        print(file.read(10)) # Reads next 10 characters in a file

    # Reading line by line
    with open("sample1.txt", "r") as file: # file object is iterable
        for line in file:
            print(line, end="")

    # To read file as a list
    with open("sample1.txt", "r") as file: # file object is iterable
        lines = file.readlines()
        print(lines)

def renamefile(oldfilename, newfilename):
    os.rename(oldfilename, newfilename)

def removefile(filename):
    os.remove(filename)

if __name__ == "__main__":
    print("****** Create a new file ******")
    createfile()
    print("****** Read an existing file ******")
    print(readfile())
    print("****** Append a text to existing file ******")
    appendfile()
    print("****** Read operations ******")
    readoperations()
    print("****** Renaming a file ******")
    sleep(10)
    renamefile("sample2.txt", "renamedfile.txt")
    print("****** Deleting a file ******")
    sleep(10)
    removefile("renamedfile.txt")
