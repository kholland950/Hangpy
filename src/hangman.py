#-------------------------------------------------
#HANGMAN
#By: Kevin Holland
#-------------------------------------------------

import random
from graphics import *
from Button import *

#----------------------------------------------------------
#fill dictionary with words
words = {"Easy":[],"Medium":[],"Hard":[],"Random":[]}

f = open('../words/easyWords.txt', 'r')
for line in f:
    words['Easy'].append(line[:-1])
f.close()
f = open('../words/medWords.txt', 'r')
for line in f:
    words['Medium'].append(line[:-1])
f.close()
f = open('../words/hardWords.txt', 'r')
for line in f:
    words['Hard'].append(line[:-1])
f.close()
f = open('../words/randomWords.txt', 'r')
for line in f:
    words['Random'].append(line[:-1])
f.close()

#----------------------------------------------------------

#draw body functions
def drawHead(win):
    head = Circle(Point(120, 95), 10)
    head.draw(win)

def drawTorso(win):
    torso = Line(Point(120,105), Point(120, 125))
    torso.draw(win)

def drawLeftArm(win):
    arm = Line(Point(120, 118), Point(105, 105))
    arm.draw(win)

def drawRightArm(win):
    arm = Line(Point(120, 118), Point(135, 105))
    arm.draw(win)

def drawLeftLeg(win):
    leg = Line(Point(120,125),Point(110,145))
    leg.draw(win)

def drawRightLeg(win):
    leg = Line(Point(120,125),Point(130,145))
    leg.draw(win)

#-----------------------------------------------------------
    
def chooseWord(mode):
    #chooses random word from mode of words dictionary
    return random.choice(words[mode])

#----------------------------------------------------------
    
def drawStand(win):
    #draws stand for stick person
    base = Line(Point(30,160), Point(100,160))
    base.draw(win)

    upL = Line(Point(65,160), Point(65,70))
    upL.draw(win)

    across = Line(Point(65,70), Point(120,70))
    across.draw(win)

    string = Line(Point(120,70), Point(120,85))
    string.draw(win)

    s1 = Line(Point(45,160), Point(65,140))
    s1.draw(win)

    s2 = Line(Point(85,160), Point(65,140))
    s2.draw(win)

#----------------------------------------------------------

def drawSpaces(num, win):
    #draws correct # of spaces each 2 pixels apart
    for i in range(num):
        Line(Point(30+(10*i)+2, 250), Point(40+(10*i), 250)).draw(win)

#----------------------------------------------------------

def findLetter(word, letter):
    #returns which spaces should reveal letters

    #return empty list if no letter passed
    if letter == '':
        return []
    
    count = []
    wordL = list(word)
    for i in range(len(wordL)):
        if wordL[i] == letter:
            count.append(i)
    return count

#----------------------------------------------------------

def showLetter(L, word, win):
    #use drawSpaces related formula to show letters
    #loop for multiple letter cases
    for i in L:
        Text(Point(30+(10*i) + 6, 244), word[i]).draw(win)

#----------------------------------------------------------
#old method for win calculation, do not use
'''def gameWordLength(word):
    count = 0
    prev = ''
    for i in word:
        if i != prev:
            count+=1
        prev = i
    if i!= prev:
        count+=1
    return count'''
#----------------------------------------------------------

def displayWord(notChosen, word, win):
    '''used at end of game, loops through list of unused letters
    and displays them in the appropriate spots using the
    findLetter and showLetter methods'''
    for i in notChosen:
        L = findLetter(word, i)
        showLetter(L, word, win)

#----------------------------------------------------------
        
def play():
    #draw window
    win = GraphWin("Hangman",300,300, autoflush = False)
    
    #close and play buttons , and opening text
    close = Button('Quit', Point(273, 5), Point(295, 18), win)
    PLAY = Button('PLAY!', Point(100,100), Point(200,200), win)
    PLAY.setTextSize(24)
    hangmanText = Text(Point(150,80), "Hangman!")
    hangmanText.setSize(22)
    hangmanText.setFill('blue')
    hangmanText.draw(win)

    #wait for play or close to be clicked
    p = win.getMouse()
    while not close.buttonClicked(p):
        if PLAY.buttonClicked(p):
            PLAY.hide()
            hangmanText.undraw()
            break
        p = win.getMouse()

    #make playAgain and restart buttons
    playAgain = Button('Play Again', Point(230,270), Point(290,290), win)
    playAgain.hide()
    restart = Button('Restart', Point(230,270), Point(290,290), win)
    restart.hide()

    #draw hangman stand
    drawStand(win)   

    #draw letter buttons
    a = Button('A', Point(30,19), Point(40,30), win)
    b = Button('B', Point(42,19), Point(52,30), win)
    c = Button('C', Point(54,19), Point(64,30), win)
    d = Button('D', Point(66,19), Point(76,30), win)
    e = Button('E', Point(78,19), Point(88,30), win)
    f = Button('F', Point(90,19), Point(100,30), win)
    g = Button('G', Point(102,19), Point(112,30), win)
    h = Button('H', Point(114,19), Point(124,30), win)
    i = Button('I', Point(126,19), Point(136,30), win)
    j = Button('J', Point(138,19), Point(148,30), win)
    k = Button('K', Point(150,19), Point(160,30), win)
    l = Button('L', Point(162,19), Point(172,30), win)
    m = Button('M', Point(174,19), Point(184,30), win)
    n = Button('N', Point(186,19), Point(196,30), win)
    o = Button('O', Point(198,19), Point(208,30), win)
    Lp = Button('P', Point(210,19), Point(220,30), win)
    q = Button('Q', Point(30,35), Point(40,45), win)
    r = Button('R', Point(42,35), Point(52,45), win)
    s = Button('S', Point(54,35), Point(64,45), win)
    t = Button('T', Point(66,35), Point(76,45), win)
    u = Button('U', Point(78,35), Point(88,45), win)
    v = Button('V', Point(90,35), Point(100,45), win)
    w = Button('W', Point(102,35), Point(112,45), win)
    x = Button('X', Point(114,35), Point(124,45), win)
    y = Button('Y', Point(126,35), Point(136,45), win)
    z = Button('Z', Point(138,35), Point(148,45), win)
        
    #draw difficulty buttons
    easy = Button('Easy', Point(230, 50), Point(280, 62), win)
    med = Button('Medium', Point(230,65), Point(280, 77), win)
    hard = Button('Hard', Point(230, 80), Point(280, 92), win)
    random = Button('Random', Point(230,95),Point(280,107),win)

    #define order for body drawing
    bodyOrder = ['head','torso','leftArm','rightArm','leftLeg','rightLeg']

    #START GAME LOOP
    while not close.buttonClicked(p):

        #select difficulty prompt
        selectDifficulty = Text(Point(170,60), 'Select difficulty >>>')
        selectDifficulty.draw(win)
        #CLICK LOOP REGIONvvvvvvvvvvvvv
        p = win.getMouse()
        #inf loop, difficulty selection (or close) breaks loop
        while 1==1:
            if easy.buttonClicked(p):
                mode = 'Easy'
                easy.deactivate()
                break
            elif med.buttonClicked(p):
                mode = 'Medium'
                med.deactivate()
                break
            elif hard.buttonClicked(p):
                mode = 'Hard'
                hard.deactivate()
                break
            elif random.buttonClicked(p):
                mode = 'Random'
                random.deactivate()
                break
            elif close.buttonClicked(p):
                win.close()
                return 0
            else:
                #if nothing clicked, get mouse
                p = win.getMouse()
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        #GAME STARTS HERE!!!

        #unhide restart button
        restart.unhide()

        #display current mode, undraw difficulty prompt
        modeT = Text(Point(230, 120), "Mode: " + mode)
        modeT.draw(win)
        selectDifficulty.undraw()

        #choose words, set spaces, get length
        word = chooseWord(mode)
        drawSpaces(len(word),win)
        length = len(word)

        '''vvv old length usage - out dated vvv'''
        #gLength = gameWordLength(word)
        #print(gLength)
        '''^^^ old length usage - out dated ^^^'''

        #set default letter, loseCount, winCount,
        #L for drawing list, and notChosenList
        letter = ''
        loseCount = 0
        winCount = 0
        L = ['0']
        notChosenList=['a','b','c','d','e','f','g','h','i','j','k','l','m',
                   'n','o','p','q','r','s','t','u','v','w','x','y','z']

        #CLICK LOOP REGIONvvvvvvvvvvvvvvvvvvv
        p = win.getMouse()
        while not close.buttonClicked(p):
            #if restart pressed, break back to game loop
            #if letter pressed, set letter
            if restart.buttonClicked(p):
                break
            if a.buttonClicked(p):
                a.deactivate()
                letter = 'a'
            elif b.buttonClicked(p):
                b.deactivate()
                letter = 'b'
            elif c.buttonClicked(p):
                c.deactivate()
                letter = 'c'
            elif d.buttonClicked(p):
                d.deactivate()
                letter = 'd'
            elif e.buttonClicked(p):
                e.deactivate()
                letter = 'e'
            elif f.buttonClicked(p):
                f.deactivate()
                letter = 'f'
            elif g.buttonClicked(p):
                g.deactivate()
                letter = 'g'
            elif h.buttonClicked(p):
                h.deactivate()
                letter = 'h'
            elif i.buttonClicked(p):
                i.deactivate()
                letter = 'i'
            elif j.buttonClicked(p):
                j.deactivate()
                letter = 'j'
            elif k.buttonClicked(p):
                k.deactivate()
                letter = 'k'
            elif l.buttonClicked(p):
                l.deactivate()
                letter = 'l'
            elif m.buttonClicked(p):
                m.deactivate()
                letter = 'm'
            elif n.buttonClicked(p):
                n.deactivate()
                letter = 'n'
            elif o.buttonClicked(p):
                o.deactivate()
                letter = 'o'
            elif Lp.buttonClicked(p):
                Lp.deactivate()
                letter = 'p'
            elif q.buttonClicked(p):
                q.deactivate()
                letter = 'q'
            elif r.buttonClicked(p):
                r.deactivate()
                letter = 'r'
            elif s.buttonClicked(p):
                s.deactivate()
                letter = 's'
            elif t.buttonClicked(p):
                t.deactivate()
                letter = 't'
            elif u.buttonClicked(p):
                u.deactivate()
                letter = 'u'
            elif v.buttonClicked(p):
                v.deactivate()
                letter = 'v'
            elif w.buttonClicked(p):
                w.deactivate()
                letter = 'w'
            elif x.buttonClicked(p):
                x.deactivate()
                letter = 'x'
            elif y.buttonClicked(p):
                y.deactivate()
                letter = 'y'
            elif z.buttonClicked(p):
                z.deactivate()
                letter = 'z'
            #no letter pressed
            else:
                letter = ''

            #if letter was pressed
            if letter != '':
                #find letter, show letter
                L = findLetter(word, letter)
                showLetter(L,word,win)
                '''if letter in word:
                    winCount+=1'''
                #set winCount -
                #if letter in word one or multiple times, sets accordingly
                for letters in word:
                    if letters == letter:
                        winCount+=1
                #if letter hasn't been used, remove from notChosenList
                if letter in notChosenList:
                    notChosenList.remove(letter)

            #L==[] when the letter is not in word
            #in this case, add to lose count, draw according body part
            if L == []:
                loseCount+=1
                body = bodyOrder[loseCount-1]

                if body == 'head':
                    drawHead(win)
                elif body == 'torso':
                    drawTorso(win)
                elif body == 'leftArm':
                    drawLeftArm(win)
                elif body == 'rightArm':
                    drawRightArm(win)
                elif body == 'leftLeg':
                    drawLeftLeg(win)
                elif body == 'rightLeg':
                    drawRightLeg(win)

            #WIN-------------------------!!!!!!!!!!!!!!!!!!!
            #v old winCount, do not use
            #if winCount == gLength:
            #^old winCount, do not use
            if winCount == length:
                #display large green text 'you win'
                winText = Text(Point(100,200), "YOU WIN!!!")
                winText.setFill('green')
                winText.setSize(22)
                winText.draw(win)
                #CLICK LOOP REGIONvvvvvv
                #play again or quit
                playAgain.unhide()
                while 1==1:
                    p = win.getMouse()
                    if playAgain.buttonClicked(p):
                        break
                    elif close.buttonClicked(p):
                        win.close()
                        return 0
                break
                #^^^^^^^^^^^^^^^^^^^^^^^^^^
                
            #LOSE------------------------!!!!!!!!!!!!!!!!!!
            #at loseCount == 6, all body parts drawn, you lose
            elif loseCount == 6:
                #display large red text 'you lose'
                loseText = Text(Point(100,200), "YOU LOSE")
                loseText.setFill('red')
                loseText.setSize(22)
                loseText.draw(win)
                displayWord(notChosenList,word,win)
                #CLICK LOOP REGIONvvvvvvvvvvvvvvv'
                #play again or quit
                playAgain.unhide()
                while 1==1:
                    p = win.getMouse()
                    if playAgain.buttonClicked(p):
                        break
                    elif close.buttonClicked(p):
                        win.close()
                        return 0
                #^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                break
            
            #no buttons clicked
            else:
                p = win.getMouse()
                L = [0]
                letter = ''
        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        #----------------------------------------------
        #RESET DISPLAY
        if winCount == length:
            winText.undraw()
        elif loseCount == 6:
            loseText.undraw()

        easy.activate()
        med.activate()
        hard.activate()
        random.activate()
        modeT.undraw()
        playAgain.hide()
        clearWord = Rectangle(Point(0,230),Point(300,250))
        clearWord.setFill('white')
        clearWord.setOutline('white')
        clearWord.draw(win)
        clearBody = Rectangle(Point(105,85),Point(135,145))
        clearBody.setFill('white')
        clearBody.setOutline('white')
        clearBody.draw(win)

        a.activate()
        b.activate()
        c.activate()
        d.activate()
        e.activate()
        f.activate()
        g.activate()
        h.activate()
        i.activate()
        j.activate()
        k.activate()
        l.activate()
        m.activate()
        n.activate()
        o.activate()
        Lp.activate()
        q.activate()
        r.activate()
        s.activate()
        t.activate()
        u.activate()
        v.activate()
        w.activate()
        x.activate()
        y.activate()
        z.activate()

        #RESET DISPLAY^^^
        #-----------------------------------------------------
        
    #close window at loop break
    win.close()
play()
