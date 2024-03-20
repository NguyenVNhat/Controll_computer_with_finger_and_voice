import socket
import cv2
import pickle
import struct
import threading

def receive_video_from_client(conn):
    payload_size = struct.calcsize("L")
    while True:
        data = b""
        while len(data) < payload_size:
            packet = conn.recv(4*1024)
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]
        
        while len(data) < msg_size:
            data += conn.recv(4*1024)
        frame_data = data[:msg_size]
        data = data[msg_size:]
        
        # Deserialize frame
        frame = pickle.loads(frame_data)
        
        # Hiển thị video từ client
        cv2.imshow('Video from client', frame)
        if cv2.waitKey(1) == 27:
            break
    conn.close()

def send_video_to_client(conn):
    cap = cv2.VideoCapture(0)
    while True:
        # Đọc khung hình từ camera
        ret, frame = cap.read()
        
        # Serialize frame thành một chuỗi bytes
        data = pickle.dumps(frame)
        
        # Lấy độ dài của dữ liệu và chuyển thành một chuỗi bytes
        message_size = struct.pack("L", len(data))
        
        # Gửi độ dài của dữ liệu trước
        conn.sendall(message_size + data)

# Khởi tạo socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Khai báo host và port
host = '127.0.0.1'
port = 12345

# Bind địa chỉ và port với socket
server_socket.bind((host, port))

# Lắng nghe kết nối từ client
server_socket.listen(5)

print("Server đang lắng nghe tại {}:{}".format(host, port))

# Chấp nhận 
