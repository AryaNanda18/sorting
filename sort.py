games=["carroms","chess","ludo"]
n=len(games)
for i in range(n):
    for j in range(n-1-i):
        if len(games[j]) > len(games[j+1]):
            #swapping if no of alphabets in first game is greater than next
            games[j],games[j+1]=games[j+1],games[j]
#to print the games in order
print(games)







