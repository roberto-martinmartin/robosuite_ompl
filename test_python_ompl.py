from ompl import base as ob
from ompl import geometric as og
 
def isStateValid(state):
    # "state" is of type SE2StateInternal, so we don't need to use the "()"
    # operator.
    #
    # Some arbitrary condition on the state (note that thanks to
    # dynamic type checking we can just call getX() and do not need
    # to convert state to an SE2State.)
    return state.getX() < .6
 
def plan():
    # create an SE2 state space
    # space = ob.SE2StateSpace()
    space = ob.RealVectorStateSpace(7)
 
    # set lower and upper bounds
    bounds = ob.RealVectorBounds(7)
    bounds.setLow(-0.1)
    bounds.setHigh(0.1)
    space.setBounds(bounds)
 
    # create a simple setup object
    ss = og.SimpleSetup(space)
    ss.setStateValidityChecker(ob.StateValidityCheckerFn(isStateValid))
 
    start = ob.State(space)
    # we can pick a random start state...
    start.random()
 
    goal = ob.State(space)
    # we can pick a random goal state...
    goal.random()
 
    ss.setStartAndGoalStates(start, goal)
 
    # this will automatically choose a default planner with
    # default parameters
    solved = ss.solve(1.0)
 
    if solved:
        # try to shorten the path
        ss.simplifySolution()
        # print the simplified path
        print(ss.getSolutionPath())
 
 
if __name__ == "__main__":
    plan()
