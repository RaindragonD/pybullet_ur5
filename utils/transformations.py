import numpy as np
from scipy.spatial.transform import Rotation as R
import pybullet as p

def q2e(quat, ret_deg):
    return R.from_quat(quat).as_euler('xyz', degrees=ret_deg)

def e2q(euler, is_deg):
    return R.from_euler('xyz', euler, degrees=is_deg).as_quat()
    
def invert_pose(pose):
    return p.invertTransform(*pose)

def mult_pose(pose1, pose2):
    return p.multiplyTransforms(*pose1, *pose2)