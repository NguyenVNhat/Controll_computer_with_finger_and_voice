import socket
import cv2
import pickle
import struct

# Khởi tạo socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Khai báo host và port của server
host = '127.0.0.1'
port = 12345

# Kết nối tới server
client_socket.connect((host, port))

# Nhận dữ liệu video từ server
data = b""
payload_size = struct.calcsize("L")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4*1024)
        if not packet: break
        data += packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0]
    
    while len(data) < msg_size:
        data += client_socket.recv(4*1024)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    # Deserialize frame
    frame = pickle.loads(frame_data)
    
    # Hiển thị video
    cv2.imshow('Video from server', frame)
    if cv2.waitKey(1) == 27:
        break

# Đóng kết nối
client_socket.close()

