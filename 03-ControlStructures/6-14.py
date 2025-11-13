amount_of_media = 0

enter_media1 = bool(input("Facebook?"))
enter_media2 = bool(input("twitter?"))
enter_media3 = bool(input("instagram?"))

for media in (enter_media1, enter_media2, enter_media3):
    if media:
        amount_of_media += 1

if amount_of_media >= 2:
    print("You are a good influencer")
else:
    print("You need to work on your influence")