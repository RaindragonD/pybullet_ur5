import pybullet as p
from environment.ur5 import UR5
from environment.envBase import BaseEnv
import numpy as np
import time

def step(interval=10):
    for i in range (interval):
        p.stepSimulation()
        time.sleep(1/240)

gui = True # set to True to enable gui
env = BaseEnv(gui=gui) # create a environment
p.loadURDF("plane.urdf")
robot_pos = np.array([0,0,0]) # robot positioned at the center
ur5 = UR5(env, basePosition=robot_pos)
step()


obj_path = "assets/parts/cube.urdf"
obj_pos = [0.5,0.5,0] # define object position
obj_orn = [0,0,0,1] # define object orientation in quaternion
obj_id = p.loadURDF(obj_path, obj_pos, obj_orn)

pick_pose = p.getBasePositionAndOrientation(obj_id) # get object pose as pick pose
place_pose = ([0.5,-0.5,0], [0,0,0,1]) # define place pose (place_position, place_orientation)

ur5.execute_pick_place(pick_pose, place_pose, obj_ids=[obj_id])

step()