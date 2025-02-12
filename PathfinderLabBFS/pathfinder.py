from queue import Queue
from maze_problem import *
from dataclasses import *

@dataclass
class SearchTreeNode:
    """
    SearchTreeNodes contain the following attributes to be used in generation of
    the Search tree:

    Attributes:
        player_loc (tuple[int, int]):
            The player's location in this node.
        action (str):
            The action taken to reach this node from its parent (or empty if the root).
        parent (Optional[SearchTreeNode]):
            The parent node from which this node was generated (or None if the root).
    """
    player_loc: tuple[int, int]
    action: str
    parent: Optional["SearchTreeNode"]
    
    def __str__(self) -> str:
        return "@: " + str(self.player_loc)


def pathfind(problem: MazeProblem) -> Optional[list[str]]:
    """
    The main workhorse method of the package that performs breadth first tree search to find the optimal
    sequence of actions that takes the agent from its initial state to the goal.

    Parameters:
        problem (MazeProblem):
            The MazeProblem object constructed on the maze that is to be solved.

    Returns:
        Optional[list[str]]:
            A solution to the problem: a sequence of actions leading from the 
            initial state to the goal. Assume all problems served to this classwork
            have a solution!
    """
    # Initialize the frontier with the initial state
    initial_loc = problem.get_initial_loc()
    frontier = Queue()
    frontier.put(SearchTreeNode(player_loc=initial_loc, action="", parent=None))
    explored = set()

    while not frontier.empty():
        # Pop the node from the frontier
        node = frontier.get()
        player_loc = node.player_loc

        # If the node contains the goal state, return the solution
        if player_loc == problem.get_goal_loc():
            return construct_solution(node)

        # Add the node to the explored set
        explored.add(player_loc)

        # Expand the node, adding the resulting nodes to the frontier
        for action, new_loc in problem.get_transitions(player_loc).items():
            if new_loc not in explored:
                child_node = SearchTreeNode(player_loc=new_loc, action=action, parent=node)
                frontier.put(child_node)

    return None


def construct_solution(node: SearchTreeNode) -> list[str]:
    """
    Constructs the solution path by walking back from the goal node to the initial state.

    Parameters:
        node (SearchTreeNode):
            The goal node from which to construct the solution path.

    Returns:
        list[str]:
            The sequence of actions leading from the initial state to the goal.
    """
    solution = []
    while node.parent is not None:
        solution.append(node.action)
        node = node.parent
    solution.reverse()
    return solution

