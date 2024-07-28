import socket

print(socket.gethostbyname(socket.getfqdn()))			#1-1
print(socket.gethostbyname(socket.gethostname()))		#1-2

print(socket.gethostbyname_ex(socket.getfqdn()))		#2

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#3
s.connect(('8.8.8.8', 0))
ip = s.getsockname()[0]
print(ip)


clearScreen(15)
time.sleep(1)
origImage = Image.open('text_generate_img.jpg')
origImage = origImage.resize((1448, 1072))
drawImage(0, 0, origImage)

time.sleep(1)
s.close()
