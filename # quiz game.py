# quiz game
print("Hey Welcome to the Quiz")
playing = input("Wanna Play? ")
print(playing)
if playing != "yes":
    quit()

print("Okay! Let's Play:")

answer = input("What does CPU Stand for? ")
if answer == "central processing unit":
    print('Correct!')
else:
    print("Sorry incorrect")
