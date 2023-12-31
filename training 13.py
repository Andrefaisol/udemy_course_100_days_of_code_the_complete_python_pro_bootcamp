############DEBUGGING#####################

# # Describe Problem
# def my_function():
#     for i in range(1, 20):  # + 1: #  not reach number 20 because second parameter will be -1,
#         if i == 20:                 # add + 1 to reach range
#             print("You got it")
# my_function()
# # my answer: not reach number 20 because second parameter will be -1, add + 1 to reach range

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# # my answer: change a = 0 and b = 5, list order start with 0 and last order always -1

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")
# # my answer: if year is 1980 or 1994 code will skip because not catch the if statement
# # and year under 1980 not yet have statement

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# my answer: age constant parameter not yet define and also if input age 18 code will skip
# instead make legal_age = 18 and statement id age >= legal_age:
# and change {age} to {legal_age}
# indent not in place and need to cast in to string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# my answer: on line 39 should be =, not ==

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#     b_list.append(new_item)
#     print(b_list)
#

# mutate([1,2,3,5,8,13])
# # my answer: append not right intend, the append outside of loop
# # so the code only append last index