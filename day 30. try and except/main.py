
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("fruit pie")
#     else:
#         print(fruit, "pie")
#
# make_pie(1)  # Raises IndexError on list with less than 5 items.
#



#
# facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3},
#                   {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]
#
# total_likes = 0
# # TODO: Catch the KeyError exception
# for post in facebook_posts:
#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         pass
#
# print(total_likes)


import pandas

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for index, row in nato_df.iterrows()}

while True:
    try:
        word = input("Enter a word :").upper()
        phonetic_code_list = [nato_dict[letter]for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(phonetic_code_list)
        break
