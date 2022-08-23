from SLL import *

maze = SLL()
front0 = Location(False, False, True, 0)
right0 = Location(False, True, False, 0)
left0 = Location(True, False, False, 0)

front1 = Location(False, False, True, 1)
right1 = Location(False, True, False, 1)
left1 = Location(True, False, False, 1)

maze.append(front0)
maze.append(right0)
maze.append(left0)

maze.append(front1)
maze.append(right1)
maze.append(left1)
print("------")

maze.print_as_matrix()
s = maze.head.next




maze.insert(1, 1, front0, Node(id="?B"))
print("------")
maze.remove(0, 0)
maze.insert(0, 0, left0, Node(id="?B"))
maze.remove(0, 0)
print("------")


maze.print_as_matrix()

