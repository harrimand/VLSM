wheel = 0
wheelX = 32
wheelY = 32
wheelP = 0
newWheel = False
mX = 0
mY = 0
def settings():
    size(1024, 512)
    
def setup():
    global wheel
    background(0)
    # rectMode(CENTER)
    netArray(9)
    drawgrid()
    
def draw():
    global wheel, newWheel, mX, mY, wheelX, wheelY
    pushMatrix()
    # translate(width/2, height/2)
    if (newWheel):
        background(0)
        drawgrid()
        stroke(32, 32, 96)
        fill(32, 96, 96, 160)
        rect(mX, mY, abs(wheelX), abs(wheelY))
        newWheel = False
    popMatrix()

    
def drawgrid():
    stroke(64)
    for r in range(0, height, 32):
        line(0, r, width, r)
    for c in range(0, width, 32):
        line(c, 0, c, height)     
    
def mouseWheel(event):
    global wheel, newWheel, mX, mY, wheelX, wheelY, wheelP
    mX = round(mouseX - mouseX % 32 )
    mY = round(mouseY - mouseY % 32 )
    wheel += event.getCount()
    if wheel > wheelP:
        if(wheelX == wheelY):
            wheelX *= 2
        else:
            wheelY *= 2
    elif wheel < wheelP:
        if(wheelX == wheelY):
            wheelY /= 2
        else:
            wheelX /= 2
    wheelX = 32 if wheelX < 32 else wheelX
    wheelY = 32 if wheelY < 32 else wheelY
    wheelP = wheel
    print("Wheel", wheel, "mX: ", mX, "mY: ", mY)
    newWheel = True

def netArray(hostBits):
    if hostBits % 2 == 0:
        print("Square")
    else: print("Rectangular")








