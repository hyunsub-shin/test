import socket, struct, time, random
from PIL import Image, ImageOps
from io import BytesIO

TCP_IP = '192.168.137.6'
TCP_PORT = 8319

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def clearScreen(color, apply=True):
    header = struct.pack('<BBHHHH', 1, color, 0, 0, 1448, 1072)
    s.sendall(header)
    if apply:
        header = struct.pack('<BBHHHH', 4, 0, 0, 0, 1448, 1072)
        s.sendall(header)

def drawImage(posx, posy, origImage):
    grayImage = ImageOps.grayscale(origImage)
    width, height = grayImage.size
    pixels = grayImage.load()
    image = bytearray()
    for y in range(height):
        for x in range(0, width, 2):
            byt = (pixels[x,y] // 17) + ((pixels[x+1,y] // 17) << 4)
            image.append(byt)
    header = struct.pack('<BBHHHH', 2, 15, posx, posy, width, height)
    s.sendall(header)
    s.sendall(image)
    header = struct.pack('<BBHHHH', 4, 0, posx, posy, width, height)
    s.sendall(header)


clearScreen(15)
time.sleep(1)
origImage = Image.open('text_generate_img.jpg')
origImage = origImage.resize((1448, 1072))
drawImage(0, 0, origImage)

time.sleep(1)
s.close()
