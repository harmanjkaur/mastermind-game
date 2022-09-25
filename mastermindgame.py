# Mastermind Game
"""
Created on Mon Dec 13 13:55:46 2021

@author: harmanjot kaur
"""

from tkinter import *
import tkinter as tk
import random,os
from random import choices
import itertools as it
from tkinter import messagebox

  

# CREATING MASTERMIND GAME WINDOW-------------------------------------------------------------------------------------------------------------------------------


class MastermindGameMenu:
    
    def __init__(self,root):
        
        self.master=root
       
        self.master.geometry('780x650')     # Select the width and height of the menu window...
       
        self.master.config(bg='#dae8ec')
       
        self.gameStatus=self.read('GameStatus.txt',5)      # Save game status....
        
        self.MastermindGameMainMenu()



    # CREATING MASTERMIND MAIN MENU FUNCTION--------------------------------------------------------------------------------------------------------------------
    
    def MastermindGameMainMenu(self):
        
        self.clear() 
        
        self.label1 = tk.Label(self.master, text = "Mastermind Game",width=40, height=2,bg='#bed2d5',font='Arial 15 bold' )          # Title lebel...

        self.label1.pack(side = "top", pady=10)
        
        self.label1 = tk.Label(self.master, text = "Welcome ...!",width=25, height=2,font='Arial 13 bold' )                            

        self.label1.pack(side = "top", pady=10)

                
        self.button1=tk.Button(self.master,text='Play Mastermind Game', width=20, height=2,bg='#bbbbbb',font='Serif 13 italic')     # Create a play game button...
        
        self.button2=tk.Button(self.master,text='Save Status Game', width=20, height=2,bg='#bbbbbb',font='Serif 13 italic')         # Create a save status game button...
        
        self.button3=tk.Button(self.master,text='Close Game', width=20, height=2,bg='#bbbbbb',font='Serif 13 italic')              # Create a quit game button...
       
        # Pack buttons
        
        self.button1.pack(pady=40)
        self.button2.pack(pady=40)
        self.button3.pack(pady=40)
              
        # Bind buttons
        
        self.button1.bind('<Button-1>',lambda i:self.specs())
        self.button2.bind('<Button-1>',self.loading_function)
        self.button3.bind('<Button-1>',lambda i:exit())


    # CREATING CLEAR FUNCTION ----------------------------------------------------------------------------------------------------------------------------------
    
    def clear(self):
        list_retun_widget= self.master.slaves()         # This function return a list of all the widgets....
        
        for l in list_retun_widget:                     
            l.destroy()                                 # Destroy method.....

   
    # CREATING REQUIREMENT FOR GAME-----------------------------------------------------------------------------------------------------------------------------
    
    def specs(self):
        
        self.clear()
        
        self.label1 = tk.Label(self.master, text = "Mastermind Game",width=40, height=2,bg='#bed2d5',font='Arial 15 bold' )          # Title label....

        self.label1.pack(side = "top", pady=10)
        
        self.label1 = tk.Label(self.master, text = "Game Requirements",width=35, height=2,font='Arial 13 bold' )                     # Requirement label

        self.label1.pack(side = "top", pady=20)

        # frame one...
        
        self.frame1=tk.Frame(self.master,bg='#dae8ec')
        self.frame1.pack()
        
        # frame two...
        
        self.frame2=tk.Frame(self.master,bg='#dae8ec')
        self.frame2.pack()
        
        # frame three...
        
        self.frame3=tk.Frame(self.master,bg='#dae8ec')
        self.frame3.pack()

       
        
        #Column selection options here--------------------------------------------------------------------------------------------------------------------------
    
        self.coLab=tk.Label(self.frame1,text='Choose Game Columns',bg='#dae8ec',font='Centaur 13')    # Column label..... 
        self.coLab.grid(row=0,column=0,pady=20)            
        self.cols=['4','6','8']                                                                       # This option work for accessing columns according to given numbers....
        self.col = StringVar() 
        self.col.set(self.cols[0])  
            
        self.dropCol = tk.OptionMenu( self.frame1 , self.col , *self.cols)                            # Option menu and this will select number of columns...
        self.dropCol.config(width=30)  
        self.dropCol.grid(row=0,column=1,pady=20)   

     
        # Row selection options here----------------------------------------------------------------------------------------------------------------------------
        
        self.roLab=tk.Label(self.frame2,text='Choose Game Rows',bg='#dae8ec',font='Centaur  13')       # Row label..... 
        self.roLab.grid(row=0,column=0,pady=20)
        self.ros=[str(i) for i in range(10,14)]                                                        # Using for loop to access rows from minimum 10 and maximum.....
        self.rowS = StringVar()
        self.rowS.set(self.ros[-1])
        
        self.dropRow = tk.OptionMenu( self.frame2 , self.rowS , *self.ros)                             # Option menu and this will select number of rows...
        self.dropRow.config(width=30)
        self.dropRow.grid(row=0,column=1,pady=20)

   
       # Game selection options here----------------------------------------------------------------------------------------------------------------------------
       
        self.typLab=tk.Label(self.frame3,text='Choose Game Type',bg='#dae8ec',font='Centaur  13')       # Game option label shows game types....
        self.typLab.grid(row=0,column=0,pady=20)
        self.typ=['Human Player vs Computer Player','Computer Player vs Computer Player']               # This option display full name of types of game...
        self.typShort=['HvC','CvC']                                                                     # This option display short name of types of game...
        
        self.dictionary=dict(zip(self.typ,self.typShort))                                               # Creating a dictionary....
        self.gType = StringVar()    
        self.gType.set(self.typ[0])
        
        self.gam = tk.OptionMenu( self.frame3 , self.gType , *self.typ )                                # Option menu and this function will select type of game... 
        self.gam.config(width=30)
        self.gam.grid(row=0,column=1,pady=20)


        # Game run button----------------------------------------------------------------------------------------------------------------------------------------
        
        self.runbutton=tk.Button(self.master,text='Run Mastermind Game',width=30,height=2,bg='#bbbbbb',font='Centaur  13')            # Creating a run button....
       
        self.runbutton.pack(pady=30)                                                                                                  # Pack button 
       
        self.runbutton.bind('<Button-1>',lambda x:self.start(int(self.col.get()),int(self.rowS.get()),self.dictionary[self.gType.get()]))     # Binding button....



    # CREATING START GAME FUNCTION------------------------------------------------------------------------------------------------------------------------------
    
    def start(self,holes,guesses,typ,load=None):
        
        self.clear()    
        
        self.label1 = tk.Label(self.master, text = "Mastermind Game",width=40, height=2,bg='#bed2d5',font='Arial 15 bold' )          # Title of game....

        self.label1.pack(side = "top", pady=10)
        
        self.x=Mastermind(self.master,self,self.gameStatus,holes=holes,guesses=guesses,typ=typ,load=load)        # Creating a mastermind Game frame window here...
        
        self.x.pack()                                                                                            #packing frame...
        
        self.x.mastermind_gui()                                                                                  #Showing graphic interface of the mastermind game....

    
    # CREATING LOADING FUNCTION---------------------------------------------------------------------------------------------------------------------------------
    
    def loading_function(self,event): 
        
        self.clear()
        
        self.label1 = tk.Label(self.master, text = "Mastermind Game",width=40, height=2,bg='#bed2d5',font='Arial 15 bold' )          # Title of game....

        self.label1.pack(side = "top", pady=10)
        
        self.names=['Save '+str(i) for i in range(5)]                                                               # Using for loop here and this will display save file names.....
        
        self.SaveLabs=[tk.Button(self.master,text=name,width=30,height=1,bg='#dac5bc', font='Centaur 15 bold') for name in self.names]                   #labels for save files
        
        for widg in self.SaveLabs:                                                                                   # This will show all labels....
            widg.pack(pady=30)
        
        # Binding the labels....
        
        self.SaveLabs[0].bind('<Button-1>',lambda x:self.starting_function(0))        
        self.SaveLabs[1].bind('<Button-1>',lambda x:self.starting_function(1))
        self.SaveLabs[2].bind('<Button-1>',lambda x:self.starting_function(2))
        self.SaveLabs[3].bind('<Button-1>',lambda x:self.starting_function(3))
        self.SaveLabs[4].bind('<Button-1>',lambda x:self.starting_function(4))

    
    # CREATE STARTING FUNCTION----------------------------------------------------------------------------------------------------------------------------------
    
    def starting_function(self,ind):
        
        if self.gameStatus[ind][0]=='1':     
            
            self.clear()
            
            self.data=self.read("Saves\\Save "+str(ind)+'.txt',4)       # Calling the read file function here....
            
            self.LoadedData=self.split_data_function()                  # This option work as to converting the data in a form that the game can recognise...... 
            
            self.start(*self.LoadedData[0],'HvC',load=self.LoadedData)          
   
        else:                                                                        # If above statement is not working then this else statement will work......
        
            messagebox.showinfo('Sorry!','There is no any save file availabe.')      # Display this message if save status game is zero.....
            
   
    # CREATE SPLIT DATA FUNCTION TO DISTINGUISH THE DATA--------------------------------------------------------------------------------------------------------
    
    def split_data_function(self):
        
        a=[[] for i in range(4)]                                                     # This will display four rows for each single save game file.....
        
        RCtup=self.data[0].split(',')                                                
        
        a[0]=[int(RCtup[0]),int(RCtup[1])]                                           # This will convert the first value according to the available range of rows and columns....
        
        a[1]=int(self.data[1])  
       
        hlp=self.data[2].split(',')
        
       
        outLis=[]     
        
        for i in range(0,len(hlp),a[0][0]):                                          # This list is used for size and many time as number of colors in this list....
        
            inLis=[]                                                                 # This is empty list...........
            
            for j in range(a[0][0]):                                                 # This for loop repeat several times because there are number of game columns..... 
            
                inLis.append(hlp[j+i])    
                
            outLis.append(inLis)
            
        a[2]=outLis
        
        hlp=self.data[3].split(',')
        
        a[3]=hlp    
     
        return a

   
    # CREATING READ FUNCTION-----------------------------------------------------------------------------------------------------------------------------------
    
    def read(self,directory,x):
        
        maz=open(directory,'r')                                                 # This maz variable open file direrctory path in read format.........
        
        a=[]    
        
        for i in range(x):                                                      # Using for loop and it will repeat several times here....
        
            c=maz.readline()                                                    # This option work as read the data....
            
            c=c.rstrip('\n')    
            
            a.append(c)                                                         # Append method
            
        maz.close()
        
        return a    
    
  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# CREATING MASTERMIND GAME CLASSS-------------------------------------------------------------------------------------------------------------------------------

class Mastermind(tk.Frame):

    def __init__(self, master,parent, gameStatus, holes=4, guesses=10, colours=8, typ='HvC',load=None, bg="white", fg="black", **kwargs):
        
        self.parent=parent                                                         # Parent window here....
                        
        self.numberOfHoles = holes    
                    
        self.numberOfGuesses = guesses  
        
        self.numberOfColours = colours  
        
        self.gameType=typ  
        
        self.load=load  
        
        self.GameStatus=gameStatus                                                  # Save status game list work like if game is saved then it will display in save files otherwise will not display in the save files....
        
        self.backtohumanplayer=True                                                  # This option for go back to player....
        
        self.time=2000                                                               # Giving 2 seconds time to play game by computer 
        
        if self.load!=None:                                                          # If statement work here like if save data is not empty...... 
                 
            self.backtohumanplayer=False                                             #Game is loaded then backtohumanplayer will be false until all data has not been loaded
            self.time=10
            
        self.steps=0                                                                 # Starting value 0
        self.step=random.choice([i for i in range(self.numberOfGuesses)])   
        
        self.bg = bg                                        
        
        self.fg = fg                                      
        
        self.clr2save=[]
        self.master = master
        self.colours = ["#9E5D00", "#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#FF00FF", "#8C44FF", "#FFFFFF", "#000000"][:self.numberOfColours]         # Colours range code here....
        
        self.cLis={"#9E5D00":'brown', "#FF0000":'red', "#FF7F00":'orange', "#FFFF00":'yellow', 
                "#00FF00":'green',"#0000FF":'blue', "#FF00FF":'pink', "#8C44FF":'purple'}
        '''for i in self.colours:
            tk.Label(root,text=i,bg=i).pack()'''
            
        self.combination=self.color_combination(self.colours, self.numberOfHoles)
        
        self.reset_cycles()
        
        self.answer = random.sample(self.colours, k=self.numberOfHoles)                              # Computer player can select a random colors...
        
        if self.load != None:   
            self.answer=self.load[3]    
        super().__init__(self.master, bg=self.bg, **kwargs)                                          #Initialization of the super tk.Frame class
        for i in self.answer:                                                                        # Displaying answer colors 
            print(self.cLis[i]+' ',end='')
        self.clrSelect=self.colours[0]                                                               # Before starting the game, one colour will be slected



   
    # CREATING GRAPHICS GUI FUNCTION----------------------------------------------------------------------------------------------------------------------------
    def mastermind_gui(self):

       
        # Creating labels....
        
        self.allGuesses = [tk.Frame(self, bg=self.bg) for _ in range(self.numberOfGuesses)]
        self.allMarks = [tk.Frame(self, bg=self.bg) for _ in range(self.numberOfGuesses)]
        self.answerFrame = tk.Frame(self, bg=self.bg)
        self.answerCover = tk.Frame(self, bg=self.fg, relief=tk.RAISED) 
        
        self.allGuessPins = [[tk.Label(self.allGuesses[i], width=6, height=1, bg="#ccc2c7", relief=tk.GROOVE)   # This label work as player can filled the positions with given colors....
                             for _ in range(self.numberOfHoles)]
                             for i in range(self.numberOfGuesses)]
        

        self.allMarkPins = [[tk.Label(self.allMarks[i], width=4, height=1, bg="#9a9392", relief=tk.RIDGE)     # This label work automatically like red color means a right color at right position and white color means a right color but at wrong position....
                             for _ in range(self.numberOfHoles)]
                             for i in range(self.numberOfGuesses)]
        
        
        self.answerPins = [tk.Label(self.answerFrame, width=5, height=1, bg=colour, relief=tk.RAISED) for colour in self.answer]                    # This is the correct color position answer box which display on the top of main window in black colour....
        self.guessbutton= tk.Button(self, text="Click for colour guess", command=self.color_guess, bg=self.bg, fg=self.fg,font='Miriam 10')
        
        self.activeGuess = 0    
        
        
        # Rows and columns for the game is empty in beginning and each player can fill colors from given colours at the bottom...
        
        for rowIndex in range(self.numberOfGuesses):
            for holeIndex in range(self.numberOfHoles):
                
                self.allGuessPins[rowIndex][holeIndex].grid(row=0, column=holeIndex, padx=1, pady=4)
                self.allMarkPins[rowIndex][holeIndex].grid(row=0, column=holeIndex, padx=1, pady=4)
                
            tk.Label(self, text=str(rowIndex+1), bg=self.bg, fg=self.fg).grid(row=self.numberOfGuesses-rowIndex, column=0)   # This label will show row indexes....
            
            self.allGuesses[rowIndex].grid(row=rowIndex+1, column=1)
            self.allMarks[rowIndex].grid(row=rowIndex+1, column=3)

       
        for i, a in enumerate(self.answerPins):
            a.grid(row=0, column=i, padx=1)

        #These two label give space...
        tk.Label(self, text="Answer Colour Bar ", bg=self.bg,font='Miriam  11').grid(row=0, column=2)
        tk.Label(self, text="   ", bg=self.bg).grid(row=0, column=4)

     
        for a in [tk.Label(self.answerCover, width=6, height=1, bg=self.fg) for _ in range(self.numberOfHoles)]:     # This will show hidden correct answer color positions.... 
            a.pack(side=tk.LEFT, padx=1)


       
        self.answerCover.grid(row=0, column=1, pady=20)         # Black row at the top hide answers...
        
        self.guessbutton.grid(column=1, row=999, pady=10)
        
        if self.gameType=='HvC':                                # If player choose game type is human vs computer...
            self.color_guess(start=True)
            
        elif self.gameType=='CvC':                              # If player choose game type is computer vs computer...
            self.color_guess(start=True)

        self.colrFram=tk.Frame(self)
        self.colrFram.grid(row=1000, column=0,columnspan=5,sticky='WE')
        
        selectFram=tk.Frame(self)
        selectFram.grid(row=1001, column=0,columnspan=2,pady=4,sticky='WE')
        
        self.selctLab=tk.Label(selectFram,text='Choosen Colour',anchor='w',font='Miriam  10')
        self.selectClrLab=tk.Label(selectFram,width=4,height=1,relief=tk.SUNKEN,bg=self.clrSelect)
        
        
        
        # DISPLAY GIVEN COLORS----------------------------------------------------------------------------------------------------------------------------------
        
        self.labLis=[]
        colN=0
        col=0
      
        for colr in self.colours:                                                   # Player can access the colors and use in the game.....
            ro=1
            if colN%1==0:      
                ro=0
            lab=tk.Label(self.colrFram, width=3, height=2, bg=colr, relief=tk.RIDGE, anchor="w")               
            lab.grid(row=ro,column=col)
            self.labLis.append(lab) 
            colN+=1
            col+=1

        
        for i, pin in enumerate(self.labLis):      
            pin.bind("<1>", lambda event, i=i: self.change_choosen_color(event, i))
            pin["cursor"] = "arrow"                                                       #The arrow shape of the cursor will be displayed by this  # Cursor will display through this command....
        self.selctLab.grid(row=0,column=0)
        self.selectClrLab.grid(row=0,column=1)
        
       
        
        # NEW GAME BUTTON--------------------------------------------------------------------------------------------------------------------------------------
        
        self.savs=['Save '+str(i) for i in range(5)]
        self.sav = StringVar()
        self.sav.set(self.savs[0])
        self.dropSav = tk.OptionMenu( self , self.sav , *self.savs)                        # Option menu to display all files and player can save file anywhere.......
        self.dropSav.grid(row=999,column=3,pady=10)

        
        self.NewButton=tk.Button(self,text='New Game',width=17,bg='#bbbbbb',font='Miriam  10',command=lambda:self.parent.__init__(self.master))                 # Create a new game button...
        self.NewButton.grid(row=1000,column=3)
        self.Save=tk.Button(self,text='Save Game',width=17,bg='#bbbbbb',font='Miriam  10')                                                                      # Save game button...
        self.Save.grid(row=1001,column=3)
        self.Save.bind('<Button-1>',lambda x:self.save_game_function())                     # Call the save function....

  
    # CREATING COLOR COMBINATION FUNCTION-------------------------------------------------------------------------------------------------------------------------------
    
    def color_combination(self,lst, n):  
        if n == 0:
            return [[]]
        
        l =[]                                                             # Shows all combinations for computer versus computer game.....
        for i in range(0, len(lst)):                                      # Loop will repeat several times based on the selection of colors.......
            
            m = lst[i]
            remLst = lst[i + 1:]
            
            for p in self.color_combination(remLst, n-1):                  # This loop will run to number of combinations.....
                l.append([m]+p)
                
        return l                                                           # Return method use to return color combination.....

  
    # CREATE FUNCTION GUESS (PLAYER OR COMPUTER)----------------------------------------------------------------------------------------------------------------
    
    def color_guess(self, start=False):
      
        for colour in self.getting_colors_pin():
            if colour == "grey" and not start:
                return None

        self.reset_cycles()                                          
        self.allGuesses[self.activeGuess].config(bg=self.bg)            # Change color of guess labels.....
       
        for pin in self.allGuessPins[self.activeGuess]:
            pin.unbind("<1>")                        # Unbind buttons.....
            pin["cursor"] = ""

       
        score = self.score_guess(self.getting_colors_pin(), self.answer)                 # Pin for the guess.........
      
        if not start and len(score) != 0:
            score = self.score_guess(self.getting_colors_pin(), self.answer)
            self.clr2save.append(self.getting_colors_pin())                              # Appended to clr2sav list to save game.......       

            score.sort(reverse=True)                                                     # Sort guesss reverse......
            for i, pin in enumerate(self.allMarkPins[self.activeGuess]):    
                if i > len(score)-1:                  
                    break
                if score[i]==0:                                                          # if no match color guess then this statement will work.....
                    continue
                elif score[i]==1:                                                        #  Elif statement work like right color but on wrong position....
                    pin.config(bg='White', relief=tk.RAISED)
                elif score[i]==2:                                                         # Color match and also on right position....
                    pin.config(bg='Red', relief=tk.RAISED)

       
        
        # This statement run to check for a win.......
        
        if score == [2 for _ in range(self.numberOfHoles)]:                     # If every color guess match and on right position, then it will show red color and the runner will win....
        
            self.answerCover.grid_forget()                                          
        
            self.answerFrame.grid(row=0, column=1, pady=15)                      # Showing right color answers....
            
            self.guessbutton["command"] = None
            
            messagebox.showinfo("displaymeassage", "Congratulation! You are the Master Mind of this game.....")                              # Display this win message on screen if runner win the game....
            
            return None


            
        
        self.lis=[i-1 for i in range(self.numberOfGuesses,0,-1)]
        
        if self.lis[self.activeGuess]<self.numberOfGuesses:
            
            if self.gameType=='HvC' and self.backtohumanplayer:
                self.activeGuess -= 1
                self.allGuesses[self.activeGuess].config(bg=self.fg)                     # Change color of position....
                
                for i, pin in enumerate(self.allGuessPins[self.activeGuess]):      
                
                    pin.bind("<1>", lambda event, i=i: self.change_colors_pin(event, i))     # Bind and pins rows...
                     
                    pin["cursor"] = "arrow"                                                  # Display arrow to fill colors on labels....
                    
            else:
                
                if self.backtohumanplayer:                                                   # This if statement work if player or computer turn....
                
                    self.compGuess=random.choice(self.combination)                           # Random color guess if its computer turn......
                    
                    if self.step==self.steps and self.steps!=0:                              # If color guesses are right on right positions then computer will win the game....
                    
                        self.compGuess=self.answer
                        
                else:
                    
                    if len(self.load[2])==0:  
                        self.activeGuess=self.load[1]
                        self.backtohumanplayer=True
                        
                    print(self.load[2])
                    
                    
                    if len(self.load[2])!=0:
                        self.compGuess=self.load[2].pop(0)
                        
                   
                self.count=0                                                        # Using count here to know how many times computer fill colors in the labels....
                self.activeGuess-=1                                                 # Active guess-=1 means reverse order (-1,-2,-3....).....
                self.steps+=1
                self.allGuesses[self.activeGuess].config(bg=self.fg)                #Change the color of labels.....
                self.computer_play()                                                # Calling computer play function....

        else:
            self.answerCover.grid_forget()                                                                     
            self.answerFrame.grid(row=0, column=1, pady=15)
            self.guessbutton["command"] = None
            messagebox.showinfo("displaymessage", "Game is over...")                # Display message on the screen.....
            self.parent.clear()                                                     # Clear function calling.....
            self.parent.MainMenu()                                                  # Main menu game function calling..............
            return None


    # CREATING GAME SAVE FUNCTION---------------------------------------------------------------------------------------------------------------
    
    def save_game_function(self):
        
        nam=self.sav.get()                                                          # Get the game data to save in files....
        lists=self.save_data_function()                                             # Convert into list format...... 
        lisSavable=self.convert_to_save_format(lists)                               # Convert to save format............
        
        self.update_to_textfile(lisSavable,'Saves\\'+nam+'.txt')                    # Save to text function calling.....
        self.GameStatus[int(nam[-1])]='1'
        self.update_to_textfile(self.GameStatus, 'GameStatus.txt')                  # Save status of game......

   
    # CREATING DATA SAVE FUNCTION-------------------------------------------------------------------------------------------------------------
    
    def save_data_function(self):
        
        lis=[[self.numberOfHoles,self.numberOfGuesses],self.activeGuess,self.clr2save,self.answer]                       # Creating list........
        
        return lis

   
    # CREATING FUNCTION TO CONVERT GAME DATA TO SAVEABLE FORMAT-------------------------------------------------------------------------------
    
    def convert_to_save_format(self,lists):
        
        data=[[] for i in range(4)]
        data[0]=','.join([str(lists[0][0]),str(lists[0][0])])                    # First line will include rows and columns
        data[1]=str(lists[1]+1) 
        outLis=[]
        for i in lists[2]:
            for j in i:
                outLis.append(j)
        data[2]=','.join(outLis)
        data[3]=','.join(lists[3])  
        return data


  
    # CREATING FUNCTION TO SEND TEXT FILE-----------------------------------------------------------------------------------------------------
    
    def update_to_textfile(self,lists,directory):
        
        nam=open(directory,'w')              # Open file direrctory path in write format.........          
        nam.close()                                                                
        nam=open(directory,'a')              
        for i in range(len(lists)):               # Loop will work as four times....              
            argument=lists[i]+'\n'  
            nam.write(argument)
        nam.close()                                            # Close file method.........                           

   
    # CREATING COMPUTER PLAY FUNCTION---------------------------------------------------------------------------------------------------------
    
    def computer_play(self):
        
        pin=self.allGuessPins[self.activeGuess] 
        if self.count<len(self.compGuess):                                       # If statement check computer moves in the game.....
            self.clrSelect=self.compGuess[self.count]                            
            pin[self.count].config(bg=self.clrSelect, relief=tk.RAISED) 
            self.count+=1                                                         # Update count ................
            self.master.after(self.time,self.computer_play)            
        else:
            self.color_guess()                                                    # This else statement work to check the number of columns are equal to count............

    # Using static method........................
    
    @staticmethod
    def score_guess(guess, answer):
        
        cLis={"#9E5D00":'brown', "#FF0000":'red', "#FF7F00":'orange', "#FFFF00":'yellow', 
                "#00FF00":'green',"#0000FF":'blue', "#FF00FF":'pink', "#8C44FF":'purple','grey':'grey'}
        
        answer = answer.copy()
        
        reds = [2 if secret == guess_item else 0 for secret, guess_item in zip(answer, guess)]
        whites = []
        
        for guess_item in guess:
           
            if guess_item in answer:
                
                answer[answer.index(guess_item)] = None
                whites.append(1)
            else: 
                whites.append(0)
       
        score=[0 for i in range(len(reds))]
        for i in range(len(reds)):
            if reds[i]!=2:
                score[i]=reds[i]+whites[i]
            else:
                score[i]=reds[i]
       
        return score
    


    def getting_colors_pin(self):
        return [pin["bg"] for pin in self.allGuessPins[self.activeGuess]]       # Getting the pin colour...

    def change_colors_pin(self, event, i):
        event.widget.config(bg=self.clrSelect, relief=tk.RAISED)                # Raised method used for raise the box when pin is coloured...  
        
    def change_choosen_color(self, event, i):
        ind=i
        self.clrSelect=self.colours[ind]                                         # Getting given colours from bottom...
        self.selectClrLab.config(bg=self.clrSelect, relief=tk.SUNKEN)            # Updating the label showing selected color

    def reset_cycles(self):
        self.colourCycles = it.tee(it.cycle(self.colours), self.numberOfHoles)    



if __name__ == "__main__":
    root = tk.Tk()                                 # Creating a window with name root
    root.title("Mastermind Game")                       
    mastermindgamemenu=MastermindGameMenu(root)     # Creating an object of class Menu                 
    root.mainloop()                 