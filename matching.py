'''
Name: Shashank Agrawal
Class: CS 5001
Program: Project
'''
import turtle
import traceback
import random
from card_class import *
import time
import os

#global variables
#Turtle to help set up game
setUpTurtle = turtle.Turtle()
setUpTurtle.speed(0)
#Turtle used as quit button
button = turtle.Turtle()
button.speed(0)
screen = turtle.Screen()
#Turtle to help write in status bar
statusBarTurtle = turtle.Turtle()
statusBarTurtle.speed(0)

class MatchingGame:   
    #name of player
    playerName = ""
    #number of total cards displayed
    numCards = -1    
    #holds number of guesses
    guesses = 0
    #holds number of matches
    matches = 0
    #holds image file names
    imagesList = []
    #holds the same index as xcod and ycod for each card drawn
    positionList = []
    #holds card objects
    cards = []    
    #centers of cards
    xcod = [-353, -190, -27, 143, -353, -190, -27, 143,
            -353, -190, -27, 143]
    ycod = [264, 264, 264, 264, 72, 72, 72, 72, -120,
            -120, -120, -120]
    #holds number of cards matched
    countMatched = 0
    #selected cards by user
    selectedObj1 = None
    selectedObj2 = None
    #x co-od of selectedObj1 to prevent matching with same card.
    xTemp = None
    #Index of x co-od of selectedObj1 to prevent matching with same card
    xIndex = None
    #default card images used if config file is missing
    default = ["2_of_diamonds.gif", "3_of_hearts.gif",
               "ace_of_diamonds.gif", "jack_of_spades.gif",
               "king_of_diamonds.gif", "queen_of_hearts.gif"]

    def hideAllCards(self):
        '''
        Function: hideAllCards
        Parameters: None
        Does: Hides all cards to display error message in form
            of .gif file to prevent error message from being
            displayed behind the card image (prevent overlapping).
        '''
        for i in self.cards:
            i.tuurtle.ht()        
   
    def quit(self, x, y):
        '''
        Function: quit
        Parameters:
                x (int): x co-od of mouse click
                y (int): y co-od of mouse click
        Does: If mouse click was on the turtle 'button',
            game is quit after displaying a quit message.
        '''
        button.ht()
        self.hideAllCards()
        screen.addshape("quitmsg.gif")
        button.shape("quitmsg.gif")
        button.goto(0, 0)
        button.st()
        time.sleep(1.1)
        turtle.bye()
        
    def drawPlayArea(self):
        '''
        Function: drawPlayarea
        Parameters: None
        Does: Marks the region within which cards are
            displayed.
        '''
        setUpTurtle.pensize(5)       
        setUpTurtle.penup()
        setUpTurtle.goto(-429, 360)
        setUpTurtle.pendown()
        setUpTurtle.goto(230,360)
        setUpTurtle.goto(230,-232)
        setUpTurtle.goto(-429,-232)
        setUpTurtle.goto(-429,360)

    def drawStatusBar(self):
        '''
        Function: drawStatusBar
        Parameters: None
        Does: Marks the region within which guesses
            and matches are displayed.
        '''
        setUpTurtle.penup()
        setUpTurtle.goto(-429, -267)
        setUpTurtle.pendown()
        setUpTurtle.goto(-429,-367)
        setUpTurtle.goto(230,-367)
        setUpTurtle.goto(230,-267)
        setUpTurtle.goto(-429,-267)

    def drawLeaderBoard(self):
        '''
        Function: drawLeaderBoard
        Parameters: None
        Does: Marks the region within which leaderboard
            and matches are displayed.
        '''
        setUpTurtle.penup()
        setUpTurtle.goto(250, 360)
        setUpTurtle.pendown()
        setUpTurtle.goto(443,360)
        setUpTurtle.goto(443,-232)
        setUpTurtle.goto(250,-232)
        setUpTurtle.goto(250,360)
        setUpTurtle.hideturtle()
        setUpTurtle.penup()

    def printLeaderBoard(self):
        '''
        Function: printLeaderBoard
        Parameters: None
        Does: Prints the leaderboard from leaderboard.txt
            in the area marked by drawLeaderBoard(). If
            leaderboard.txt is not available, a '.gif' file
            saying so is displayed on screen and program
            execution proceeds.
        '''
        try:
            file_obj =  file_obj = open("leaderboard.txt", 'r')
            lines = file_obj.readlines()
            setUpTurtle.goto(273, 316)
            setUpTurtle.pencolor("blue")
            FONT_SIZE = 12
            FONT = ('Arial', FONT_SIZE, 'bold')
            setUpTurtle.write("Leaders:", align='left', font = FONT)
            setUpTurtle.sety(266)

            for x in range(0, len(lines), 1):               
                setUpTurtle.write(str(x+1) + ". " + lines[x], align='left',
                                  font = FONT)                
                setUpTurtle.sety(setUpTurtle.ycor() - 30)
            
                            
        except OSError as err:              
                setUpTurtle.goto(0,0)
                screen.addshape("leaderboard_error.gif")
                setUpTurtle.shape("leaderboard_error.gif")
                setUpTurtle.st()
                time.sleep(1.1)
                setUpTurtle.ht()
            
        except Exception as e:
                traceback.print_exc()

        finally:
            setUpTurtle.penup()
            setUpTurtle.ht()

    def displayQuitButton(self):
        '''
        Function: displayQuitButton
        Parameters: None
        Does: Displays quit button that can be used anytime
            to quit the game.
            Note: quit button does not work when existing dialog
            boxes are present.
        '''
        CURSOR_SIZE = 20
        FONT_SIZE = 12
        FONT = ('Arial', FONT_SIZE, 'bold')
        button.hideturtle()
        screen.addshape("quitbutton.gif")
        button.shape("quitbutton.gif")
        button.shapesize(1, 2)
        button.penup()
        button.goto(346.5, -320)       
        button.onclick(self.quit)
        button.showturtle()       
    
    def __init__(self):
        '''
        Function: MatchingGame constructor
        Parameters: None            
        Returns: None
        Does: Uses setUpTurtle to draw play area,
            status bar area, and leaderboard area.
            Displays leaderboard, quit button and
            status bar on screen.
        '''
        self.drawPlayArea()
        self.drawStatusBar()      
        self.drawLeaderBoard()
        self.printLeaderBoard()
        self.displayQuitButton()         
        self.statusBar()

    def promptPlayerName(self):
        '''
        Function: promptPlayerName
        Parameters: None            
        Returns: None
        Does: Prompts user for name which is then stored
            under class varaible 'playerName'. Uses a dialog
            box. If no name is provided, name is defaulted to
            'Anonymous'
        '''
        try:
            self.playerName = screen.textinput("Set Up",
                                               "Enter Player Name")

        except AttributeError as e:            
                print("Dialog Box was closed. Player name is\
                      now Anonymous.")
                self.playerName = "Anonymous"

    def promptNumberOfCards(self):
        '''
        Function: promptNumberOfCards
        Parameters: None            
        Returns: None
        Does: Prompts user for number of cards to be displayed
            on the board. This value is then stored under class
            varaible 'numCards'. Uses a dialog box.
        '''
        cardPrompt = "Enter Number of Cards (8, 10 or 12)"
        flag = False
        
        while(flag == False):
            try:
                self.numCards = int(screen.numinput("Set Up", cardPrompt))
                if (self.numCards == 8 or self.numCards == 10 or
                    self.numCards == 12):                    
                    flag = True
                cardPrompt = "Not a valid number. Enter 8, 10 or 12"
                
            except TypeError as err:
                print("Type error: {0}".format(err))
                cardPrompt = "Missing number. Enter 8, 10 or 12"
                continue

    def displayErrorMessage(self):
            setUpTurtle.ht()
            setUpTurtle.goto(0, 0)
            screen.addshape("file_error.gif")
            setUpTurtle.shape("file_error.gif")
            setUpTurtle.st()
            time.sleep(1.1)
            setUpTurtle.ht()
        

    def promptImagesForCards(self):
        '''
        Function: promptImagesForCards
        Parameters: None            
        Returns: None
        Does: Prompts user for the name of the text file if custom cards
            are required using a dialog box. Card file names are then
            read from file and stored in a list, imagesList.
            If wrong file name or no file name is provided, default images
            from list, default, are used after displaying a '.gif' image on
            screen.
            Raises error for lesser number of images in file than number
            of cards provided by user.
            Raises error if image is not found while adding shape.
            Finally, these images are added to the screen for turtle
            to access. PositionList is initialized with a length of
            'len(self.imagesList) * 2'.
        '''
        filePrompt = "Enter File Name for Pictures (must end in .txt)"                       
        try:
            fileName = screen.textinput("Set Up", filePrompt)
            #error raised if no file name provided
            if fileName == None:
                raise OSError 
            file_obj = open(fileName, 'r')
            for i in range(0, self.numCards//2, 1):
                line = file_obj.readline().strip()
                #skip blank line
                if line == "":
                    continue
                self.imagesList.append(line)
            #raise error if not enough image names provided in file
            if(len(self.imagesList) != self.numCards//2):
                raise OSError
            file_obj.close()                            

        except OSError as err:            
            self.displayErrorMessage()
            #import default images if file not available
            self.imagesList = self.default[0:(self.numCards//2)]

        except Exception as e:
            traceback.print_exc()

        finally:
            self.positionList = [None] * len(self.imagesList) * 2
            try:
                for x in range(0, len(self.imagesList), 1):
                    screen.addshape(self.imagesList[x])
            except:
                self.displayErrorMessage()
                self.imagesList = self.default[0:(self.numCards//2)]
                for x in range(0, len(self.imagesList), 1):
                    screen.addshape(self.imagesList[x])
            screen.addshape("card_back.gif")
            screen.addshape("winner.gif")
            
    def setUpAndReadCards(self):
        '''
        Function: setUpAndReadCards
        Parameters: None            
        Returns: None
        Does: Uses setUpTurtle to draw play area,
            status bar area, and leaderboard area.
            Displays leaderboard, quit button and
            status bar on screen.
        '''       
        self.promptPlayerName()    
        self.promptNumberOfCards()
        self.promptImagesForCards()
    
    def statusBar(self):
        '''
        Function: statusBar
        Parameters: None            
        Returns: None
        Does: Displays current guesses and matches in status bar
            using a turtle (statusBarTurtle).
        ''' 
        status = "Guesses: " + str(self.guesses) + ", Matches: " + str(self.matches)          
        FONT_SIZE = 18
        FONT = ('Arial', FONT_SIZE, 'bold')
        statusBarTurtle.hideturtle()       
        statusBarTurtle.penup()
        statusBarTurtle.goto(-403, -323)
        statusBarTurtle.pencolor("blue")
        statusBarTurtle.write(status, align='left', font=FONT)        

    def getCardPositions(self):
        '''
        Function: getCardPositions
        Parameters: None            
        Returns: None
        Does: Assigns positions to image cards randomly using centers
            of cards as provided in xcod and ycod.
            Random variable's upper bound is 'len(self.imagesList) * 2 - 1'
            which can be 7, 9 or 11, denoting 8, 10 or 12 cards.
            The outer loop goes over imageList twice since we need two of
            each card.
            If a card is assigned a center, that value of the center is
            replaced by -1 so it can't be used again.            
            Since the board contains displays rows of 4 cards, the top left
            card is card 1, the one to its right is card 2 and so on. If one
            reached the right most card, numbering starts from the left most
            card of the next row.
            The index of each card in imagesList is stored in an array
            positionList depending on where it is placed on the board.
            Eg. If imageList is ["dog.gif", "dog2.gif", "dog3.gif", "dog4.gif"],
            an example of positionList could be [0, 1, 0, 2, 3, 3, 2, 1]
            This means dog.gif is card 1, dog2.gif is card 2, and so on.
            ''' 
        xcod_copy = self.xcod.copy()
        ycod_copy = self.ycod.copy()
        random_int = -1
        flag = False
        randomIntUpperBound = len(self.imagesList) * 2 - 1        

        for j in range(0, 2, 1):
            for i in range(0, len(self.imagesList), 1):

                while flag == False:
                    random_int = random.randint(0, randomIntUpperBound)
                    if ((xcod_copy[random_int] == -1) or (ycod_copy[random_int] == -1)):
                        continue
                    else:
                        flag = True                    
                        xcod_copy[random_int] = -1
                        ycod_copy[random_int] = -1                    
                 
                self.positionList[random_int] = i
                flag = False

    def allMatched(self):
        '''
        Function: allMatched
        Parameters: None            
        Returns:
            True: if all cards have been matched
            False: if all cards have not been matched
        Does: Returns True if all cards have been matched
            and False if all cards have not been matched
        ''' 
        if(self.countMatched == self.len(imagesList)):
            return True
        else:
            return False

    def getImagesList(self):
        '''
        Function: getImagesList
        Parameters: None            
        Returns:
            imagesList (list): List containing image files names
                used for card pictures
        Does: Getter function for imagesList.
        ''' 
        return self.imagesList

    def getGuessesAndMatches(self):
        '''
        Function: getGuessesAndMatches
        Parameters: None            
        Returns:
            String contains guesses and matches
        Does: Getter function for guesses and matches.
        ''' 
        return ("Guesses: ", self.guesses, ", Matches: ", self.matches)

    def getNumCards(self):
        '''
        Function: getNumCards
        Parameters: None            
        Returns:
            getNumCards (int): Number of cards displayed on the board.
        Does: Getter function for numCards.
        ''' 
        return self.numCards

    def getPositionList(self):
        '''
        Function: getPositionList
        Parameters: None            
        Returns:
            positionList (list): list containing positions of cards on the
                                board
        Does: Getter function for positionList.
        '''
        return self.positionList

    def drawCardObjects(self):
        '''
        Function: drawCardObjects
        Parameters: None            
        Returns: None
        Does: Draws cards on the board by initializing objects of class
            card_turtle. Draws all cards face down. Position of cards
            are from positionList.
            Objects are stored in list, cards.
        '''       
            
        for i in range(0, len(self.positionList), 1):
            x = self.xcod[i]
            y = self.ycod[i]
            image = self.imagesList[self.positionList[i]]
            obj = card_turtle(x, y, image, True)
            obj.draw()
            self.cards.append(obj)
    

    def goto(self, x, y):
        '''
        Function: goto
        Parameters:
            x (int): x co-od of center of card
            y (int): y co-od of center of card                
        Returns: None
        Does: Called upon mouse click on card.
            If no card selected, card clicked on is flipped. If clicked on again
            card is flipped again.
            If one card is selected, second card clicked on is flipped. If
            they match, centers of card are marked with value -2 in list
            xcod to prevent clicking on them again. Guesses and matches
            are updated. If all cards are matched, winning message is displayed
            and leaderboard is updated.
            If cards don't match, guesses is updated, cards are face down.           
        '''
        for i in range(0, len(self.cards), 1):            

            if(self.cards[i].contains(x, y)):
                if(self.xcod[i] == -2):
                    return
                
                if(self.xcod[i] == -1):                    
                    return
                
                if(self.selectedObj1 == None):                    
                    self.selectedObj1 = self.cards[i]
                    self.xTemp = self.xcod[i]                    
                    self.xIndex = i                    
                    self.xcod[i] = -1                    
                    self.cards[i].changeVisibility()
                    break
                
                elif(self.selectedObj1 != None and self.selectedObj2 == None):
                    self.selectedObj2 = self.cards[i]                    
                    self.cards[i].changeVisibility()
                    if (self.selectedObj1.image == self.selectedObj2.image):
                        self.xcod[self.xIndex] = -2                        
                        self.xcod[i] = -2                        
                        self.matches += 1
                        self.guesses += 1                        
                        self.selectedObj1 = None
                        self.selectedObj2 = None
                        statusBarTurtle.undo()
                        self.statusBar()
                        if(self.matches == (len(self.cards)//2)):
                            self.hideAllCards()
                            setUpTurtle.shape("winner.gif")
                            setUpTurtle.goto(0, 0)
                            setUpTurtle.st()
                            self.writeToFile()
                            time.sleep(0.8)
                            turtle.bye()
                    else:
                        self.xcod[self.xIndex] = self.xTemp
                        self.guesses += 1
                        time.sleep(0.8)
                        self.selectedObj1.changeVisibility()
                        self.selectedObj2.changeVisibility()                        
                        self.selectedObj1 = None
                        self.selectedObj2 = None
                        statusBarTurtle.undo()
                        self.statusBar()


    def writeToFile(self):
        '''
        Function: writeToFile
        Parameters: None                          
        Returns: None
        Does: Opens leaderboard.txt and updates it.
            If less than 8 scores are in the file, the file is appended
            with the most recent score.
            If 8 scores are present, each score is compared with the most
            recent score and the highest score is overwritten. If the most
            recent score is the highest score, nothing is overwritten.
        '''
        try:
            file_obj =  file_obj = open("leaderboard.txt", 'r')            
            lines = file_obj.readlines()

            if(len(lines) <= 7):
                file_obj.close()
                file_obj = open("leaderboard.txt", 'a')
                if(os.stat("leaderboard.txt").st_size == 0):
                    score = self.playerName + ": " + str(self.guesses)
                else:
                    score = "\n" + self.playerName + ": " + str(self.guesses)
                file_obj.write(score)

            else:
                highestGuess = self.guesses
                index = -1
                for x in lines:
                    guess = x.split()                    
                    if(int((guess[len(guess) -1])) > highestGuess):
                        highestGuess = int(guess[len(guess) -1])
                        index = lines.index(x)
                scores = ""               
                if(index == -1):
                    return
                for y in lines:                    
                    if(lines.index(y) == index):
                        continue
                    scores += y
                scores += "\n" + self.playerName + ": " + str(self.guesses)
                file_obj.close()
                file_obj =  file_obj = open("leaderboard.txt", 'w')
                file_obj.write(scores)
                
        except OSError as err:
                print("OS error: {0}".format(err))
                filePrompt = "Error loading file. Please enter a\
                            valid file ending in .txt"
            
        except Exception as e:
                traceback.print_exc()
    
        
def main():
    try:
        obj = MatchingGame()
        obj.setUpAndReadCards()
        obj.getCardPositions()
        obj.drawCardObjects()
        screen.onclick(obj.goto)

    except Exception as e:
        traceback.print_exc()

main()



    
