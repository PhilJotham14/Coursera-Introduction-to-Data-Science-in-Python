

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


# How to anticipate for errors using try and expect
# We can use loop to prompt users to re-enter correct values again and again.
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            # though this below coplicates code and makes it difficult to understand.
            # or return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
            # instead of "print("x is not an integer")" we could use pass though it wont notify user why they are being prompt
            # pass
        # if true then the loop breaks
        else:
            break
    # "return" returns values from a function than break which breaks you of a loop on;y so return is good since it does both.
    return x


main()

# print(f"x is {x}")
