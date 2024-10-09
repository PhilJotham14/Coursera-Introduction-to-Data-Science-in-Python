import sys

# try:
#     print("Hello, My name is", sys.argv[1])

# except IndexError:
#     print("Too few Arguments")

if len(sys.argv) < 2:
    # print("Too few Arguments")
    sys.exit("Too few Arguments")
# elif len(sys.argv) > 2:
#     print("Too many Arguments")
# else:
#     print("Hello, My name is", sys.argv[1])
for arg in sys.argv[1:]
print("Hello, My name is", argv)
# NOte: run code as py .\name.py "Zoe Deogudin" or py .\name.py Zoe
