from Robot import Robot
from Maze import Maze
maze=Maze(maze_size=(10,10),trap_number=10)
robot = Robot(maze) # 记得将 maze 变量修改为你创建迷宫的变量名
robot.set_status(learning=True,testing=False)
print(robot.update())

epoch = 20

epsilon0 = 0.5
alpha = 0.5
gamma = 0.9

maze_size = (6,6)
trap_number = 1
from Runner import Runner

g = Maze(maze_size=maze_size,trap_number=trap_number)
r = Robot(g,alpha=alpha, epsilon0=epsilon0, gamma=gamma)
r.set_status(learning=True)

runner = Runner(r, g)
runner.run_training(epoch, display_direction=True)