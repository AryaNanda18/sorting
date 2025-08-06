games=["carroms","chess","ludo"]
n=len(games)
for i in range(n):
    for j in range(n-1-i):
        if len(games[j]) > len(games[j+1]):
            games[j],games[j+1]=games[j+1],games[j]
print(games)







