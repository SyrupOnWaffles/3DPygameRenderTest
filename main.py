from pygame import *
from pygame import gfxdraw
import pygame, modelLoader
import numpy as np

screenSize = [1280, 720]
scale = 100

class model:
    faces = []
    verticies = []

class colours:
    black = (40,40,46)
    purple = (108,86,113)
    grey = (217,200,191)
    red = (249,130,132)
    light_purple = (176,169,228)
    blue = (172,204,228)
    mediumBlue = (137,163,182)
    darkBlue = (68,81,91)
    teal = (179,227,218)
    pink = (254,170,228)
    dark_green = (135,168,137)
    green = (176,235,147)
    light_green = (233,245,157)
    tan = (255,230,198)
    brown = (222,163,139)
    orange = (255,195,132)
    yellow = (255,247,160)
    white = (255,247,228)

orthProjection = [[1, 0, 0], [0, 1, 0],[0,0,0]]

modelLoader.loadObj("newmodels/cow.obj",model)

# rotation
xAngle = np.deg2rad(180)
yAngle = np.deg2rad(0)
zAngle = np.deg2rad(0)
xRotation = [[1, 0, 0],
                [0, np.cos(xAngle), -np.sin(xAngle)],
                [0, np.sin(xAngle), np.cos(xAngle)]]
yRotation = [[np.cos(yAngle), 0, np.sin(yAngle)],
                [0, 1, 0],
                [-np.sin(yAngle), 0, np.cos(yAngle)]]
zRotation = [[np.cos(zAngle), -np.sin(zAngle), 0],
                [np.sin(zAngle), np.cos(zAngle), 0],
                [0, 0, 1]]    


screen = pygame.display.set_mode((screenSize[0], screenSize[1]), SCALED, 1)
texture = pygame.image.load("texture.png")
pygame.display.set_caption('software renderer')
  
def rotated(coords, xAngle, yAngle, zAngle):
    xRotation = [[1, 0, 0],
                [0, np.cos(xAngle), -np.sin(xAngle)],
                [0, np.sin(xAngle), np.cos(xAngle)]]

    yRotation = [[np.cos(yAngle), 0, np.sin(yAngle)],
                [0, 1, 0],
                [-np.sin(yAngle), 0, np.cos(yAngle)]]

    zRotation = [[np.cos(zAngle), -np.sin(zAngle), 0],
                [np.sin(zAngle), np.cos(zAngle), 0],
                [0, 0, 1]]
    #All rotation object can make
    rotated = np.matmul(coords, xRotation)
    rotated = np.matmul(rotated, yRotation)
    rotated = np.matmul(rotated, zRotation)
            
    return rotated

def renderObject(model, xAngle, yAngle, zAngle, colour, thickness):      
    for x in range(len(model.faces)): 
            shade = 0
            one = [0,0,0]
            one = rotated(model.verticies[(model.faces[x][0][0]) - 1], xAngle, yAngle, zAngle)
            two = rotated(model.verticies[(model.faces[x][1][0]) - 1], xAngle, yAngle, zAngle)
            three = rotated(model.verticies[(model.faces[x][2][0]) - 1], xAngle, yAngle, zAngle)
            # normal calc
            normal = [0,0,0]
            line1 = [0,0,0]
            line2 = [0,0,0]
            line1[0] = two[0][0] - one[0][0]
            line1[1] = two[0][1] - one[0][1]
            line1[2] = two[0][2] - one[0][2]
        
            line2[0] = three[0][0] - one[0][0]
            line2[1] = three[0][1] - one[0][1]
            line2[2] = three[0][2] - one[0][2]
        
            normal[0] = line1[1] * line2[2] - line1[2] * line2[1]
            normal[1] = line1[2] * line2[0] - line1[0] * line2[2]
            normal[2] = line1[0] * line2[1] - line1[1] * line2[0]
        
            l = np.sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]);
            normal[0] /= l
            normal[1] /= l
            normal[2] /= l
                
            if(normal[2] > 0):
                # weird shading but ok
                l = abs(normal[0])

                one = np.matmul(one, orthProjection)
                two = np.matmul(two, orthProjection)
                three = np.matmul(three, orthProjection)

                pygame.gfxdraw.filled_polygon(screen, [((one[0][0])*scale + (screenSize[0] / 2), (one[0][1])*scale + (screenSize[1] / 2)), ((two[0][0])*scale + (screenSize[0] / 2), (two[0][1])*scale + (screenSize[1] / 2)), ((three[0][0])*scale + (screenSize[0] / 2), (three[0][1])*scale + (screenSize[1] / 2))], (255*l,195*l,132*l))
                # pygame.gfxdraw.polygon(screen, [((one[0][0])*scale + (screenSize[0] / 2), (one[0][1])*scale + (screenSize[1] / 2)), ((two[0][0])*scale + (screenSize[0] / 2), (two[0][1])*scale + (screenSize[1] / 2)), ((three[0][0])*scale + (screenSize[0] / 2), (three[0][1])*scale + (screenSize[1] / 2))], colours[3])
pygame.display.flip()

running = True
# game loop
while running:
    screen.fill(colours.black)
    for event in pygame.event.get():
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()  # Checking pressed keys
    if keys[pygame.K_LEFT]:
        yAngle -= .1
    if keys[pygame.K_RIGHT]:
        yAngle += .1
    if keys[pygame.K_UP]:
        xAngle -= .1
    if keys[pygame.K_DOWN]:
        xAngle += .1
    renderObject(model, xAngle, yAngle, zAngle, colours.white, 0)
    
    pygame.display.update()