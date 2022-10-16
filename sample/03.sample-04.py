import qrcode
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
current_dir = os.getcwd()

with open('site_list.txt','r',encoding = 'utf-8') as f:
    for a in f.readlines():
        qr_data= a.strip()
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data + '.png')
    
# qr_data= 'www.naver.com'
# qr_image = qrcode.make(qr_data)

# qr_image.save(qr_data + '.png')