def give_me_numbers():
    while True:
        yield int(input("Give me a number: "))

for i in give_me_numbers():
    print(i)