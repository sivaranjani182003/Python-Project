from PIL import Image,ImageDraw,ImageFont
import random
import os
import datetime
import qrcode
Image=Image.new('RGB',(1000,900),(255,255,255))
draw=ImageDraw.Draw(Image)
font=ImageFont.truetype('arial.ttf',size=45)
os.system('ID CARD GENERATOR')
d_date=datetime.datetime.now()
reg_format_date=d_date.strftime('%d-%m-%Y\t ID CARD GENERATOR\t %I:%M:%S')
print(reg_format_date)
print('n\nall fields are mandatory')
print('avoid any kind of spelling mistakes')
print('write everything in uppercase letters')
(x,y)=(50,50)
message=input('\nEnter your company name:')
company=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=80)
draw.text((x,y),message,fill=color,font=font)
(x,y)=(600,75)
idno=random.randint(10000000,90000000)
message=str('ID'+str(idno))
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)
(x,y)=(50,250)
message=input('Enter your full name')
name=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=45)
draw.text((x,y),message,fill=color,font=font)
(x,y)=(50,350)
message=input('Enter your gender:')
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y)=(250,350)
message=input('enter your age:')
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y)=(50,450)
message=input('Enter your date of birth:')
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y)=(50,550)
message=input('Enter your blood group:')
color='rgb(255,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y)=(50,650)
message=input('Enter your mobile number:')
temp=message
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
(x,y)=(50,750)
message=input('Enter your address')
color='rgb(0,0,0)'
draw.text((x,y),message,fill=color,font=font)
image.save(str(name)+'.png')
img=qrcode.make(str(company)+str(idno))
img.save(str(idno)+'bmp')
till=Image.open(name+'.png')
im=Image.open(str(idno)+'.bmp')
till.paste(im,(600,350))
till.save(name+'.png')
print(('\n\n\nyour ID card successfully created in a png file '+name+'.png'))
eval(input('\n\npress any key to close program...'))