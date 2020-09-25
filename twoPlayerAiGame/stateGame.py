class StateGame(ABC):         
    """
    Class wich represent a state of a two-player game
    """  
    @abstractmethod
    def __init__(self):
        """
        Create a state of the game.
        
        
        :return: The state with the choosen information
        :rtype: stateGame
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