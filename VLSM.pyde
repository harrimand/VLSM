
from __future__ import print_function

wheel = 0
sn = 0
snW = 32
snH = 32
snX = 0
snY = 0
wheelP = 0
updateSN = False
netMaskBits = 8
mX = 0
mY = 0
net = []
subNet = []

class Network(object):
    def __init__(self, snAdd, snMsk):
        self.sn = snAdd
        self.snM = snMsk
    def show(self):
        shStr = str(self.sn) + "/" + str(self.snM) + "  "
        print(shStr, end='')
    # def add(self, snA, snM):
        

def settings():
    global net
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
    global updateSN
    pushMatrix()
    # translate(width/2, height/2)
    if (updateSN):
        background(0)
        drawgrid()
        ipDraw(net)
        stroke(32, 32, 96)
        fill(32, 96, 96, 160)
        rect(snX, snY, abs(snW), abs(snH))
        updateSN = False
    popMatrix()
    
def mouseWheel(event):
    global wheel, updateSN, snW, snH, wheelP, sn, snX, snY
    mX = round(mouseX - mouseX % 32 )
    mY = round(mouseY - mouseY % 32 )
    wheel += event.getCount()
    wheel = 0 if wheel < 0 else wheel
    # wheel = constrain(wheel, 0, netMaskBits)
    if wheel > wheelP:
        if(snW == snH):
            snW *= 2
        else:
            snH *= 2
    elif wheel < wheelP:
        if(snW == snH):
            snH /= 2
        else:
            snW /= 2
    snW = 32 if snW < 32 else snW
    snH = 32 if snH < 32 else snH
    
    ip = int(bin(int(mX/32))[2:],4) + 2 * int(bin(int(mY/32))[2:],4)
    sn = (2**netMaskBits - 2**wheel) &  ip
    snCol = int( floor((mX/32) / abs(snW / 32)) * abs(snW / 32))
    snX = snCol * 32
    snRow = int( floor((mY/32) / abs(snH / 32)) * abs(snH / 32))
    snY = snRow * 32
    
    wheelP = wheel
    
    # print("Wheel", wheel, "mX: ", mX, "mY: ", mY, "Row: ", mY / 32, "Column: ", mX / 32, "IP: ", ip)
    print("Subnet Size: ", 2 ** wheel, "Row: ", mY / 32, "Column: ", mX / 32, "IP: ", ip, "Subnet: ", sn)
    print("Wheel", wheel, "Subnet Row: ", snRow, "Subnet Col: ", snCol)
    
    updateSN = True

def mouseMoved(event):
    if keyCode == SHIFT:
        return
    global sn, snW, snH, snX, snY, updateSN
    mX = round(mouseX - mouseX % 32 )
    mY = round(mouseY - mouseY % 32 )
    # print("mX: ", mX, "mY: ", mY)
    ip = int(bin(int(mX/32))[2:],4) + 2 * int(bin(int(mY/32))[2:],4)
    sn = (2**netMaskBits - 2**wheel) &  ip
    snCol = int( floor((mX/32) / abs(snW / 32)) * abs(snW / 32))
    snX = snCol * 32
    snRow = int( floor((mY/32) / abs(snH / 32)) * abs(snH / 32))
    snY = snRow * 32
    updateSN = True

def netArray(w, h):
    net = []
    for r in range(h):
        net.append([int(bin(c)[2:],4) + 2 * int(bin(r)[2:], 4) for c in range(w)])
    return net

def drawgrid():
    stroke(64)
    for r in range(0, height, 32):
        line(0, r, width, r)
    for c in range(0, width, 32):
        line(c, 0, c, height)     

def ipDraw(net):
    for i, row in enumerate(net):
        for j, col in enumerate(row):
            fill(128)
            text(net[i][j], j * 32 + 16, i * 32 + 16)

def keyPressed():
    if key == 's':
        for snA in subNet:
            snA.show()

def mousePressed():
    subNet.append(Network(sn, 32 - wheel))
