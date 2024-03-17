import sys
sys.path.insert(0,'Models')
import Internet,App,Basic,CMD,ComputerFunction

def getAudio():
    return Basic.get_audio()

requestCMD = ['mở cài đặt','mở cài đặt âm thanh','mở cài đặt display''mở cài đặt autoplay','mở cài đặt usb','mở cài đặt pen and windows ink',
              'mở cài đặt touchpad','mở cài đặt mobile-devices','mở cài đặt mouse','mở cài đặt printers','mở cài đặt bluetooth','mở file explorer',
              'mở task manager','mở máy tính','mở control panel','mở quản lí ảnh','mở camera','mở lịch','mở quản lí đồng hồ','mở bản đồ','mở outlook']

def mainFunction(keyvalue):
    request = keyvalue
    if request is not None:
        request = request.lower()
        print(request)
        if 'mấy giờ' in request or 'ngày mấy' in request  :
            ComputerFunction.get_time(request)
        elif 'âm lượng' in request:
            vol = request.split('lượng',1)
            ComputerFunction.controlVolumn(int(vol[1]))
        elif 'độ sáng' in request:
            val = request.split('sáng',1)
            ComputerFunction.controlBrightness(int(val[1]))
        elif 'mở ứng dụng' in request:
            app = request.split('dụng',1)
            App.open_application_multi(app[1])
        elif 'mở web' in request:
            request = request.replace(" ","")
            web = request.split('web',1)
            Internet.open_website(web[1])
        elif 'mở youtube' in request:
            song = request.split('youtube',1)
            Internet.play_Video(song[1])
        elif 'mở zingmp3 tìm kiếm' in request:
            song = request.split('kiếm',1)
            Internet.play_song_mp3(song[1])
        elif 'tìm kiếm trên google' in request:
            search = request.split('google',1)
            Internet.googleSearch(search[1])
        elif 'chụp màn hình' in request:
            ComputerFunction.screenShot()
        elif 'gửi email' in request:
            title = input('Nhập tiêu đề :')
            content = input('Nhập nội dung :')
            email_receive = input('Nhập email nhận :')
            Internet.send_email(title,content,email_receive)
        for item in requestCMD:
            if item in request:
                CMD.OpenSetting(item)

    else :
        print('Error')
while True:
    request = input('Nhập từ khóa :')
    mainFunction(request)


