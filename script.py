import os

path= ''  ##Put in FullPath
files = os.listdir(path)

for index, file in enumerate(files):
    # print(file)
    filename = os.path.join(path, file)
    image_data = open(filename, 'rb')
    if image_data.read(2) != b'\xff\xd8':
        os.remove(filename)
    else:
        image_data.close()
        os.rename(filename, filename + '.jpg')