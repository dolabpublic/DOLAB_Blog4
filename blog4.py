import numpy as np
import cv2

def load_image(path_img):
    return cv2.imread(path_img)

def bgr2hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def setRangeColor(hsv, lower_color, upper_color):
    return cv2.inRange(hsv, lower_color, upper_color)

def contours_img(mask):
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def filter_contours_img(contours, img_draw, color_bbox):
    count = 0
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        area = w * h

        if area > 1000:
            count = count + 1
            cv2.rectangle(img_draw, (x, y), (x+w, y+h), color_bbox, 5)
    return img_draw, count

def draw_text_on_image(img_draw, count_yellow, count_orange):
    cv2.rectangle(img_draw, (0, 0), (500, 120), (0,0,0), -1)
    cv2.putText(img_draw,'Orange Count : ' + str(count_orange), 
        (10,50),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font 
        1.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType

    cv2.putText(img_draw,'Yellow Count : ' + str(count_yellow), 
        (10,100),                  # bottomLeftCornerOfText
        cv2.FONT_HERSHEY_SIMPLEX, # font 
        1.5,                      # fontScale
        (0,255,255),            # fontColor
        2)                        # lineType
    return img_draw

def main():
    path_img = '/workdir/Documents/DOLAB/Medium/Blog#4/images/IMG_2686.jpg'
    img = load_image(path_img)
    img = cv2.resize(img, None,fx=0.5,fy=0.5)
    hsv = bgr2hsv(img)
    img_draw = img

    # define range of Yellow color in HSV
    lower_ํYellow = np.array([20,100,100])
    upper_Yellow = np.array([45,255,255])
    mask = setRangeColor(hsv, lower_ํYellow, upper_Yellow)
    contours = contours_img(mask)
    color_bbox = (0, 0, 255)
    img_draw, count_yellow = filter_contours_img(contours, img_draw, color_bbox)
    print('Yellow Count:', count_yellow)

    # define range of Orange color in HSV
    lower_Orange = np.array([0,150,150])
    upper_Orange = np.array([20,255,255])
    mask = setRangeColor(hsv, lower_Orange, upper_Orange)
    contours = contours_img(mask)
    color_bbox = (0, 255, 0)
    img_draw, count_orange = filter_contours_img(contours, img_draw, color_bbox)

    img_draw = draw_text_on_image(img_draw, count_yellow, count_orange)
    print('Orange Count:', count_orange)

    cv2.imwrite('/workdir/Documents/DOLAB/Medium/Blog#4/output/output_IMG_2686.png', img_draw)
    


if __name__ == '__main__':
    main()






