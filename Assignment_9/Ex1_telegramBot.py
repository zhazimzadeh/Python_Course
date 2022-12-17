import telebot
import random
import khayyam 
import gtts 
import qrcode

bot = telebot.TeleBot("5946226671:AAHfR9TUSnV3P7AX8KDSIFAF3oBa1UW7sx0", parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = telebot.types.KeyboardButton('New Game')
markup.add(itembtn1)


@bot.message_handler(commands = ["start"])
def start(message):
    bot.reply_to(message, " خوش آمدی"+message.from_user.first_name +
                """ \n برای راهنمایی روی /help کلیک کن""")


@bot.message_handler(commands = ["help"])
def help(message):
    bot.reply_to(message, """/start
خوش‌آمد گویی\n 
/game
بازی حدس اعداد\n
/age
تاریخ تولدت رو با فرمت "روز/ماه/سال" وارد کن، سنت رو ببین\n
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
    UserMsg = bot.send_message(message.chat.id, "یک عدد بین 1 تا 100 حدس  بزن",reply_markup=markup)
    bot.register_next_step_handler(UserMsg, Guess_game)


@bot.message_handler(func=lambda m:True)
def Guess_game(message):
      global Num_Random
      if message.text == "New Game":
            Num_Random = random.randint(1, 100)
            UserMsg = bot.send_message(message.chat.id, "دوباره شروع کنیم. یک عدد بین 1 تا 100 حدس بزن")
            bot.register_next_step_handler(UserMsg, Guess_game)

      elif int(message.text) < Num_Random:
            UserMsg = bot.send_message(message.chat.id, "یک عدد بزرگتر حدس بزن", reply_markup = markup)
            bot.register_next_step_handler(UserMsg, Guess_game)

      elif int(message.text) > Num_Random:
            UserMsg = bot.send_message(message.chat.id, "یک عدد کوچکتر حدس بزن", reply_markup = markup)
            bot.register_next_step_handler(UserMsg, Guess_game)


      elif int(message.text) == Num_Random:
            bot.send_message(message.chat.id, "✨!آفرین درست حدس زدی", reply_markup = telebot.types.ReplyKeyboardRemove(selective = True))
           



@bot.message_handler(commands = ["age"])
def age(message):
        userMessage = bot.send_message(message.chat.id, "تاریخ تولدت رو با فرمت روز/ماه/سال وارد کن.")
        birthDate = message.text.split("/")
        difference = khayyam.JalaliDatetime.now() - khayyam.JalaliDatetime(birthDate[0], birthDate[1], birthDate[2])
        year = difference.days // 365
        difference = difference.days % 365
        month = difference // 30
        day = difference % 30 - 7
        bot.send_message(message.chat.id, "تو " + str(year) + " سال و " + str(month) + " ماه و " + str(day) + " روزه هستی.")



@bot.message_handler(commands = ["voice"])
def voice(message):
        userMessage = bot.send_message(message.chat.id, "یه جمله به انگلیسی بنویس.")
        audio = gtts.gTTS(text = message.text, lang = "en", slow = False)
        audio.save("audio.mp3")
        audio_File = open("audio.mp3", "rb")
        bot.send_voice(message.chat.id, audio_File)



@bot.message_handler(commands = ["max"])
def maximum(message):
        userMessage = bot.send_message(message.chat.id, "یک تعداد عدد وارد کن مثل14,7,78,15,8,19,20 تا بزرگترین عدد رو بهت بگم")
        numbers = list(map(int, message.text.split(",")))
        maximum = max(numbers)
        bot.reply_to(message, ":بزرگ‌ترین عدد " + str(maximum) )



@bot.message_handler(commands = ["argmax"])
def argmax(message):
        userMessage = bot.send_message(message.chat.id, "یک تعداد عدد وارد کن مثل 14,7,78,15,8,19,20تا بهت بگم بزرگترین عدد کدوم خونه است")
        numbers = list(map(int, message.text.split(",")))
        index = numbers.index(max(numbers))
        bot.reply_to(message, "موقعیت بزرگ‌ترین عدد: " + str(index + 1) )



@bot.message_handler(commands = ["qrcode"])
def QRcode(message):
        userMessage = bot.send_message(message.chat.id, "یک متن دلخواه وارد کن")
        qrcodeImage = qrcode.make(message.text)
        qrcodeImage.save("QR.jpg")
        qrcodeFile = open("QR.jpg", "rb")
        bot.send_photo(message.chat.id, qrcodeFile)





bot.infinity_polling()
