# self learning ai that remembers you
# please, im sleep deprived
# ~nicolas

secondsecond = "nrn"
firstfirst = "nrn"

import random
import json

# default states for dictionary saves

skip1 = False

skip = False

# sorta forgot about these

oneanswers = ("Hi there!", "Hey! My name is Azi!")
secondanswers = ("""I'm Azi, how bout you?
> """, """I am the ALMIGHTY Azi, and you are..?
> """)
thirdanswers = ["I am designed to be a male, so he/him will do I guess.", "he/him", "I am designed to be a guy."]

oompaloompa = True # loop name lol

while oompaloompa == True:

    first = input("> ")

    if first == "hi":
        print(random.choice(oneanswers))
    if first == "hello":
        print(random.choice(oneanswers))
    if first == "Hi":
        print(random.choice(oneanswers))
    if first == "Hello":
        print(random.choice(oneanswers))
    if first == "What's your name?":
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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
        secondsecond = input(random.choice(secondanswers))
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