from abc import ABC, abstractmethod
from twoPlayerAiGame.aiAlgorithms import minmaxDecision, negamaxDecision, randomDecision, humanDecision

class StateGame(ABC):         
    """
    Class wich represent a state of a two-player game
    """  
    @abstractmethod
    def __init__(self, maxPlayer):
        """
        Create a state of the game.
        
        
        :return: The state with the choosen information
        :rtype: stateGame
        """
        self.maxPlayer = 1 if maxPlayer==True else -1
        pass
    

    @abstractmethod
    def calculateScore(self):
        """
        Calculate the score of the current state if it's a terminal state or estimate the score
        
        :return: The score of the current state
        :rtype: number
        """
        pass

    
    @abstractmethod
    def getChoices(self):
        """
        Get the different choice for the player for the current state.
        
        :return: Every choices that the player can make. 
        :rtype: list[object]
        """
        pass
    
    @abstractmethod
    def doChoice(self, inNewState = False):
        """
        Apply the choice to the current state (inplace or not)
        
        :param inNewState: To choose if the choice is apply inplace (on the current state) or not (on a copy of the current state)
        
        :type inNewState: boolean
        
        :return: Nothing if it's inplace then the new state.
        :rtype: stateGame or None
        """
        pass
    
    @abstractmethod
    def undoChoice(self, inNewState = False):
        """
        Undo the given choice for the current state (inplace or not)
        
        :param inNewState: To choose if the choice is apply inplace (on the current state) or not (on a copy of the current state)
        
        :type inNewState: boolean
        
        :return: Nothing if it's inplace then the new state.
        :rtype: stateGame or None
        """
        pass
    
    @abstractmethod
    def toKey(self):
        """
        Get the unique ID of the state.
        
        This ID is useful to use memoization in different algorithms
        
        :return: the ID of the current state
        :rtype: string
        """
        pass

    
    @abstractmethod
    def printBeforeGame(self):
        """
        Print information before the beginning of the game
        """
        pass
    
    @abstractmethod
    def printInfoPlayer(self):
        """
        Print information before the turn of the current player
        """
        pass
    
    @abstractmethod
    def printResultAction(self, choice):
        """
        Print information after the turn of the current player
        
        :param choice: The choice wich was just played
            
        :type choice: typeof(self.getChoices()[0])
        """
        pass
    
    @abstractmethod
    def printAfterGame(self):
        """
        Print information after the end of the game
        """
        pass
    
    def play(self, player1, player2, verbose=True):
        """
        Play the game
           
        :param player1: String to choose the algorithm for the choice of the player1 (can be human)
        :param player2: String to choose the algorithm for the choice of the player2 (can be human)
        :param verbose: Indicate if information are printed or not
            
        :type player1: String
        :type player2: String
        :type verbose: boolean

        :return: the number of the winner then 0
        :rtype: int
        """

        ####################################
        # Selection of algorithm & Setting #
        ####################################

        if(player1=='human'):
            function1 = humanDecision
        elif(player1=='minmax'):
            function1 = minmaxDecision
        elif(player1=='negamax'):
            function1 = negamaxDecision
        elif(player1=='random'):
            function1 = randomDecision

        if(player2=='human'):
            function2 = humanDecision
        elif(player2=='minmax'):
            function2 = minmaxDecision
        elif(player2=='negamax'):
            function2 = negamaxDecision
        elif(player2=='random'):
            function2 = randomDecision

        #########################
        # Beginning of the game #
        #########################

        over = False
        if(verbose==True):
            self.printBeforeGame()

        currentScore = self.calculateScore()
        while(currentScore==False):
            if(verbose==True):
                self.printInfoPlayer()
            if(self.maxPlayer==1):
                choice = function1(self)[1]
            else:
                choice = function2(self)[1]
            self.doChoice(choice)
            currentScore = self.calculateScore()
            if(verbose==True):
                self.printResultAction(choice)
        if(verbose==True):
            self.printAfterGame()

        return currentScore
        
        