import math

def getForceFromDistance(px1,py1,px2,py2):
    distance = math.sqrt((px2-px1)**2 + (py2-py1)**2)
    force = round(math.sqrt(distance),3)
    
    if distance == 0:
        return 0
    return force