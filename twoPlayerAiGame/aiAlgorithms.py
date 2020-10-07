import numpy as np

states = {}

################
# Human Choice #
################

def humanDecision(state, verbose=False):
    """
    Function to make a human choice
    
    :param state: The state of the game on wich we want to get the best choice and score.
    
    :type state: StateGame
    
    :return: Return a 2-tuple with 0 and the choice
    :rtype: 2-tuple(0, typeof(state.getChoices()[0]))
    """

    choices = state.getChoices()
    choice = choices[int(input())-1]
    return 0, choice

##################################
# Algorithms without memoization #
##################################
def randomDecision(state):
    """
    Implementation of random algorithm
    
    :param state: The state of the game on wich we want to get the best choice and score.
    
    :type state: StateGame
    
    :return: Return a 2-tuple with the score and the best choice to make
    :rtype: 2-tuple(typeof(state.calculScore()), typeof(state.getChoices()[0]))
    """
    return 0, np.random.choice(state.getChoices())

def minmaxDecisionWithoutMemoization(state):
    """
    Implementation of MinMax algorithm without memoization
    
    :param state: The state of the game on wich we want to get the best choice and score.
    
    :type state: StateGame
    
    :return: Return a 2-tuple with the score and the best choice to make
    :rtype: 2-tuple(typeof(state.calculScore()), typeof(state.getChoices()[0]))
    """
    
    score = state.calculateScore()
    
    # Terminal Node
    if(type(score) is bool and score == False):
        return score, None
    
    choices = state.getChoices()
    
    #MAX player
    if(state.maxPlayer == 1): 
        score = -np.inf
        bestChoice = None
        for choice in choices:
            state.doChoice(choice)
            newScore, newChoice = minmaxDecision(state)
            if(newScore > score):
                score = newScore
                bestChoice = choice
            state.undoChoice(choice)
        return score, bestChoice
    
    #MIN player
    else: 
        score = np.inf
        bestChoice = None
        for choice in choices:
            state.doChoice(choice)
            newScore, newChoice = minmaxDecision(state)
            if(newScore < score):
                score = newScore
                bestChoice = choice
            state.undoChoice(choice)
        return score, bestChoice


def negamaxDecisionWithoutMemoization(state):
    """
    Implementation of Negamax algorithm without memoization
    
    :param state: The state of the game on wich we want to get the best choice and score.
    
    :type state: StateGame
    
    :return: Return a 2-tuple with the score and the best choice to make
    :rtype: 2-tuple(typeof(state.calculScore()), typeof(state.getChoices()[0]))
    """
    score = state.calculateScore()
    
    # Terminal Node
    if(type(score) is bool and score == False):
        return score*state.maxPlayer, None
    
    score = -np.inf
    bestChoice = None
    choices = state.getChoices()
    for choice in choices:
        state.doChoice(choice)
        newScore, newChoice = negamaxDecision(state)
        newScore *= -1
        if(newScore > score):
            score = newScore
            bestChoice = choice
        state.undoChoice(choice)
    return score, bestChoice


###############################
# Algorithms with memoization #
###############################


def minmaxDecision(state):
    """
    Implementation of MinMax algorithm with memoization
    
    :param state: The state of the game on wich we want to get the best choice and score.
    
    :type state: StateGame
    
    :return: Return a 2-tuple with the score and the best choice to make
    :rtype: 2-tuple(typeof(state.calculScore()), typeof(state.getChoices()[0]))
    """
    global states #global to use memoization
    key = state.toKey()
    
    #if the state already calculated, return values
    if(key in states):
        return states[key]
    
    score = state.calculateScore()
    
    # Terminal Node
    if(type(score) is bool and score == False):
        states[key] = score, None #Save values
        return states[key]
    
    choices = state.getChoices()
    
    #MAX player
    if(state.maxPlayer == 1):
        score = -np.inf
        bestChoice = None
        for choice in choices:
            state.doChoice(choice)
            newScore, newChoice = minmaxDecision(state)
            if(newScore > score):
                score = newScore
                bestChoice = choice
            state.undoChoice(choice)
        states[key] = score, bestChoice #Save values
        
    #MIN player
    else:
        score = np.inf
        bestChoice = None
        for choice in choices:
            state.doChoice(choice)
            newScore, newChoice = minmaxDecision(state)
            if(newScore < score):
                score = newScore
                bestChoice = choice
            state.undoChoice(choice)
        states[key] = score, bestChoice #Save values
    return states[key]


def negamaxDecision(state):
    """
    Implementation of Negamax algorithm with memoization
    
    :param state: The state of the game on wich we want to get the best choice and score.
    
    :type state: StateGame
    
    :return: Return a 2-tuple with the score and the best choice to make
    :rtype: 2-tuple(typeof(state.calculScore()), typeof(state.getChoices()[0]))
    """
    global states #global to use memoization
    key = state.toKey()
    
    #if the state already calculated, return values
    if(key in states):
        return states[key]
    
    score = state.calculateScore()
    
    # Terminal Node
    if(type(score) is bool and score == False):
        states[key] = score*state.maxPlayer, None #Save values
        return states[key] 
    
    score = -np.inf
    bestChoice = None
    choices = state.getChoices()
    for choice in choices:
        state.doChoice(choice)
        newScore, newChoice = negamaxDecision(state)
        newScore *= -1
        if(newScore > score):
            score = newScore
            bestChoice = choice
        state.undoChoice(choice)
    states[key] = score, bestChoice #Save values
    return states[key]

