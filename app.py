import wikipedia

# edmonton = wikipedia.page('Edmonton')
# print (edmonton.title)
# print (edmonton.content)

user_choice = input('Know more about: ')
choice = wikipedia.page(user_choice)

try:
    print (choice.title)
    print (choice.content)
    
except wikipedia.exceptions.PageError:
    print("Sorry! Page does not exist")

finally:
    print('I will always be here, error or no error :)')
