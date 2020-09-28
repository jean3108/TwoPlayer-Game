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
    def isOver(self):
        """
        Indicate if the game is over or not
        
        :return: True if the game is over else False
        :rtype: boolean
        """
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
        print(self.toKey())
        print("Start")
        while(stateGame.isOver()==False):
            if(self.maxPlayer==1):
                choice = function1(self)
            else:
                choice = function2(self)
            self.doChoice(choice)
            print(self.toKey())
        print("END")

        return self.calculateScore()
        
        