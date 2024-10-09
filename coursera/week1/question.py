# This function should add the two values if the value of the "kind" parameter is "add" or is not passed in,
# otherwise it should subtract the second value from the first.
def do_math(a, b, kind="add"):
    if kind == "add":
        return a + b
    else:
        return a - b


do_math(1, 2)

# What would be an appropriate slice to get the name "Christopher" from the string "Dr. Christopher Brooks"?
x = "Dr. Christopher Brooks"

print(x[4:15])

# Here is a list of faculty teaching this MOOC. Can you write a function
# and apply it using map() to get a list of all faculty titles and last names
# (e.g. ['Dr. Brooks', 'Dr. Collins-Thompson', …]) ?
people = [
    "Dr. Christopher Brooks",
    "Dr. Kevyn Collins-Thompson",
    "Dr. VG Vinod Vydiswaran",
    "Dr. Daniel Romero",
]


def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return "{} {}".format(title, lastname)


list(map(split_title_and_name, people))

# Convert this function into lamba
# people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

# def split_title_and_name(person):
#     return person.split()[0] + ' ' + person.split()[-1]

# #option 1
# for person in people:
#     print(split_title_and_name(person) == (lambda person:???))

# option 2
# list(map(split_title_and_name, people)) == list(map(???))

# converted below
people = [
    "Dr. Christopher Brooks",
    "Dr. Kevyn Collins-Thompson",
    "Dr. VG Vinod Vydiswaran",
    "Dr. Daniel Romero",
]


def split_title_and_name(person):
    return person.split()[0] + " " + person.split()[-1]


# option 1
for person in people:
    print(
        split_title_and_name(person)
        == (lambda x: x.split()[0] + " " + x.split()[-1])(person)
    )

# option 2
list(map(split_title_and_name, people)) == list(
    map(lambda person: person.split()[0] + " " + person.split()[-1], people)
)


# Here, why don’t you try converting a function into a list comprehension.
def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


# converted
times_tables() == [j * i for i in range(10) for j in range(10)]

# Here’s a harder question which brings a few things together.

# Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider
# and the user ids are all two letters followed by two numbers (e.g. aa49).
# Your task at such an organization might be to hold a record on the billing activity for each possible user.
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

correct_answer = [
    a + b + c + d for a in lowercase for b in lowercase for c in digits for d in digits
]

correct_answer[:50]  # Display first 50 ids
