# Jarad, the AI

# 22/11/21 Jarad now has a neural network
# He isn't stupid anymore!

# ~nicolas

import random
import json
import math


secondsecond = "nrn"
firstfirst = "nrn"
namename = ""
yourFavFood = "nrn"

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


    if first == "What's your name?":
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

    if first == "Whats your name?":
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


    if first == "what's your name?":
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

    if first == "whats your name?":
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


    if first == "whats your name":
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


    if first == "What's ur name?":
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


    if first == "whats ur name?":
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


    if first == "whats ur name":
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


    if first == "whats my name":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

        
    if first == "what's my name":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    if first == "What's my name":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    if first == "What's my name?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    if first == "whats my name?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    if first == "Whats my name?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    if first == "what's my name?": # checks dict.json for you name

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print(why2['Name'])

    if first == ("what r ur pronouns"):
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

    if first == ("what are ur pronouns"):
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


    if first == ("what are your pronouns"):
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


    if first == ("what are your pronouns?"):
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


    if first == ("What r ur pronouns?"):
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


    if first == ("what r ur pronouns?"):
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


    if first == ("What are your pronouns?"):
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


    if first == ("what are ur pronouns"):
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


    if first == ("what r your pronouns"):
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


    if first == ("what are ur pronouns?"):
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


    if first == ("what r your pronouns?"):
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

    if first == "what are my pronouns":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])
        
    if first == "What are my pronouns":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "what r my pronouns":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "What r my pronouns":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "What are my pronouns?":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "what are my pronouns?":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "what r my pronouns?":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "What r my pronouns?":

        why3 = open('dict.json', 'r')
        why4 = json.load(why3)

        print(why4['Pronouns'])

    if first == "do you believe in me?":
        print(random.choice(fiveanswers))

    if first == "Do you believe in me?":
        print(random.choice(fiveanswers))

    if first == "do u believe in me?":
        print(random.choice(fiveanswers))

    if first == "do you believe in me":
        print(random.choice(fiveanswers))

    if first == "Do you believe in me":
        print(random.choice(fiveanswers))

    if first == "Do u believe in me?":
        print(random.choice(fiveanswers))

    if first == "Do u believe in me":
        print(random.choice(fiveanswers))

    if first == "do u believe in me":
        print(random.choice(fiveanswers))

##

    if first == "are u my friend":
        print(random.choice(fourthanswers))

    if first == "Are u my friend":
        print(random.choice(fourthanswers))

    if first == "are u my friend?":
        print(random.choice(fourthanswers))

    if first == "Are u my friend?":
        print(random.choice(fourthanswers))

    if first == "are you my friend?":
        print(random.choice(fourthanswers))

    if first == "Are you my friend?":
        print(random.choice(fourthanswers))

    if first == "Are you my friend":
        print(random.choice(fourthanswers))

    if first == "are you my friend":
        print(random.choice(fourthanswers))

    if first == "friend":
        print(random.choice(fourthanswers))

    if first == "Friend":
        print(random.choice(fourthanswers))

    if first == "friend?":
        print(random.choice(fourthanswers))

    if first == "Friend?":
        print(random.choice(fourthanswers))

    if first == "friends":
        print(random.choice(fourthanswers))

    if first == "Friends":
        print(random.choice(fourthanswers))

    if first == "friends?":
        print(random.choice(fourthanswers))

    if first == "Friends?":
        print(random.choice(fourthanswers))

##

    if first == "who am i":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "Who am i":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "who am I":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "who am i?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "Who am I":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "who am I?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "Who am I?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

    if first == "Who am i?":

        why = open('dict.json', 'r')
        why2 = json.load(why)

        print('You are', why2['Name'])
        print('Why would I forget?')

        #/*

    if first == "What is your favorite food?":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "what is your favorite food?":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "What is your favorite food":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "what is your favorite food":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "What is ur favorite food?":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "what is ur favorite food?":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "What is ur favorite food":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

    if first == "what is ur favorite food":
        yourFavFood = input("""If you tell me, I'll tell you
> """)
        print(random.choice(sixthasnwers))

 #*/


    if first == "joke":
        jokeCatalog = open('jokesdict.json', 'r')
        jokesCatalog = json.load(jokeCatalog)

        randomJoke = jokesCatalog["Jokes1"], jokesCatalog["Jokes2"], jokesCatalog["Jokes3"], jokesCatalog["Jokes4"], jokesCatalog["Jokes5"]

        print(random.choice(randomJoke))

    if first == "Joke":
        jokeCatalog = open('jokesdict.json', 'r')
        jokesCatalog = json.load(jokeCatalog)

        randomJoke = jokesCatalog["Jokes1"], jokesCatalog["Jokes2"], jokesCatalog["Jokes3"], jokesCatalog["Jokes4"], jokesCatalog["Jokes5"]

        print(random.choice(randomJoke))

    if first == "joke?":
        jokeCatalog = open('jokesdict.json', 'r')
        jokesCatalog = json.load(jokeCatalog)

        randomJoke = jokesCatalog["Jokes1"], jokesCatalog["Jokes2"], jokesCatalog["Jokes3"], jokesCatalog["Jokes4"], jokesCatalog["Jokes5"]

        print(random.choice(randomJoke))

    if first == "Joke?":
        jokeCatalog = open('jokesdict.json', 'r')
        jokesCatalog = json.load(jokeCatalog)

        randomJoke = jokesCatalog["Jokes1"], jokesCatalog["Jokes2"], jokesCatalog["Jokes3"], jokesCatalog["Jokes4"], jokesCatalog["Jokes5"]

        print(random.choice(randomJoke))

#/*

    if first == "fact": # fact command
        factCatalog = open('factdict.json', 'r') # opens the fact dictionary
        factsCatalog = json.load(factCatalog) # loads the fact dictionary

        randomFact = factsCatalog["Fact1"], factsCatalog["Fact2"], factsCatalog["Fact3"], factsCatalog["Fact4"], factsCatalog["Fact5"]

        # self explanitory

        print(random.choice(randomFact)) # chooses a random fact from the "randomFact" list

    if first == "tell me a fact":
        factCatalog = open('factdict.json', 'r')
        factsCatalog = json.load(factCatalog)

        randomFact = factsCatalog["Fact1"], factsCatalog["Fact2"], factsCatalog["Fact3"], factsCatalog["Fact4"], factsCatalog["Fact5"]

        print(random.choice(randomFact))

    if first == "Fact":
        factCatalog = open('factdict.json', 'r')
        factsCatalog = json.load(factCatalog)

        randomFact = factsCatalog["Fact1"], factsCatalog["Fact2"], factsCatalog["Fact3"], factsCatalog["Fact4"], factsCatalog["Fact5"]

        print(random.choice(randomFact))

    if first == "Tell me a fact":
        factCatalog = open('factdict.json', 'r')
        factsCatalog = json.load(factCatalog)

        randomFact = factsCatalog["Fact1"], factsCatalog["Fact2"], factsCatalog["Fact3"], factsCatalog["Fact4"], factsCatalog["Fact5"]

        print(random.choice(randomFact))

    if first == "Tell me a fact.":
        factCatalog = open('factdict.json', 'r')
        factsCatalog = json.load(factCatalog)

        randomFact = factsCatalog["Fact1"], factsCatalog["Fact2"], factsCatalog["Fact3"], factsCatalog["Fact4"], factsCatalog["Fact5"]

        print(random.choice(randomFact))

    if first == "tell me a fact.":
        factCatalog = open('factdict.json', 'r')
        factsCatalog = json.load(factCatalog)

        randomFact = factsCatalog["Fact1"], factsCatalog["Fact2"], factsCatalog["Fact3"], factsCatalog["Fact4"], factsCatalog["Fact5"]

        print(random.choice(randomFact))

    if first == "what is your favorite genre":
        print('My favorite genre of music is Electronic!')

    if first == "what is your favorite genre?":
        print('My favorite genre of music is Electronic!')

    if first == "What is your favorite genre":
        print('My favorite genre of music is Electronic!')

    if first == "What is your favorite genre?":
        print('My favorite genre of music is Electronic!')

    if first == "what is your favorite genre of music?":
        print('My favorite genre of music is Electronic!')

    if first == "what is your favorite genre of music":
        print('My favorite genre of music is Electronic!')

    if first == "What is your favorite genre of music":
        print('My favorite genre of music is Electronic!')

    if first == "What is your favorite genre of music?":
        print('My favorite genre of music is Electronic!')

    if first == "What is ur favorite genre":
        print('My favorite genre of music is Electronic!')

    if first == "what is ur favorite genre":
        print('My favorite genre of music is Electronic!')

    if first == "What is ur favorite genre?":
        print('My favorite genre of music is Electronic!')

    if first == "what is ur favorite genre?":
        print('My favorite genre of music is Electronic!')

    if first == "What is ur favorite genre of music?":
        print('My favorite genre of music is Electronic!')

    if first == "what is ur favorite genre of music?":
        print('My favorite genre of music is Electronic!')

    if first == "What is ur favorite genre of music":
        print('My favorite genre of music is Electronic!')

    if first == "what is ur favorite genre of music": # im just bored ffs
        print('My favorite genre of music is Electronic!')
        #*/
    if first == "how old r u":
        print(random.choice(ageInSmallLetters))

    if first == "how old are u":
        print(random.choice(ageInSmallLetters))

    if first == "how old r you":
        print(random.choice(ageInSmallLetters))

    if first == "how old are you":
        print(random.choice(ageInSmallLetters))

    if first == "How old are u":
        print(random.choice(ageInSmallLetters))

    if first == "How old r you":
        print(random.choice(ageInSmallLetters))

    if first == "How old are you":
        print(random.choice(ageInSmallLetters))

    if first == "How old r u":
        print(random.choice(ageInSmallLetters))

    if first == "how old r u?":
        print(random.choice(ageInSmallLetters))

    if first == "how old are u?":
        print(random.choice(ageInSmallLetters))

    if first == "how old r you?":
        print(random.choice(ageInSmallLetters))

    if first == "how old are you?":
        print(random.choice(ageInSmallLetters))

    if first == "How old are u?":
        print(random.choice(ageInSmallLetters))

    if first == "How old r you?":
        print(random.choice(ageInSmallLetters))

    if first == "How old are you?":
        print(random.choice(ageInSmallLetters))

    if first == "How old r u?":
        print(random.choice(ageInSmallLetters))

#/*
    if first == "name":
        namename = input('''What should my name be then?
> ''')  
        dictname = {"AIName": namename}

    with open('namedict.json', 'w') as namedictionary:
        json.dump(dictname, namedictionary)

    if first == "Name":
        namename = input('''What should my name be then?
> ''')  
        dictname = {"AIName": namename}

    with open('namedict.json', 'w') as namedictionary:
        json.dump(dictname, namedictionary)

    if first == "name?":
        namename = input('''What should my name be then?
> ''')  
        dictname = {"AIName": namename}

    with open('namedict.json', 'w') as namedictionary:
        json.dump(dictname, namedictionary)

    if first == "Name?":
        namename = input('''What should my name be then?
> ''')  
        dictname = {"AIName": namename}

    with open('namedict.json', 'w') as namedictionary:
        json.dump(dictname, namedictionary)

#*/

    if first == "Favorite Game?":
        print(random.choice(gameFav))

    if first == "favorite Game?":
        print(random.choice(gameFav))

    if first == "Favorite game?":
        print(random.choice(gameFav))

    if first == "favorite game?":
        print(random.choice(gameFav))

    if first == "Favorite Game":
        print(random.choice(gameFav))

    if first == "Favorite game":
        print(random.choice(gameFav))

    if first == "favorite Game":
        print(random.choice(gameFav))

    if first == "favorite game":
        print(random.choice(gameFav))
#/*

    if first == "What came first, the chicken or the egg?":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "What came first the chicken or the egg?":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "what came first, the chicken or the egg?":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "what came first the chicken or the egg?":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "What came first, the chicken or the egg":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "what came first, the chicken or the egg":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "What came first the chicken or the egg":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

    if first == "what came first the chicken or the egg":
        chickCatalog = open('advanceddict.json', 'r')
        chickenCatalog = json.load(chickCatalog)

        print(chickenCatalog["ChickenQuest"])

#*/

    if first == "What happened before the Big Bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "what happened before the Big Bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "What happened before the Big Bang":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "what happened before the Big Bang":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "What happened before the big Bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "what happened before the big Bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "What happened before the Big bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "what happened before the Big bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "What happened before the big bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "what happened before the big bang?":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "What happened before the big bang":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

    if first == "what happened before the big bang":
        bangCatalog = open('advanceddict.json', 'r')
        bangerCatalog = json.load(bangCatalog)

        BangError123 = bangerCatalog['BigBangQuest'], bangerCatalog['BigBangError']

        print(random.choice(BangError123))

#*/

    if first == "What does pain feel like?":
        painCatalog = open('advanceddict.json', 'r')
        painersCatalog = json.load(painCatalog)

        print(painersCatalog['PainQuest'])

    if first == "what does pain feel like?":
        painCatalog = open('advanceddict.json', 'r')
        painersCatalog = json.load(painCatalog)

        print(painersCatalog['PainQuest'])

    if first == "What does pain feel like":
        painCatalog = open('advanceddict.json', 'r')
        painersCatalog = json.load(painCatalog)

        print(painersCatalog['PainQuest'])

    if first == "what does pain feel like":
        painCatalog = open('advanceddict.json', 'r')
        painersCatalog = json.load(painCatalog)

        print(painersCatalog['PainQuest'])

#*/

    if first == "Who is God?":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "who is God?":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "Who is god?":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "who is god?":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "Who is God":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "Who is god":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "who is God":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

    if first == "who is god":
        godCatalog = open('advanceddict.json', 'r')
        godsCatalog = json.load(godCatalog)

        print(godsCatalog['GodQuest'])

#/*

    if first == "Pick a number":
        firstask1 = input('''Input a number, please.
> ''')

        firstask2 = input('''Input another number, please.
> ''')

        result = int(firstask1)/int(firstask2)

        print('I got this:', result)

    if first == "pick a number":
        firstask1 = input('''Input a number, please.
> ''')

        firstask2 = input('''Input another number, please.
> ''')

        result = int(firstask1)/int(firstask2)

        print('I got this:', result)

    if first == "Pick a number.":
        firstask1 = input('''Input a number, please.
> ''')

        firstask2 = input('''Input another number, please.
> ''')

        result = int(firstask1)/int(firstask2)

        print('I got this:', result)

    if first == "pick a number.":
        firstask1 = input('''Input a number, please.
> ''')

        firstask2 = input('''Input another number, please.
> ''')

        result = int(firstask1)/int(firstask2)

        print('I got this:', result)