import sys
sys.path.insert(0,'Models')
import Internet,App,Basic,CMD,ComputerFunction

def getAudio():
    return Basic.get_audio()

def mainFunction(keyvalue):
    request = keyvalue
    if request is not None:
        request = request.lower()
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
            Internet.open_website(request)
        elif 'mở bài hát' in request:
            song = request.split('hát',1)
            Internet.play_song(song[1])
        elif 'tìm kiếm trên google' in request:
            search = request.split('google',1)
            Internet.googleSearch(search[1])
        elif 'chụp màn hình' in request:
            ComputerFunction.screenShot()
        elif 'mở cài đặt' in request:
            ComputerFunction.open_setting()
        elif 'chuyển sang trang' in request:
            title = request.split('trang',1)
            ComputerFunction.switch_window(title[1])
        elif 'trở lại trang' in request:
            ComputerFunction.Return_Window()
        else :
            print("Sao dị")
    else :
        print('Error')


