import moduleApp
import moduleFuntion
import moduleStart

# hàm xin chào khi bắt đầu làm việc : text là tên của người dùng
def hello(text) :
    return moduleStart.hello(text)
# hàm nhận giọng nói và chuyển thành văn bản
def get_audio():
    return moduleStart.get_audio()
# hàm chuyển văn bản thành âm thanh
def speak(text):
    moduleStart.speak(text)
# lấy giờ / ngày tháng năm
def get_time(text):
    moduleFuntion.get_time(text)
# mở app trong máy tính : text là danh sách các app muốn mở
def open_application_multi(text):
    moduleApp.open_application_multi(text)
# điều khiển âm thanh loa
def controlVolumn(vol):
    moduleFuntion.controlVolumn(vol)
# điều khiển độ sáng màn hình
def controlBrightness(value):
    moduleFuntion.controlBrightness(value)
# mở nhạc trên youtube
def playSong_youtube(text):
    moduleApp.play_song(text)
def open_website(text):
    return moduleApp.open_website(text)
def googleSearch(text):
    moduleApp.googleSearch(text)
def weather_description(text):
    return moduleApp.current_weather(text)
def screenShot():
    moduleFuntion.screenShot()