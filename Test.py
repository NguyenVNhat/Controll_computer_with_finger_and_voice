import os

def find_and_open_folder(CD_driver,folder_name):
    folder_name_lower = folder_name.lower()
    for root, dirs, files in os.walk('{0}:\\'.format(CD_driver)):
        for dir_name in dirs:
            if dir_name.lower() == folder_name_lower:
                folder_path = os.path.join(root, dir_name)
                os.startfile(folder_path)
                return
    return "Không tìm thấy thư mục"
find_and_open_folder("D","riot client")
 