import socket

print(socket.gethostbyname(socket.getfqdn()))			#1-1
print(socket.gethostbyname(socket.gethostname()))		#1-2

print(socket.gethostbyname_ex(socket.getfqdn()))		#2

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)	#3
s.connect(('8.8.8.8', 0))
ip = s.getsockname()[0]
print(ip)