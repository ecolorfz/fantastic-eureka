from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=2) # 创建场景，指定体素描边宽度和曝光值
scene.set_floor(0, (1.0, 1.0, 1.0)) # 地面高度
scene.set_background_color((0.5, 0.5, 0.4)) # 天空颜色
scene.set_directional_light((1, 1, -1), 0.2, (1, 0.8, 0.6)) # 光线方向和颜色


@ti.kernel
def initialize_voxels():
    scene.set_voxel(vec3(0), 1, vec3(1)) # 在 (0, 0, 0) 加入一个白色 (1, 1, 1) 的体素！

initialize_voxels()

scene.finish()
