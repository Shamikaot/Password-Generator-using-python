#COPYRIGHT
#Password Generator
#written by Sepehr Mohseni




#importing libraries
import string
import random

#main
def GeneratePassword (passLength):
    password = string.ascii_letters + string.digits + "!@#$%^&*()_+=-./?><|\}{[]"
    #generating characters, numbers and letters for password
    passwordList = []
    #password list is for putting all the selected password units into a string and show them to user
    for passChar in range(passLength):
        passRandom = random.choice(password)
        passwordList.append(passRandom)

    finalOutput = "".join(passwordList)
    return finalOutput
