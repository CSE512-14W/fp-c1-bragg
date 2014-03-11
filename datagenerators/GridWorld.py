

class GridWorld:
    
    def __init__(self, x, y, cost, reward, firepitreward, pFailure, discount):
        self.x = x
        self.y = y
        self.cost = cost
        self.reward = reward
        self.firepitreward = firepitreward
        self.pFailure = pFailure
        self.pSuccess = 1.0 - (2.0 * pFailure)
        self.discount = discount

    
    def getInitialState(self):
        return (0,0)

    def getStateString(self, state):
        (x, y) = state
        return "s%d-%d" % (x, y)
 
    def getStates(self):
        states = []
        for i in range(self.x):
            for j in range(self.y):
              states.append((i, j))
        states.append((-1,-1))
        
        return states

    def getActions(self, state):
        (x,y) = state
        actions = []
        if (x,y) == (2, 2):
            return ['Exit']
        if (x,y) == (-1,-1):
            return ['None']
        if y < self.y - 1:
            actions.append('N')
        if y > 0:
            actions.append('S')
        if x < self.x - 1:
            actions.append('E')
        if x > 0:
            actions.append('W')

        return actions

    def isTerminal(self, state):
        if state == (-1,-1):
            return True
        else:
            return False

    def getReward(self, state):
        (x, y) = state
        if (x, y) == (self.x - 1, self.y - 1):
            return self.reward
        if y == 0 and x > 0 and x < self.x - 1:
            return self.firepitreward
        if self.isTerminal(state):
            return 0
        else:
            return self.cost
        

    #assuming the action works perfectly, what is the next state?
    def getNextState(self, state, action):
        (x, y) = state
        if action == 'None':
            return (-1,-1)

        if action == 'N':
            if y < self.y - 1:
                return (x, y+1)
            else:
                return (x, y)
        elif action == 'S':
            if y > 0:
                return (x, y-1)
            else:
                return (x, y)
        elif action == 'E':
            if x < self.x - 1:
                return (x+1, y)
            else:
                return (x, y)
        elif action == 'W':
            if x > 0:
                return (x-1, y)
            else:
                return (x,y)

    def getT(self, state, action):
        nextStates = {}

        if state == (self.x-1, self.y-1):
            nextStates[(-1,-1)] = 1.0
        elif action == 'N':
            nextStates[self.getNextState(state, 'N')] = 0.0
            nextStates[self.getNextState(state, 'E')] = 0.0
            nextStates[self.getNextState(state, 'W')] = 0.0
            
            nextStates[self.getNextState(state, 'N')] += self.pSuccess
            nextStates[self.getNextState(state, 'E')] += self.pFailure
            nextStates[self.getNextState(state, 'W')] += self.pFailure
        elif action == 'S':
            nextStates[self.getNextState(state, 'S')] = 0.0
            nextStates[self.getNextState(state, 'E')] = 0.0
            nextStates[self.getNextState(state, 'W')] = 0.0
            
            nextStates[self.getNextState(state, 'S')] += self.pSuccess
            nextStates[self.getNextState(state, 'E')] += self.pFailure
            nextStates[self.getNextState(state, 'W')] += self.pFailure

        elif action == 'E':
            nextStates[self.getNextState(state, 'N')] = 0.0
            nextStates[self.getNextState(state, 'E')] = 0.0
            nextStates[self.getNextState(state, 'S')] = 0.0
            
            nextStates[self.getNextState(state, 'N')] += self.pFailure
            nextStates[self.getNextState(state, 'E')] += self.pSuccess
            nextStates[self.getNextState(state, 'S')] += self.pFailure

        elif action == 'W':
            nextStates[self.getNextState(state, 'N')] = 0.0
            nextStates[self.getNextState(state, 'S')] = 0.0
            nextStates[self.getNextState(state, 'W')] = 0.0
            
            nextStates[self.getNextState(state, 'N')] += self.pFailure
            nextStates[self.getNextState(state, 'S')] += self.pFailure
            nextStates[self.getNextState(state, 'W')] += self.pSuccess

        return nextStates.items()

