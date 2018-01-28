from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import os

print("Program have started")

# Сколько прошло дней до наступления текущего месяца
months = [31, 59, 90, 120, 151, 181, 212, 233, 263, 294, 324]

# Сегодняшний день и месяц
data = time.strftime("%d %m").split(" ")

# Подсчет номера текущего дня
if int(data[1]) > 1:
    todayIs = int(data[0]) + months[int(data[1])-2]
else:
    todayIs = int(data[0])

# Получить список всех файлов в папке image
osi = os.listdir("/home/nigma/Projects/ImageChanger/image")

# Если текущая картинка правильная, то сделать ее обоями,
# иначе сделать картинку с сегоднящней датой и поставиьт ее на обои
if int(osi[0].split(".")[0]) == todayIs:
    os.system("feh --bg-scale /home/nigma/Projects/ImageChanger/image/" + osi[0])
else:
    im = Image.open("/home/nigma/Pictures/wallpaperbest4kworked.jpg")

    text_font = ImageFont.truetype("/home/nigma/Projects/ImageChanger/fonts/AmaticSC-Bold.ttf", 350)
    text_color = (239, 240, 240)

    text = "Страница"

    draw = ImageDraw.Draw(im)

    # Для каждого разряда определенно расположен текст
    if todayIs < 10:
        text_position = (750, 700)
        text += "    " + str(todayIs) + "    из   365"
    elif todayIs < 100:
        text_position = (810, 700)
        text += "  " + str(todayIs) + "   из   365"
    else:
        text_position = (780, 700)
        text += " " + str(todayIs) + "   из   365"


    draw.text(text_position, text, text_color, text_font)
    draw.text((1150, 1075), "ВПЕРЕДИ ДОЛГИЙ ПУТЬ", text_color,
              ImageFont.truetype("/home/nigma/Projects/ImageChanger/fonts/AmaticSC-Bold.ttf", 250))

    os.remove("/home/nigma/Projects/ImageChanger/image/"+str(osi[0]))
    im.save("/home/nigma/Projects/ImageChanger/image/"+str(todayIs)+".jpg")

    os.system("feh --bg-scale /home/nigma/Projects/ImageChanger/image/" + str(todayIs) + ".jpg")
    os.system("feh --bg-scale /home/nigma/Projects/ImageChanger/image/" + str(todayIs) + ".jpg")



