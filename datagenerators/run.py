from GridWorld import *
from VI import *
import json

#state, bestAction, value
def outputStateValues(mdp, v):
    f = open('../data/gridworldstatevalues', 'w')
    f.write('state,value\n')
    for state in mdp.getStates():
        bestAction = None
        bestActionQValue = -1290310231
        for a in mdp.getActions(state):
            qvalue = getQValue(mdp, state, a, v)
            if  qvalue > bestActionQValue:
                bestAction = a
        f.write('%s,%s,%f\n' % (mdp.getStateString(state),bestAction, v[state]))


#state, action, qvalue
def outputQValues(mdp):
    f = open('../data/gridworldqvalues', 'w')
    f.write('state,action,qvalue\n')
    for state in mdp.getStates():
        for action in mdp.getActions(state):
            qvalue = 0.0
            for (s, p) in mdp.getT(state, action):
                qvalue += p * v[s]
            f.write('%s,%s,%f\n' % (mdp.getStateString(state), str(action), qvalue))

#state1, action, qvalue,  state2, bestAction, value, poo, probability
def outputTable(mdp, v):
    f = open('../data/gridworldtable', 'w')
    f.write('state1,action,qvalue,state2,bestAction,value,poo,incomingProbability\n')
    for state in mdp.getStates():
        print state
        for action in mdp.getActions(state):
            qvalue = 0.0
            for (s, p) in mdp.getT(state, action):
                qvalue += p * v[s]
            lastPointOfOrigin = -0.5
            for (s, p) in mdp.getT(state, action):
                bestAction = None
                bestActionQValue = -1290310231
                for a in mdp.getActions(s):
                    q = getQValue(mdp, s, a, v)
                    if  q > bestActionQValue:
                        bestActionQValue = q
                        bestAction = a
                nextPointOfOrigin = lastPointOfOrigin + p / 2
                lastPointOfOrigin += p
                print "HERE"
                print state
                f.write('%s,%s,%f,%s,%s,%f,%f,%f\n' % (mdp.getStateString(state), str(action), qvalue, 
                                                       mdp.getStateString(s), bestAction, v[s], 
                                                       nextPointOfOrigin, p))


def outputPolicyTreeToJSON(mdp, state, action, isBestAction, prob, v, 
                 policy, depth, isState, pointOfOrigin):
    json = {}
    if isState:
        json['name'] = mdp.getStateString(state)
        json['value'] = "%f" % v[state]
        json['incomingProbability'] = "%f" % prob
        if depth > 0:
            actions = []
            bestAction = None
            bestActionQValue = -1290310231
            for a in mdp.getActions(state):
                qvalue = getQValue(mdp, state, a, v)
                if  qvalue > bestActionQValue:
                    bestAction = a
                    bestActionQValue = qvalue
            for a in mdp.getActions(state):
                if a == bestAction:
                    actions.append(outputPolicyTreeToJSON(mdp, state, a, True,  0, 
                                                v, policy, depth, False, 0))
                else:
                    actions.append(outputPolicyTreeToJSON(mdp, state, a, False, 0, 
                                                v, policy, depth, False, 0))

            json['policy'] = bestAction
            json['children'] = actions
        json['type'] = "state"
        json['poo'] = "%f" % pointOfOrigin
    else:
        json['name'] = str(action)
        json['value'] = "0"
        
        states = []
        qvalue = 0.0

        lastPointOfOrigin = -0.5

        if isBestAction:
            for (s, p) in mdp.getT(state, action):
            #compute necessary translation for links so they all line up nicely
                nextPointOfOrigin = lastPointOfOrigin + p / 2
                lastPointOfOrigin += p

                states.append(outputPolicyTreeToJSON(mdp, s, None, False, p, 
                                           v, policy, depth-1, True,
                                           nextPointOfOrigin))
                qvalue += p * v[s]
        else:
            for (s, p) in mdp.getT(state, action):
                qvalue += p * v[s]


        json['qvalue'] = qvalue

        
        json['children'] = states
        json['type'] = "action"
    
    return json

def outputToJSON(mdp, state, action, prob, v, 
                 policy, depth, isState, pointOfOrigin):
    json = {}
    if isState:
        json['name'] = mdp.getStateString(state)
        json['value'] = "%f" % v[state]
        json['incomingProbability'] = "%f" % prob
        #if depth > 0:
        actions = []
        bestAction = None
        bestActionQValue = -1290310231
        for a in mdp.getActions(state):
            qvalue = getQValue(mdp, state, a, v)
            if  qvalue > bestActionQValue:
                bestAction = a
                bestActionQValue = qvalue
        if depth > 0:
            for a in mdp.getActions(state):
                actions.append(outputToJSON(mdp, state, a, 0, 
                                            v, policy, depth, False, 0))
            json['children'] = actions
        json['policy'] = bestAction
        json['type'] = "state"
        json['poo'] = "%f" % pointOfOrigin
    else:
        json['name'] = str(action)
        json['value'] = "0"
        
        states = []
        qvalue = 0.0

        lastPointOfOrigin = -0.5

        for (s, p) in mdp.getT(state, action):
            #compute necessary translation for links so they all line up nicely
            nextPointOfOrigin = lastPointOfOrigin + p / 2
            lastPointOfOrigin += p

            states.append(outputToJSON(mdp, s, None, p, 
                                       v, policy, depth-1, True,
                                       nextPointOfOrigin))
            qvalue += p * v[s]

        json['qvalue'] = qvalue

        
        json['children'] = states
        json['type'] = "action"
    
    return json

gridworld = GridWorld(3, 3, -10, 100, -10000, 0.1, 1.0)
v = runVI(gridworld)
print v
policy = getPolicy(gridworld, v)
print policy

f = open('../data/gridworldpolicytreedepth5.json', 'w')
f2 = open('../data/gridworlddepth2.json', 'w')

f2.write(json.dumps(outputToJSON(gridworld, gridworld.getInitialState(), None, 1.0, 
             v, policy, 2, True, 0)))



f.write(json.dumps(outputPolicyTreeToJSON(gridworld, gridworld.getInitialState(), 
                                None, False, 1.0, v, policy, 5, True, 0),
                   indent=4))

print "Outputing Table"
outputTable(gridworld, v)
print "Done"
