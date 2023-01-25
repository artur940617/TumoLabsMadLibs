from tkinter import *

# initialize window.
root = Tk()
root.geometry('300x300')
root.title('Tumo Labs Mad Libs Generator')
Label(root, text='Mad Libs Story \n Have Fun!', font='arial 30 bold').pack()
Label(root, text='Click Any One :', font='arial 13 bold').place(x=100, y=90)


# Stories
def madlib1():
    Number = input('Input a Number : ')
    Measure_of_time = input('Input a Measure of Time: ')
    Mode_of_Transportation = input('Input a mode of Transportation: ')
    Adjective = input('Input a Adjective: ')
    Adjective2 = input('Input a Adjective: ')
    Noun = input('Input a Noun: ')
    Color = input('Input a Color: ')
    Part_of_the_Body = input('Input a Part of the Body: ')
    Verb = input('Input a Verb: ')
    Number2 = input('Input a Number: ')
    Noun2 = input('Input a Noun: ')
    Noun3 = input('Input a Noun: ')
    Part_of_the_Body2 = input('Input a Part of the Body: ')
    Noun4 = input('Input a Noun: ')
    Adjective3 = input('Input a Adjective: ')
    Silly_Word = input('Input a Silly Word: ')

    print(f'It was about {Number} {Measure_of_time} ago when I arrived at the hospital in a {Mode_of_Transportation}.'
          f'The hospital is a/an {Adjective} place, there are a lot of {Adjective2} {Noun} here. There are nurses here'
          f'who have {Color} {Part_of_the_Body} . If someone wants to come into my room I told them that they have to '
          f'{Verb} first. I’ve decorated my room with  {Number2} {Noun2} . Today I talked to a doctor and they were'
          f'wearing  a {Noun3}  on their {Part_of_the_Body2} .I heard that all doctors  {Verb} {Noun4}  every day for'
          f'breakfast.The most {Adjective3}  thing about being in the hospital is the {Silly_Word} {Noun}!')


def madlib2():
    Proper_Noun = input('Input proper noun : ')
    Person_Name = input('Input a person name : ')
    Noun = input('Input a Noun :')
    Adjective_Feeling = input('Input a Adjective (feeling) : ')
    Verb = input('Input a Verb : ')
    Adjective_Feeling_2 = input('Input a Adjactive (feeling) : ')
    Animal = input('Input a Animal : ')
    Verb2 = input('Input a Verb : ')
    Color = input('Input a Color : ')
    Verb_ing = input('Input a Verb name ending in ing : ')
    Adverb_ly = input('Input a Adverb ending in ly : ')
    Number = input('Input a Verb number : ')
    Measure_of_Time = input('Input a Measure of Time : ')
    Silly_Word = input('Input a Silly Word : ')
    Noun2 = input('Input a Noun : ')

    print(f'This weekend I am going camping with {Proper_Noun} {Person_Name}. I packed my lantern, sleeping bag, and '
          f'{Noun}. I am so {Adjective_Feeling} to {Verb} in a tent. I am {Adjective_Feeling_2} we might see a(n) '
          f'{Animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {Verb2}. '
          f'I have heard that the {Color} lake is great for {Verb_ing}. Then we will {Adverb_ly} hike through the '
          f'forest for {Number} {Measure_of_Time}. If I see a {Color} {Animal} while hiking, I am going'
          f'to bring it home as a pet! At night we will tell {Number} {Silly_Word} stories and roast {Noun2} around the'
          f'campfire!!')


def madlib3():
    Proper_Noun = input('Input proper noun: ')
    Person_Name = input('Input person name : ')
    Adjective = input('Input Adjective : ')
    Color = input('Input a color: ')
    Animal = input('Input a Animal : ')
    Place = input('Input place : ')
    Adjective2 = input('Input a Adjective : ')
    Magical_Creature_plural = input('Input Magical Creature Plural : ')
    Adjective3 = input('Input a Adjective: ')
    Magical_Creature_Plural2 = input('Input a Magical Creature Plural: ')
    Room_house = input('Input a Room in a House : ')
    Noun = input('Input a thing noun : ')
    Noun2 = input('Input a thing Noun : ')
    Noun_Plural3 = input('Input a noun plural  : ')
    Adjective4 = input('Input a thing Noun : ')
    Noun_Plural4 = input('Input a noun plural  : ')
    Number = input('Input a number : ')
    Measure_of_time = input('Input a Measure of time  : ')
    Verb_ing = input('Input a verb ending in ing  : ')
    Adjective5 = input('Input a Adjective : ')
    Noun5 = input('Input a noun : ')

    print(
        f'Dear {Proper_Noun} {Person_Name}, I am writing to you from a {Adjective} castle in an enchanted forest.'
        f' I found myself here one day after going for a ride on a {Color} {Animal} in  {Place}. There are {Adjective2}'
        f'{Magical_Creature_plural} and {Adjective3} {Magical_Creature_Plural2} here! In the  {Room_house} there is'
        f'a pool full of {Noun}. I fall asleep each night on a {Noun2} of {Noun_Plural3} and dream of {Adjective4}'
        f'{Noun_Plural4}. It feels as though I have lived here for {Number} {Measure_of_time}. I hope one day you can'
        f'visit, although the only way to get here now is {Verb_ing}  on a {Adjective5} {Noun5} !!')

# Button.

Button(root, text='Hospital', font='arial 15', command=madlib1).place(x=100, y=130)
Button(root, text='Camping', font='arial 15', command=madlib2).place(x=100, y=180)
Button(root, text='Enchanted forest', font='arial 15', command=madlib3).place(x=70, y=230)

root.mainloop()
