from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import sys
sys.path.insert(0,'Models')
import ComputerFunction  # Import module chứa hàm screenShot

class SimpleHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        try:
            # Đường dẫn tương đối đến file index.html
            file_path = os.path.join(os.path.dirname(__file__), self.path[1:])
            
            # Đọc nội dung từ file index.html với mã bảng ký tự 'utf-8'
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            
            # Trả về nội dung của file index.html
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(content, "utf8"))
        except FileNotFoundError:
            # Trường hợp file index.html không tồn tại
            self.send_error(404, "File not found")

    def do_POST(self):
        # Xử lý yêu cầu POST
        if self.path == '/screenshot':  # Endpoint cho chụp màn hình
            try:
                # Gọi hàm screenShot từ module ComputerFunction
                ComputerFunction.screenShot()

                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Success')
            except Exception as e:
                self.send_error(500, f"Internal Server Error: {str(e)}")
        if self.path == '/gettime':  # Endpoint cho chụp màn hình
            try:
                # Gọi hàm screenShot từ module ComputerFunction
                ComputerFunction.get_time('giờ')

                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Success')
            except Exception as e:
                self.send_error(500, f"Internal Server Error: {str(e)}")


if __name__ == "__main__":
    # Cấu hình host và cổng port cho server
    server_address = ('127.0.0.1', 8000)
    # Khởi tạo server với thông số cấu hình ở trên
    httpd = HTTPServer(server_address, SimpleHTTP)
    # Tiến hành chạy server
    print("Server đang chạy...")
    httpd.serve_forever()
