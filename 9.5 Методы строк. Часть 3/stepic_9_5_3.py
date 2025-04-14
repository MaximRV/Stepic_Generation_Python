nickname = input()

if (nickname.startswith('@') and
    5 <= len(nickname) <= 15 and
    all(c.isdigit() or ('a' <= c <= 'z') for c in nickname[1:])):
    print("Correct")
else:
    print("Incorrect")