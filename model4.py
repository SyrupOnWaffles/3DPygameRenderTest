#pyramid
class transform:
    size = 10
    normalsize = 20
    xPos = 0
    yPos = 0
    zPos = 0
vertices=[
    
    [[int(0.000000 * transform.size) + transform.xPos,int(-2.000000 * transform.size) + transform.yPos,int(-2.000000 * transform.size) + transform.zPos]],
    [[int(1.732051 * transform.size) + transform.xPos,int(-2.000000 * transform.size) + transform.yPos,int(1.000000 * transform.size) + transform.zPos]],
    [[int(-1.732051 * transform.size) + transform.xPos,int(-2.000000 * transform.size) + transform.yPos,int(1.000000 * transform.size) + transform.zPos]],
    [[int(0.000000 * transform.size) + transform.xPos,int(2.000000 * transform.size) + transform.yPos,int(0.000000 * transform.size) + transform.zPos]],
]
faces=[
    [[1,1,1],[4,2,1],[2,3,1]],
    [[1,4,2],[2,5,2],[3,6,2]],
    [[2,3,3],[4,2,3],[3,7,3]],
    [[3,7,4],[4,2,4],[1,1,4]],
]
normal=[
    [[int(0.8402 * transform.normalsize) + transform.xPos, int(0.2425 * transform.normalsize) + transform.yPos, int(-0.4851 * transform.normalsize) + transform.zPos]],
    [[int(0.0000 * transform.normalsize) + transform.xPos, int(-1.0000 * transform.normalsize) + transform.yPos, int(0.0000 * transform.normalsize) + transform.zPos]],
    [[int(-0.0000 * transform.normalsize) + transform.xPos, int(0.2425 * transform.normalsize) + transform.yPos, int(0.9701 * transform.normalsize) + transform.zPos]],
    [[int(-0.8402 * transform.normalsize) + transform.xPos, int(0.2425 * transform.normalsize) + transform.yPos, int(-0.4851 * transform.normalsize) + transform.zPos]],
]