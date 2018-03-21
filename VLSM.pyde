wheel = 0
wheelX = 32
wheelY = 32
wheelP = 0
newWheel = False
mX = 0
mY = 0
net = []
def settings():
    global net
    netMaskBits = 8
    if netMaskBits % 2 == 0:
        w = int(sqrt(2**netMaskBits))
        h = w
        size(w * 32, h * 32)
        print("Width: ", w, "Height: ", h)
    else:
        w = int(sqrt(2**netMaskBits/2)*2)
        h = int(sqrt(2**netMaskBits/2))
        size(w * 32, h * 32)
        print("Width: ", w, "Height: ", h)
    net = netArray(w, h)
    # idPrint 
    print(net)


def setup():
    global wheel, net
    
    background(0)
    # rectMode(CENTER)
    # netArray(9)
    drawgrid()
    textAlign(CENTER, CENTER)
    textSize(12)
    text("123", 112, 112)
    ipDraw(net)    
    
def draw():
    global wheel, newWheel, mX, mY, wheelX, wheelY, net
    pushMatrix()
    # translate(width/2, height/2)
    if (newWheel):
        background(0)
        drawgrid()
        ipDraw(net)
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
    wheel = 0 if wheel < 0 else wheel
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
    ip = int(bin(int(mX/32))[2:],4) + 2 * int(bin(int(mY/32))[2:],4)
    print("Wheel", wheel, "mX: ", mX, "mY: ", mY, "Row: ", mY / 32, "Column: ", mX / 32, "IP: ", ip)
    
    newWheel = True

def netArray(w, h):
    net = []
    for r in range(h):
        net.append([int(bin(c)[2:],4) + 2 * int(bin(r)[2:], 4) for c in range(w)])
        # for c in range(w):
    return net

def ipDraw(net):
    for i, row in enumerate(net):
        for j, col in enumerate(row):
            fill(128)
            text(net[i][j], j * 32 + 16, i * 32 + 16)
            # print(net[i][j])     

