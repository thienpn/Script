"""
Convert label from Label Me format (.xml) to label for train SCRFD
XML:

<annotation>
  <filename>09_05_image_20200515000803127_008.jpg</filename>
  <folder></folder>
  <source>
    <sourceImage></sourceImage>
    <sourceAnnotation>Datumaro</sourceAnnotation>
  </source>
  <imagesize>
    <nrows>540</nrows>
    <ncols>720</ncols>
  </imagesize>
  <object>
    <name>plate</name>
    <deleted>0</deleted>
    <verified>0</verified>
    <occluded>no</occluded>
    <date></date>
    <id>0</id>
    <parts>
      <hasparts></hasparts>
      <ispartof></ispartof>
    </parts>
    <polygon>
      <pt>
        <x>224.00</x>
        <y>342.00</y>
      </pt>
      <pt>
        <x>225.00</x>
        <y>381.00</y>
      </pt>
      <pt>
        <x>377.00</x>
        <y>383.00</y>
      </pt>
      <pt>
        <x>377.00</x>
        <y>344.00</y>
      </pt>
      <username></username>
    </polygon>
    <attributes>ocr=93A07015</attributes>
  </object>
</annotation>

Label for SCRFD train (txt):

# <image_path> image_width image_height
bbox_x1 bbox_y1 bbox_x2 bbox_y2 (<keypoint,3>*N)
"""


import cv2
import xmltodict
from glob import glob
import os
imgs_path = "labeled/imgs/"
annos_path = "labeled/annos/"
label_path = 'labelv2.txt'
image_paths = glob(imgs_path + '*.jpg', recursive=True) + glob(imgs_path + '*.png', recursive=True)
labels = open(label_path,'w')
for img in image_paths:
    image = cv2.imread(img)
    line1 = '# %s %d %d\n'%(img,image.shape[1], image.shape[0])
    labels.write(line1)
    file_xml = open(annos_path+os.path.basename(img)[:-3]+'xml')
    annotation = xmltodict.parse(file_xml.read())
    if isinstance(annotation['annotation']['object'],dict):
        list_obj = [annotation['annotation']['object']]
    elif isinstance(annotation['annotation']['object'],list):
        list_obj = annotation['annotation']['object']
    for object in list_obj:
        bbox = False
        if 'type' in object:
            if object['type'] == 'bounding_box':
                bbox = True
            else:
                print("image error: ",img)
                print('type: ', object['type']) 
        else:
            pass
        
        kps = []
        point_list = object['polygon']['pt']
        if bbox == False:
            for pt in object['polygon']['pt']:
                kps.append('%.5f'%float(pt['x']))
                kps.append('%.5f'%float(pt['y']))
                kps.append('%.5f'%float(1.))
            kps_str = ' '.join(["%s" %pt for pt in kps])
            x1, y1 = float(point_list[0]['x'])- 5, float(point_list[0]['y'])- 5
            x2, y2 = float(point_list[2]['x'])+ 5, float(point_list[2]['y'])+ 5 
        if bbox == True:
            x1, y1 = float(point_list[0]['x']), float(point_list[0]['y'])
            x2, y2 = float(point_list[2]['x']), float(point_list[2]['y'])   
            kps = ['%.5f'%float(-1.)]*12
            kps_str = ' '.join(["%s" %pt for pt in kps])
        line2 = '%.5f %.5f %.5f %.5f %s\n'%(x1,y1,x2,y2,kps_str)
        labels.write(line2)
