'''
Name: Shashank Agrawal
Class: CS 5001
Program: Project
'''
import turtle
import traceback
import random


class card_turtle:
    '''
    Class associated with each card drawn on
    the board. Each instance of this class
    is an individual turtle object
    '''
    #is card visible or not
    flipped = True
    #x co-od of center of card
    xvalue = 0
    #y co-od of center of card
    yvalue = 0
    #height of card
    height = 150
    #width of card
    width = 100
    #back
    back = "card_back.gif"
    #.gif image associated with card
    image = None
    #turtle object associated with card
    tuurtle = None

    def __init__(self, x, y, image, flipped):
        '''
        Function: card_turtle constructor
        Parameters:
            x (int): x co-od of center of card
            y (int): y co-od of center of card
            image (string): .gif image associated with card
            flipped (boolean): is card visible or not
        Returns: None
        Does: Creates a new turtle object, defines co-od for
            center of card, sets visibility for card and
            assigns image to card.
        '''
        self.tuurtle = turtle.Turtle()
        self.x = x
        self.y = y
        self.flipped = flipped
        self.image = image

    def changeVisibility(self):
        '''
        Function: changeVisibility
        Parameters: None
        Does: Changes the visibility of card.
            If card is visible, card is now hidden and
            vice versa.
        '''
        if(self.tuurtle.shape() == self.back):
            self.tuurtle.shape(self.image)
        else:
            self.tuurtle.shape(self.back)

    def hideCard(self):
        '''
        Function: hideCard
        Parameters: None
        Does: Hides card.
        '''
        self.tuurtle.ht()
        self.flipped = False

    def showCard(self):
        '''
        Function: hideCard
        Parameters: None
        Does: Shows card.
        '''
        self.tuurtle.st()
        self.flipped = True

    def contains(self, x, y):
        '''
        Function: contains
        Parameters:
                x (int): x co-od of mouse click
                y (int): y co-od of mouse click
        Does: Checks whether mouse click was within region
            of card. Use height and width of card to help
            do so.
        '''
        if(x <= self.x + 50 and x >= self.x - 50):
            if(y <= self.y + 75 and y >= self.y - 75):
                return True
        return False
        
    def draw(self):
        '''
        Function: draw
        Parameters: None
        Does: Draws card on the board with x and y
            co-od as its center and visibility as defined.
        '''
        self.tuurtle.speed(0)
        self.tuurtle.penup()
        self.tuurtle.shape(self.back)
        self.tuurtle.goto(self.x, self.y)
        if(self.flipped == False):
            self.hideCard()
        else:
            self.showCard()
        return self.tuurtle               
    
        
    
        
    






