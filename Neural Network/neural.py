# Jarad, the AI

# 22/11/21 Jarad now has a neural network
# He isn't stupid anymore!

# ~nicolas



import random
import json
import math
import datetime

lookFor = ["'", "?", ".", "!", "(", ")", ":"]

secondsecond = "nrn"
firstfirst = "nrn"
namename = ""
yourFavFood = "nrn"
currentDMY = datetime.datetime.now()

dictname = {"AIName": "Jarad"}

with open('namedict.json', 'w') as namedictionary:
    json.dump(dictname, namedictionary)

# default states for dictionary saves

skip1 = False

skip = False

# sorta forgot about these

thirdanswers = ["I am designed to be a male, so he/him will do I guess.", "he/him", "I am designed to be a guy."]
fourthanswers = ["I don't think you can consider me a friend, since I am a robot, and do not exist.", "I am a robot, I cannot express love.", "I could be your friend if you would like, but I cannot commit."]
fiveanswers = ["I believe in you!", "I support you.", "If you can do it, I'll support you all the way!"]
sixthasnwers = ["My favorite food? Obviously it's chips!", f"I am a computer generated being, my favorite food is... {yourFavFood}", "Cheese of course!"]
ageInSmallLetters = ["I am however old you are!", "I am 1 year old.", "I am the age of your computer!?"]
gameFav = ["Apex Legends", "I don't believe I have one", "Mine is whatever yours is!"]

oompaloompa = True # loop name lol

while oompaloompa == True:

    first = input("> ")
    gM = first

    if first == "hi":
        why6 = open('namedict.json', 'r')
        why7 = json.load(why6)

        print("Hi! I am", why7['AIName'])
    if first == "hello":
        why6 = open('namedict.json', 'r')
        why7 = json.load(why6)

        print("Hi! I am", why7['AIName'])
    if first == "Hi":
        why6 = open('namedict.json', 'r')
        why7 = json.load(why6)

        print("Hi! I am", why7['AIName'])
    if first == "Hello":
        why6 = open('namedict.json', 'r')
        why7 = json.load(why6)

        print("Hi! I am", why7['AIName'])

        #/*

    first = first.replace("'", "")
    first = first.replace("?", "")
    first = first.replace("what", "What")
    if "Whats your name" in first:
        why6 = open('namedict.json', 'r')
        why7 = json.load(why6)

        print(why7['AIName'])
        secondsecond = input("""And you are?
> """)
        print("Ah,", secondsecond, "nice to meet you!")

        if skip == False:

            dicta = {"Name":secondsecond, "Pronouns":"Syntax Not Found"}

            with open('dict.json', 'w') as dictionary:
                json.dump(dicta, dictionary)

            skip1 = True


        if skip == True:


            dicta = {"Name":secondsecond, "Pronouns":firstfirst}

            with open('dict.json', 'w') as dictionary:
                json.dump(dicta, dictionary)

    skip1 = True

    first = first.replace("'", "")
    first = first.replace("?", "")
    first = first.replace("what", "What")
    if "Whats my name" in first: # checks dict.json for you name

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    first = first.replace("your", "ur")
    first = first.replace("?", "")
    first = first.replace("what", "What")
    if "What r ur pronouns" in first:

        print(random.choice(thirdanswers))
        firstfirst = input("""What are your pronouns?
> """)
        print(firstfirst, "I'll remember that!")

        if skip1 == False:

            dicta = {"Name":"Syntax Not Found", "Pronouns":firstfirst}

            with open('dict.json', 'w') as dictionary:
                json.dump(dicta, dictionary)

            skip = True


        if skip1 == True:


            dicta = {"Name":secondsecond, "Pronouns":firstfirst}

            with open('dict.json', 'w') as dictionary:
                json.dump(dicta, dictionary)

    first = first.replace("your", "ur")
    first = first.replace("?", "")
    first = first.replace("what", "What")
    if "What are ur pronouns" in first:

        print(random.choice(thirdanswers))
        firstfirst = input("""What are your pronouns?
> """)
        print(firstfirst, "I'll remember that!")

        if skip1 == False:

            dicta = {"Name":"Syntax Not Found", "Pronouns":firstfirst}

            with open('dict.json', 'w') as dictionary:
                json.dump(dicta, dictionary)

            skip = True


        if skip1 == True:


            dicta = {"Name":secondsecond, "Pronouns":firstfirst}

            with open('dict.json', 'w') as dictionary:
                json.dump(dicta, dictionary)

    skip = True

    first = first.replace("?", "")
    first = first.replace("what", "What")
    if "What r my pronouns" in first:

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    first = first.replace("?", "")
    first = first.replace("what", "What")
    if "What are my pronouns" in first:

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])
        
    first = first.replace("you", "u")
    first = first.replace("?", "")
    first = first.replace("do", "Do")
    if "Do u believe in me" in first:
        print(random.choice(fiveanswers))

##

    first = first.replace("tell", "Tell")
    first = first.replace(".", "")
    first = first.replace("urself", "yourself")
    
    if "Tell me about yourself" in first:
        print("im jarad, lol")
    
##
    
    first = first.replace("generate", "Generate")
    first = first.replace(".", "")

    if "Generate a password" in first:

        openNow = open("num.json", "r")
        openTwice = json.load(openNow)

        Randomize = openTwice["1"], openTwice["2"], openTwice["3"], openTwice["4"], openTwice["5"], openTwice["6"], openTwice["7"], openTwice["8"], openTwice["9"], openTwice["0"], openTwice["!"], openTwice["@"], openTwice["#"], openTwice["$"], openTwice["%"], openTwice["^"], openTwice["&"], openTwice["*"], openTwice["("], openTwice[")"], openTwice["-"], openTwice["_"], openTwice["="], openTwice["+"], openTwice["q"], openTwice["w"], openTwice["e"], openTwice["r"], openTwice["t"], openTwice["y"], openTwice["u"], openTwice["i"], openTwice["o"], openTwice["p"], openTwice["a"], openTwice["s"], openTwice["d"], openTwice["f"], openTwice["g"], openTwice["h"], openTwice["j"], openTwice["k"], openTwice["l"], openTwice["z"], openTwice["x"], openTwice["c"], openTwice["v"], openTwice["b"], openTwice["n"], openTwice["m"], openTwice["."], openTwice["<"], openTwice[">"], openTwice["/"], openTwice["?"]

        Randomize2 = Randomize

        Randomize3 = Randomize

        Randomize4 = Randomize

        Randomize5 = Randomize

        Randomize6 = Randomize

        Randomize7 = Randomize

        Randomize8 = Randomize

        Randomize9 = Randomize

        Randomize10 = Randomize

        print(f"{random.choice(Randomize)}{random.choice(Randomize2)}{random.choice(Randomize3)}{random.choice(Randomize4)}{random.choice(Randomize5)}{random.choice(Randomize6)}{random.choice(Randomize7)}{random.choice(Randomize8)}{random.choice(Randomize9)}{random.choice(Randomize10)}")

##
    first = first.replace("who", "Who")
    first = first.replace("am i", "am I")
    first = first.replace("?", "")
    if "Who am I" in first:

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

       

 #*/

    first = first.replace("tell", "Tell")
    first = first.replace(".", "")
    if "Tell me a joke" in first:
        jokeCatalog = open('jokesdict.json', 'r')
        jokesCatalog = json.load(jokeCatalog)

        randomJoke = jokesCatalog["Jokes1"], jokesCatalog["Jokes2"], jokesCatalog["Jokes3"], jokesCatalog["Jokes4"], jokesCatalog["Jokes5"]

        print(random.choice(randomJoke))

#*/
    
    first = first.replace("favorite", "Favorite")
    first = first.replace("?", "")
    if "Favorite game" in first:
        print(random.choice(gameFav))


    first = first.replace("depressed", "Depression")
    first = first.replace("depression", "Depression")
    first = first.replace("Depression", "Depression")
    first = first.replace("jarad", "Jarad")
    first = first.replace(".", "")
    if 'Jarad i am Depression' in first:
        depressionHotlineInput = input('''Where are you from? - US, UK, AU (Australia), CA (Canada)
> ''')

        hotlineCatalog = open('hotlines.json', 'r')
        hotlinesCatalog = json.load(hotlineCatalog)

        print(hotlinesCatalog[depressionHotlineInput])
            
#/*

    first = first.replace("pick", "Pick")
    first = first.replace(".", "")
    if "Pick a number" in first:
        firstask1 = input('''Input a number, please.
> ''')

        firstask2 = input('''Input another number, please.
> ''')

        result = int(firstask1)/int(firstask2)

        print('I got this:', result)

#/*
    ###################################################################################3

    first = first.replace("open", "Open")
    first = first.replace(".", "")
    if "Open dictionary" in first:

        dictquestiona = input('''What word are you looking for?
> ''')
        Catalog = open('worddict.json', 'r')
        sCatalog = json.load(Catalog)

        print(sCatalog[dictquestiona])

    first = first.replace("save", "Save")
    first = first.replace(".", "")
    if "Save my email" in first:
        firstInput = input('''What should we call this email?
> ''')
        secondInput = input('''What is the email we are adding?
> ''')
        thirdInput = input('''What is the password to this email?
> ''')

        theDump = {'Name#':firstInput, 'Email#':secondInput, 'Pass#':thirdInput}

        with open('emaildict.json', 'w') as dictionarial:
            json.dump(theDump, dictionarial)

    first = first.replace("'", "")
    first = first.replace("what", "What")
    first = first.replace(".", "")
    if "Whats my email" in first:
        why = open('emaildict.json', 'r')
        why2 = json.load(why)

        print(why2['Name#'], "is", why2['Email#'], "password is", why2['Pass#'])


#/* Christmas Update

    first = first.replace("sing", "Sing")
    first = first.replace(".", "")
    if "Sing me a tune" in first:
        tune = input('''What is the tune I should sing? Includes: Christmas, Rock & Pop
> ''')
        if tune == 'Christmas':
            whatKind = input('''What kind of Christmas tune?
> ''')
            if whatKind == 'Mariah Carrey':
                mariah = print('no.')

            if whatKind == 'mariah carrey':
                mariah = print('no.')

        if tune == 'christmas':
            whatKind = input('''What kind of Christmas tune?
> ''')
            if whatKind == 'Mariah Carrey':
                mariah = print('no.')

            if whatKind == 'mariah carrey':
                mariah = print('no.')

        if tune == 'Rock':
            print('We will, we will, ROCK YOU!')

        if tune == 'rock':
            print('We will, we will, ROCK YOU!')

        if tune == 'Pop':
            popMusic = input('''Are you sure?
> ''')
            if popMusic == 'Yes':
                print('...')

            if popMusic == 'No':
                print('k')

        if tune == 'pop':
            popMusic = input('''Are you sure?
> ''')
            if popMusic == 'Yes':
                print('...')

            if popMusic == 'No':
                print('k')

        if tune == 'Pop':
            popMusic = input('''Are you sure?
> ''')
            if popMusic == 'yes':
                print('...')

            if popMusic == 'no':
                print('k')

        if tune == 'pop':
            popMusic = input('''Are you sure?
> ''')
            if popMusic == 'yes':
                print('...')

            if popMusic == 'no':
                print('k')

#/* Other Christmas Stuff

    first = first.replace("recipe", "Recipe")
    first = first.replace(".", "")
    if 'Recipe for pudding' in first:
        puddingLoad = open('recipedict.json', 'r')
        puddingClean = json.load(puddingLoad)

        print(puddingClean["RecipePuddingIng"], puddingClean["RecipePuddingDir"])
    #

    first = first.replace("what is the", "What is the")
    first = first.replace("?", "")
    if 'What is the date today' in first:
        print(f'The date today is {currentDMY}')