# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 1)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        v = float("-inf")
        bestAction = []
        agent = 0
        actions = gameState.getLegalActions(agent)
        successors = [(action, gameState.generateSuccessor(agent, action)) for action in actions]
        for successor in successors:
            temp = minimax(1, range(gameState.getNumAgents()), successor[1], self.depth, self.evaluationFunction)

            if temp > v:
                v = temp
                bestAction = successor[0]
        return bestAction


def minimax(agent, agentList, state, depth, evalFunc):
    if depth <= 0 or state.isWin() == True or state.isLose() == True:
        return evalFunc(state)

    if agent == 0:
        v = float("-inf")
    else:
        v = float("inf")

    actions = state.getLegalActions(agent)
    successors = [state.generateSuccessor(agent, action) for action in actions]
    for j in range(len(successors)):
        successor = successors[j];

        if agent == 0:

            v = max(v, minimax(agentList[agent + 1], agentList, successor, depth, evalFunc))
        elif agent == agentList[-1]:

            v = min(v, minimax(agentList[0], agentList, successor, depth - 1, evalFunc))
        else:

            v = min(v, minimax(agentList[agent + 1], agentList, successor, depth, evalFunc))

    return v

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """

class ExpectimaxAgent(MultiAgentSearchAgent):

    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.ExpectiMax(gameState, 1, 0)

    def ExpectiMax(self, gameState, currentDepth, agentIndex):
            "terminal check"
            if currentDepth > self.depth or gameState.isWin() or gameState.isLose():
                return self.evaluationFunction(gameState)

            "expectimax algorithm"
            legalMoves = [action for action in gameState.getLegalActions(agentIndex) if action != 'Stop']

            # update next depth
            nextIndex = agentIndex + 1
            nextDepth = currentDepth
            if nextIndex >= gameState.getNumAgents():
                nextIndex = 0
                nextDepth += 1

            results = [self.ExpectiMax(gameState.generateSuccessor(agentIndex, action), nextDepth, nextIndex) for action
                       in legalMoves]

            if agentIndex == 0 and currentDepth == 1:  # pacman first move
                bestMove = max(results)
                bestIndices = [index for index in range(len(results)) if results[index] == bestMove]
                chosenIndex = random.choice(bestIndices)  # Pick randomly among the best
                # print 'pacman %d' % bestMove
                return legalMoves[chosenIndex]

            if agentIndex == 0:
                bestMove = max(results)
                # print bestMove
                return bestMove
            else:
                "In ghost node, return the average(expected) value of action"
                bestMove = sum(results) / len(results)
                # print bestMove, sum(results), len(results)
                return bestMove



def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    """Calculating distance to the closest food pellet"""
    util.raiseNotDefined()

    better = betterEvaluationFunction

    class ContestAgent(MultiAgentSearchAgent):


        def getAction(self, gameState):

            util.raiseNotDefined()
# Abbreviation
better = betterEvaluationFunction

