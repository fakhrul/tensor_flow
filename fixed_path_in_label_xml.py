import os
import glob
import xml.etree.ElementTree as ET


def fixed_filename(path):
    for file in glob.glob(path + '/*.*'):
        dirName = os.path.dirname(file)
        baseName = os.path.basename(file)
        (fileName, ext) = os.path.splitext(baseName)
        fileName = fileName.replace(" ", "")
        fileName = fileName.replace("(", "")
        fileName = fileName.replace(")", "")
        newPath = dirName + "\\" + fileName + ext
        os.rename(file, newPath)

def fixed_xml(path):
    for xml_file in glob.glob(path + '/*.xml'):
        baseName = os.path.basename(xml_file)
        fileName = os.path.splitext(baseName)[0]
        print(fileName)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            elmFileName = root.find('filename')
            elmFileName.text = fileName + ".jpg"
            # value = (root.find('folder').text,
            #          root.find('filename').text,
            #          root.find('path').text)
        tree.write(xml_file,encoding='UTF-8',xml_declaration=True)

        # print(value)
        


def main():
    for folder in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), ('images\\' + folder))
        # fixed_xml(image_path)
        fixed_filename(image_path)
    print('Successfully fixed fileName.')

    for folder in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), ('images\\' + folder))
        fixed_xml(image_path)
    print('Successfully fixed xml.')
    

main()