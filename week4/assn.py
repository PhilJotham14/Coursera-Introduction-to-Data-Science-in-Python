from openpyxl import workbook
from stdiomask import getpass
import hashlib
import os
import tkinter as tk
import pandas as pd
# from openpyxl import *
from tkinter.messagebox import showinfo
import csv
opexcel = open("user.txt", "a")
excel = ('user.csv', 'a')
students = csv.writer(excel)
students.writerow(['Name', 'Average', 'PerAvg',
                  'FinalTest', 'AvgTest', 'Equal'])


def clear(): return os.system('cls')


def main():
    clear()
    print("MAIN MENU")
    print("---------")
    print()
    print("1 - Register")
    print("2 - Login")
    print()
    while True:
        print()
        userChoice = input("Choose An Option: ")
        if userChoice in ['1', '2']:
            break
    if userChoice == '1':
        Register()
    else:
        Login()


def Register():
    clear()
    print("REGISTER")
    print("--------")
    print()
    while True:
        userName = input("Enter Your Name: ").title()
        if userName != '':
            break
    userName = sanitizeName(userName)
    if userAlreadyExist(userName):
        displayUserAlreadyExistMessage()
    else:
        while True:
            userPassword = getpass("Enter Your Password: ")
            if userPassword != '':
                break
        while True:
            confirmPassword = getpass("Confirm Your Password: ")
            if confirmPassword == userPassword:
                break
            else:
                print("Passwords Don't Match")
                print()
        if userAlreadyExist(userName, userPassword):
            while True:
                print()
                error = input(
                    "You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
                if error == 't':
                    Register()
                    break
                elif error == 'l':
                    Login()
                    break
        addUserInfo([userName, hash_password(userPassword)])

        print()
        print("Registered!")


def Login():
    clear()
    print("LOGIN")
    print("-----")
    print()
    usersInfo = {}
    with open('userInfo.txt', 'r') as file:
        for line in file:
            line = line.split()
            usersInfo.update({line[0]: line[1]})

    while True:
        userName = input("Enter Your Name: ").title()
        userName = sanitizeName(userName)
        if userName not in usersInfo:
            print("You Are Not Registered")
            print()
        else:
            break
    while True:
        userPassword = getpass("Enter Your Password: ")
        if not check_password_hash(userPassword, usersInfo[userName]):
            print("Incorrect Password")
            print()
        else:
            break
    print()
    print("Logged In!")


def addUserInfo(userInfo: list):
    with open('userInfo.txt', 'a') as file:
        for info in userInfo:
            file.write(info)
            file.write(' ')
        file.write('\n')


def userAlreadyExist(userName, userPassword=None):
    if userPassword == None:
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName:
                    return True
        return False
    else:
        userPassword = hash_password(userPassword)
        usersInfo = {}
        with open('userInfo.txt', 'r') as file:
            for line in file:
                line = line.split()
                if line[0] == userName and line[1] == userPassword:
                    usersInfo.update({line[0]: line[1]})
        if usersInfo == {}:
            return False
        return usersInfo[userName] == userPassword


def displayUserAlreadyExistMessage():
    while True:
        print()
        error = input(
            "You Are Already Registered.\n\nPress (T) To Try Again:\nPress (L) To Login: ").lower()
        if error == 't':
            Register()
            break
        elif error == 'l':
            Login()
            break


def sanitizeName(userName):
    userName = userName.split()
    userName = '-'.join(userName)
    return userName


def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_password_hash(password, hash):
    return hash_password(password) == hash


main()

# / ---------------------------------------
partyanimals = {}

print("""
Student Test Results
-----------------------
4: Add Participant

""")
option = int(input("Enter an option: "))

while option != 0:
    if option == 4:
        partier = input("Enter name of Student: ")
        test1 = int(input("Enter the marks in the first test: "))
        test2 = int(input("Enter the marks in second test: "))
        coursework = int(input("Enter the marks in third test: "))

        if partier in partyanimals:
            print("Participant Already Added")

        else:
            # partyanimals[partier] = gift, gender, phonenumber, dateOfBirth
            if (test1 > test2):
                if (test2 > coursework):
                    total = test1 + test2
                else:
                    total = test1 + test2
            elif (test1 > coursework):
                total = test1 + test2
            else:
                total = test2 + coursework
                Avg = total / 2
                # with open('userInfo.txt', 'a') as file:
                #     for Avg in file:
                #         Avg = Avg.split()
                print("The Average of the Best two test marks is: ", Avg)

                PerAvg = Avg * 40
                print("The Percentage Average * 40 is: ", PerAvg)

                FinalTest = PerAvg / 60
                print("The Final Test / 60 is: ", FinalTest)

                AvgTest = FinalTest / 2
                print("The Average / 2 is: ", AvgTest)

                Equal = AvgTest + test1 + test2 + coursework
                print("The Final Equal Mark Added is: ", Equal)

                # Updating data to the txt file
                students.writerow(
                    [partier, Avg, PerAvg, FinalTest, AvgTest, Equal])
                opexcel.write('(Student Name):' + partier + '\n')
                opexcel.write('(Average):' + Avg + '\n')
                opexcel.write('(PerAvg):' + PerAvg + '\n')
                opexcel.write('(FinalTest):' + FinalTest + '\n')
                opexcel.write('(AvgTest):' + AvgTest + '\n')
                opexcel.write('(Equal):' + Equal + '\n')

                # write to Excel file
                opexcel = open('user.txt', 'r', encoding='utf8')
                details = opexcel.read()
                print(details)
                opexcel.close()
                # displaying content to excel file
                excel = open('user.csv', 'r')
                students = csv.reader(excel)
                for lines in students:
                    print(lines)
                excel.close()


# print("""
# -----RUN TEST TO CALCULATE BEST 2/3 % MARKS-----
#             -----------------------
# """)

# test1 = int(input("Enter the marks in the first test: "))
# test2 = int(input("Enter the marks in second test: "))
# coursework = int(input("Enter the marks in third test: "))

# if (test1 > test2):
#     if (test2 > coursework):
#         total = test1 + test2
#     else:
#         total = test1 + test2
# elif (test1 > coursework):
#     total = test1 + test2
# else:
#     total = test2 + coursework

# Avg = total / 2
# # with open('userInfo.txt', 'a') as file:
# #     for Avg in file:
# #         Avg = Avg.split()
# print("The Average of the Best two test marks is: ", Avg)

# PerAvg = Avg * 40
# print("The Percentage Average * 40 is: ", PerAvg)

# FinalTest = PerAvg / 60
# print("The Final Test / 60 is: ", FinalTest)

# AvgTest = FinalTest / 2
# print("The Average / 2 is: ", AvgTest)

# Equal = AvgTest + test1 + test2 + coursework
# print("The Final Equal Mark Added is: ", Equal)
