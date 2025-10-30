movie = "The Lord of the Rings: The Return of the King"
capitalized = movie.capitalize
lowercased = movie.casefold
counted_e = movie.count('e')
found_lord = movie.find('Lord')
found_dragon = movie.find('dragon')

print('Number of characters: ', len(movie))

print(f"capital letters  {capitalized}" )

print(f"lowercase letters {lowercased}")

print(f"counted e times: {counted_e}")

print(f"Lord is at: {found_lord}")

print(f"Dragon is at: {found_dragon}")