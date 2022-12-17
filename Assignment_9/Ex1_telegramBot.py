import telebot
import random
from khayyam import JalaliDatetime
from gtts import gTTS
import qrcode

bot = telebot.TeleBot("5946226671:AAHfR9TUSnV3P7AX8KDSIFAF3oBa1UW7sx0", parse_mode=None)


@bot.message_handler(commands = ["start"])
def start(message):
    bot.reply_to(message, " خوش آمدی"+message.from_user.first_name )


@bot.message_handler(commands = ["help"])
def help(message):
    bot.reply_to(message, """/start
خوش‌آمد گویی 
/game
بازی حدس اعداد\n
/age
تاریخ تولدت رو با فرمت "سال/ماه/روز" وارد کن، سنت رو ببین\n
/voice
یک جمله انگلیسی تایپ کن و صوتش رو بشنو\n
/max
یک تعداد عدد وارد کن مثل 14,7,78,15,8,19,20 تا بزرگترین عدد رو بهت بگم\n
/argmax
یک تعداد عدد وارد کن مثل 14,7,78,15,8,19,20 تا بهت بگم بزرگترین عدد کدوم خونه است\n
/qrcode
یک متن وارد کن تا بهت بارکد دوبعدیش رو نشون بدم\n
""")


@bot.message_handler(commands = ["game"])
def game(message):
    global Num_Random
    Num_Random = random.randint(1, 100)
    userMessage = bot.send_message(message.chat.id, "یک عدد بین 0 تا 100 حدس  بزن")
    bot.register_next_step_handler(userMessage, Guess_Game)


def Guess_Game(message):
    
    global Num_Random
    if message.text == "New Game":
            Num_Random = random.randint(1, 100)
            userMessage = bot.send_message(message.chat.id, "دوباره شروع کنیم. یک عدد بین 0 تا 100 حدس بزن")
            bot.register_next_step_handler(userMessage, Guess_Game)

    elif int(message.text) < Num_Random:
            userMessage = bot.send_message(message.chat.id, "یک عدد بزرگتر حدس بزن", reply_markup = markup)
            bot.register_next_step_handler(userMessage, Guess_Game)

    elif int(message.text) > Num_Random:
            userMessage = bot.send_message(message.chat.id, "یک عدد کوچکتر حدس بزن", reply_markup = markup)
            bot.register_next_step_handler(userMessage, Guess_Game)

    elif int(message.text) == Num_Random:
            bot.send_message(message.chat.id, "آفرین درست حدس زدی", reply_markup = telebot.types.ReplyKeyboardRemove(selective = True))
            



@bot.message_handler(commands = ["age"])
def age(message):
    userMessage = bot.send_message(message.chat.id, "تاریخ تولدت رو با فرمت سال/ماه/روز وارد کن.")
    bot.register_next_step_handler(userMessage, Age_Calculator)


def Age_Calculator(message):
        birthDate = message.text.split("/")
        difference = JalaliDatetime.now() - JalaliDatetime(birthDate[0], birthDate[1], birthDate[2])
        year = difference.days // 365
        difference = difference.days % 365
        month = difference // 30
        day = difference % 30 - 7
        bot.send_message(message.chat.id, "تو " + str(year) + " سال و " + str(month) + " ماه و " + str(day) + " روزه هستی.")



@bot.message_handler(commands = ["voice"])
def voice(message):
    userMessage = bot.send_message(message.chat.id, "یه جمله به انگلیسی بنویس.")
    bot.register_next_step_handler(userMessage, voiceMaker)


def voiceMaker(message):
        audio = gTTS(text = message.text, lang = "en", slow = False)
        audio.save("audio.mp3")
        audio_File = open("audio.mp3", "rb")
        bot.send_voice(message.chat.id, audio_File)



@bot.message_handler(commands = ["max"])
def maximum(message):
    userMessage = bot.send_message(message.chat.id, "یک تعداد عدد وارد کن مثل14,7,78,15,8,19,20 تا بزرگترین عدد رو بهت بگم")
    bot.register_next_step_handler(userMessage, maxNumber)


def maxNumber(message):
        numbers = list(map(int, message.text.split(",")))
        maximum = max(numbers)
        bot.reply_to(message, ":بزرگ‌ترین عدد " + str(maximum) )



@bot.message_handler(commands = ["argmax"])
def argmax(message):
    userMessage = bot.send_message(message.chat.id, "یک تعداد عدد وارد کن مثل 14,7,78,15,8,19,20تا بهت بگم بزرگترین عدد کدوم خونه است")
    bot.register_next_step_handler(userMessage, maxIndex)


def maxIndex(message):
        numbers = list(map(int, message.text.split(",")))
        index = numbers.index(max(numbers))
        bot.reply_to(message, "موقعیت بزرگ‌ترین عدد: " + str(index + 1) )



@bot.message_handler(commands = ["qrcode"])
def QRcode(message):
    userMessage = bot.send_message(message.chat.id, "یک متن دلخواه وارد کن")
    bot.register_next_step_handler(userMessage, QRcodeMaker)


def QRcodeMaker(message):
        qrcodeImage = qrcode.make(message.text)
        qrcodeImage.save("QR.jpg")
        qrcodeFile = open("QR.jpg", "rb")
        bot.send_photo(message.chat.id, qrcodeFile)



markup = telebot.types.ReplyKeyboardMarkup(row_width = 1)
button = telebot.types.KeyboardButton("New Game")
markup.add(button)

bot.infinity_polling()
