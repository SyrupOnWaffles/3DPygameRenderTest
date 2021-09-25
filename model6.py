#cube
import numpy as np
xAngle = 0
yAngle = 0
zAngle = 0
class transform:
    size = 10
    xPos = 0
    yPos = 0
    zPos = 0
vertices=[
    [[(-2.0000* transform.size) + transform.xPos,(-2.000000 * transform.size) + transform.yPos,(2.000000 * transform.size) + transform.zPos]],
    [[(-2.0000* transform.size) + transform.xPos,(2.000000 * transform.size) + transform.yPos,(2.000000 * transform.size) + transform.zPos]],
    [[(-2.0000* transform.size) + transform.xPos,(-2.000000 * transform.size) + transform.yPos,(-2.000000 * transform.size) + transform.zPos]],
    [[(-2.0000* transform.size) + transform.xPos,(2.000000 * transform.size) + transform.yPos,(-2.000000 * transform.size) + transform.zPos]],
    
    [[(2.0000* transform.size) + transform.xPos,(-2.000000 * transform.size) + transform.yPos,(2.000000 * transform.size) + transform.zPos]],
    [[(2.0000* transform.size) + transform.xPos,(2.000000 * transform.size) + transform.yPos,(2.000000 * transform.size) + transform.zPos]],
    [[(2.0000* transform.size) + transform.xPos,(-2.000000 * transform.size) + transform.yPos,(-2.000000 * transform.size) + transform.zPos]],
    [[(2.0000* transform.size) + transform.xPos,(2.000000 * transform.size) + transform.yPos,(-2.000000 * transform.size) + transform.zPos]],


]
faces=[
    [[1,0,2],[7,0,2],[5,0,2]],
    [[1,0,2],[3,0,2],[7,0,2]], 
    [[1,0,6],[4,0,6],[3,0,6]], 
    [[1,0,6],[2,0,6],[4,0,6]], 
    [[3,0,3],[8,0,3],[7,0,3]], 
    [[3,0,3],[4,0,3],[8,0,3]], 
    [[5,0,5],[7,0,5],[8,0,5]], 
    [[5,0,5],[8,0,5],[6,0,5]], 
    [[1,0,4],[5,0,4],[6,0,4]], 
    [[1,0,4],[6,0,4],[2,0,4]], 
    [[2,0,1],[6,0,1],[8,0,1]], 
    [[2,0,1],[8,0,1],[4,0,1]], 

]
