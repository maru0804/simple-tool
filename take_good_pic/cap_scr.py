# ４枚の準備画像に対してカメラから取得した画像をそれぞれ比較し、スコアを計算して、総スコアを求めるプログラム
import cv2
import os
import numpy as np
from PIL import Image

# メイン関数ではカメラの処理をメインで記述する
def main():
    cap = cv2.VideoCapture(0)
    cnt = 0
    scr = 0
    while(True):
        # Capture　スタート
        ret, frame = cap.read()

        # １秒に１フレーム取得して 
        if cnt == 30:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            pil_img = Image.fromarray(gray)
            im_crop = pil_img.crop((280, 0, 1000, 720))
            im_crop = np.array(im_crop)
            img = cv2.resize(im_crop, (200,200))

            scr = comp_img(img)

            print(scr)
            if scr >= 148:
                cv2.imwrite('save_img/scr{}.jpg'.format(int(scr)), img)
                print("-------save---------")

            cnt = 0
        # 画面上への描画処理
        cv2.putText(frame, '{}'.format(int(scr)), (200, 600), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), thickness=2)
        cv2.line(frame, (280, 0), (280, 720), (0, 255, 0), thickness=4, lineType=cv2.LINE_AA)
        cv2.line(frame, (1000, 0), (1000, 720), (0, 255, 0), thickness=4, lineType=cv2.LINE_AA)
        # 画面表示
        cv2.imshow('frame',frame)
        cnt += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 終了処理
    cap.release()
    cv2.destroyAllWindows()

    # ４枚のテスト画像で複数画像の比較するテストを行うtest関数
    # test()
    
# 画像を読み込みリサイズする関数
def read_and_resize(img_path):
    IMG_SIZE = (200, 200)
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, IMG_SIZE)
    return img

# トータルスコアを計算し返す関数
def cul_scr(scr_list, cnt):
    sum = 0
    for scr in scr_list:
        sum += scr
    ans = sum / cnt
    return ans

# スコアリストを返す関数
def get_scr_list(my_face_img):
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    detector = cv2.AKAZE_create()
    (target_kp, target_des) = detector.detectAndCompute(my_face_img, None)
        
    scr_list = []

    IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/comp_images/'
    files = os.listdir(IMG_DIR)
    
    for file in files:
    # 同名もしくはターゲットファイル以外を取得
        if file == '.DS_Store':
            continue
        comparing_img_path = IMG_DIR + file
        comp_img = read_and_resize(comparing_img_path)

        (comparing_kp, comparing_des) = detector.detectAndCompute(comp_img, None)

        matches = bf.match(target_des, comparing_des)
        dist = [m.distance for m in matches]
        scr = sum(dist) / len(dist)
        scr_list.append(scr)
    
    return scr_list

# 受け取った画像と準備画像を比較する
def comp_img(img):  
    scr_list = get_scr_list(img)
    print(scr_list)
    cnt = 4
    scr = cul_scr(scr_list, cnt)
    return scr

# ４枚のテスト画像で複数画像の比較するテストを行う
def test():
    IMG_DIR = os.path.abspath(os.path.dirname(__file__)) + '/images/'
    files = os.listdir(IMG_DIR)
    for file in files:
        # 同名もしくはターゲットファイル以外を取得
        if file == '.DS_Store':
            continue

        img_path = IMG_DIR + file
        try:
            my_face_img = read_and_resize(img_path)
            scr = comp_img(my_face_img)
            print(file, scr)

        except cv2.error:
            ret = 100000
            print(file, ret)

if __name__ == "__main__":
    main()