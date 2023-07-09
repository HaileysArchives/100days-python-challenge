# Print is Your friend

pages = 0
word_per_page = 0

pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) => False (0 == 250)
# So we need to change equal sign.

word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page

# print(f"pages = {pages}")
# print(f"word_per_page = {word_per_page}")
print(total_words)
