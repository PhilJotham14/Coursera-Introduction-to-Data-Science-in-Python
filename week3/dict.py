# partyanimals = dict()
# n = int(input("How many Party Animals are their: "))
# for i in range(n):
#     name = input("Enter name of Party Animals: ")
#     gift = input("Enter Gifts Brought: ")
#     gender = input("Input your Gender: ")
#     phonenumber = input("Enter your phone number: ")
#     dateOfBirth = input("Enter your date of birth: ")

#     gifts = []
#     genders = []
#     phonenumbers = []
#     dateOfBirths = []

#     gifts.append(gift)
#     genders.append(gender)
#     phonenumbers.append(phonenumber)
#     dateOfBirths.append(dateOfBirth)

#     partyanimals[name] = gifts, genders, phonenumbers, dateOfBirths

# print("Created Dictioanry of Party Animals is ", partyanimals)


partyanimals = {}

print("""
Birthday Attendance
-----------------------
1: Add Participant
2: View Participants
0: Exit Program

""")
option = int(input("Enter an option: "))

while option != 0:
    if option == 1:
        partier = input("Enter name of Participant: ")

        if partier in partyanimals:
            print("Participant Already Added")
            gift = input("Enter Gift: ")
            gender = input("Input your Gender: ")
            phonenumber = input("Enter your phone number: ")
            dateOfBirth = input("Enter your date of birth: ")
            # partyanimals[item] = partyanimals[item] + gift
            # partyanimals[item] = partyanimals[item] + gender
            # partyanimals[item] = partyanimals[item] + phonenumber
            # partyanimals[item] = partyanimals[item] + dateOfBirth
            partyanimals[partier] = gift, gender, phonenumber, dateOfBirth
        else:
            gift = input("Enter Gift: ")
            gender = input("Input your Gender: ")
            phonenumber = input("Enter your phone number: ")
            dateOfBirth = input("Enter your date of birth: ")
            # partyanimals[item] = gift
            # partyanimals[item] = gender
            # partyanimals[item] = phonenumber
            # partyanimals[item] = dateOfBirth
            partyanimals[partier] = gift, gender, phonenumber, dateOfBirth

    elif option == 2:
        for partier in partyanimals:
            print(partier, ":", partyanimals[partier])

    elif option != 0:
        print("You didnt enetr a valid participant.")

    option = int(input("\n\nEnter an option: "))
