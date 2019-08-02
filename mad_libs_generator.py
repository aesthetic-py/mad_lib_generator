#Mad Libs Generator

'''First prompt the user for a series of inputs a la Mad Libs - nouns, adjectives, verbs, etc.
	Then, once all the information has been inputted, the program will take that data and place
	them into a premade story template. You'll need prompts for user input, and then print out 
	the full story at the end with the input included.

Mad Lib:

Tonight is the night when all of the __adjective__ monsters come out to __verb__, 
__adjective__ witches with big __noun__ and __color__ shoes make potions and very 
spooky brews. Vampires with __plural_noun__ and long red capes visit with friends and 
search for neck napes. Ogres and ghosts sometimes __verb__ and play, on this __adjective__
October day. All the trick-or-treaters __verb__ and hunt for __noun__ and a scare, dressed
up as princesses and cowboys here and there. Have a __adjective__ Halloween in 2019!

'''

adjective1 = input("Please enter an adjective:")

verb1 = input("Please enter a verb:")

adjective2 = input("Please enter another adjective:")

noun1 = input("Please enter a noun:")

color1 = input("Please enter a color:")

plural_noun1 = input("Please enter a plural noun:")

verb2 = input("Please enter another verb:")

adjective3 = input ("Please enter another adjective:")

verb3 = input("Please enter another verb:")

noun2 = input("Please enter another noun:")

adjective4 = input("Please enter another adjective:")


print('Tonight is the night when all of the ' + adjective1 + ' monsters come out to ' + verb1
	+ adjective2 + ' witches with big ' + noun1 + ' and ' + color1 + ''' shoes make potions and
	very spooky brews. Vampires with ''' + plural_noun1 + ''' and very long capes visit
	with friends and search for neck napes. Ogres and ghosts sometimes ''' + verb2 +
	' and play, on this ' + adjective3 + ' October day. All the trick-or-treaters ' +
	verb3 + ' and hunt for ' + noun2 + ''' and a scare, dressed up as  princesses and cowboys
	here and there. Have a ''' + adjective4 + ' Halloween in 2019!')