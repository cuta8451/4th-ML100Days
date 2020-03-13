import numpy as np
import pandas as pd
import cv2
'''
Day5-1 作業

在小量的資料上，我們用眼睛就可以看得出來程式碼是否有跑出我們理想中的結果。請嘗試想像一個你需要的資料結構 (裡面的值是隨機的)，然後用程式碼範例的方法把它變成 DataFrame
'''
dates=pd.date_range('20200305',periods=5,freq='2D')  #從20200305開始，兩天間隔，五天期間
com_list=['CompanyA','CompanyB']
df=pd.DataFrame(np.random.randn(5,2),index=dates,columns=com_list)
print(df)


'''
1.1. 讀取 txt 檔, 請讀取 text file

https://raw.githubusercontent.com/vashineyu/slides_and_others/master/tutorial/examples/imagenet_urls_examples.txt

1.2 將所提供的 txt 轉成 pandas dataframe

2. 從所提供的 txt 中的連結讀取圖片，請讀取上面 data frame 中的前 5 張圖片
'''
data=pd.read_table('marathon\day005_imagenet_urls_examples.txt',header=None)


# catch one picture
img_ = cv2.imread('marathon\eagle.jpg')
cv2.imshow("image",img_)
cv2.waitKey()


# use url to catch top 5 picture
 
#for url_ in data[0:5][1]:
#    cap=cv2.VideoCapture(url_)
#    if( cap.isOpened() ) :
#        ret,img = cap.read()
#        cv2.imshow("image",img)
#        cv2.waitKey()

