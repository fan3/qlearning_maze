from Robot import Robot
from Maze import Maze
maze=Maze(maze_size=(10,10),trap_number=10)
robot = Robot(maze) # 记得将 maze 变量修改为你创建迷宫的变量名
robot.set_status(learning=True,testing=False)
print(robot.update())

maze