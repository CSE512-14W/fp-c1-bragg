from GridWorld import *
from VI import *
import json


def outputToJSON(mdp, state, action, prob, v, 
                 policy, depth, isState, pointOfOrigin):
    json = {}
    if isState:
        json['name'] = mdp.getStateString(state)
        json['value'] = "%f" % v[state]
        json['incomingProbability'] = "%f" % prob
        if depth > 0:
            actions = []
            for a in mdp.getActions(state):
                actions.append(outputToJSON(mdp, state, a, 0, 
                                            v, policy, depth, False, 0))
            json['children'] = actions
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

gridworld = GridWorld(3, 3, -10, 100, -100, 0.1, 1.0)
v = runVI(gridworld)
print v
policy = getPolicy(gridworld, v)
print policy

f = open('../data/gridworlddepth5.json', 'w')

print outputToJSON(gridworld, gridworld.getInitialState(), None, 1.0, 
             v, policy, 2, True, 0)

f.write(json.dumps(outputToJSON(gridworld, gridworld.getInitialState(), 
                                None, 1.0, v, policy, 5, True, 0),
                   indent=4))

