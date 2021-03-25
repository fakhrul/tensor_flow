import os
import glob
import xml.etree.ElementTree as ET
from PIL import Image


# def fixed_filename(path):
#     for file in glob.glob(path + '/*.*'):
#         dirName = os.path.dirname(file)
#         baseName = os.path.basename(file)
#         (fileName, ext) = os.path.splitext(baseName)
#         fileName = fileName.replace(" ", "")
#         fileName = fileName.replace("(", "")
#         fileName = fileName.replace(")", "")
#         newPath = dirName + "\\" + fileName + ext
#         os.rename(file, newPath)

# def fixed_file(path):
#     for xml_file in glob.glob(path + '/*.xml'):
#         baseName = os.path.basename(xml_file)
#         fileName = os.path.splitext(baseName)[0]
#         print(fileName)
#         tree = ET.parse(xml_file)
#         root = tree.getroot()
#         for member in root.findall('object'):
#             elmFileName = root.find('filename')
#             elmFileName.text = fileName + ".jpg"
#             # value = (root.find('folder').text,
#             #          root.find('filename').text,
#             #          root.find('path').text)
#         tree.write(xml_file,encoding='UTF-8',xml_declaration=True)

        
        # print(value)

def resize_image(path, ratio):
    image = Image.open(path)
    image_new = image.resize((int(image.size[0] * ratio), int(image.size[1] * ratio)))
    image_new.save(path)

def update_xml(path, ratio):
    tree = ET.parse(path)
    root = tree.getroot()
    for size in root.find('size'):
        if size.tag == "width":
            size.text =str(int(int(size.text) * ratio))
        if size.tag == "height":
            size.text =str(int(int(size.text) * ratio))

    for member in root.findall('object'):
        for coordinate in member.find('bndbox'):
            coordinate.text =str(int(int(coordinate.text) * ratio))
            # print(coordinate.text)
    tree.write(path,encoding='UTF-8',xml_declaration=True)

def fixed_file(path, ratio):
    for xml_file in glob.glob(path + '/*.xml'):
        baseName = os.path.basename(xml_file)
        fileName = os.path.splitext(baseName)[0]

        dirName = os.path.dirname(xml_file)
        image_file = dirName + "\\" + fileName + ".jpg"

        resize_image(image_file, ratio)
        update_xml(xml_file, ratio)
        print("done", fileName)


def main():
    for folder in ['train', 'test']:
        image_path = os.path.join(os.path.abspath('../images'), ( folder))
        fixed_file(image_path, 0.2)
    print('Successfully fixed fileName.')
    

main()