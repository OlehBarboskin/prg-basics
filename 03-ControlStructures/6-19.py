interested_in_computer_science = input("Are you interested in computer science? (y/n): ")

if interested_in_computer_science.lower() == 'y':
    computer_science = True
else:
    computer_science = False

do_you_like_playing_computer_games = input("Do you like playing computer games? (y/n): ")

if do_you_like_playing_computer_games.lower() == 'y':
    computer_games = True
else:
    computer_games = False

do_you_have_instagram = input("Do you have Instagram? (y/n): ")

if do_you_have_instagram.lower() == 'y':
    instagram = True
else:
    instagram = False

print(f"SURVEY RESULTS:\nInterested in computer science: {computer_science}\nLikes playing computer games: {computer_games}\nHas Instagram: {instagram}")