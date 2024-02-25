# import asyncio
# import types
#
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message
# from aiogram.filters import Command
# import logging
# import random
# from button1 import keyboard1, sezonkey, keyboard2, kiyim1, board1,help1
# from inlinekeyboarsd import inline
# from aiogram import types
#
# logging.basicConfig(level=logging.INFO)
#
# mytoken = '6522409645:AAHZUmVprtZIwYySBeTwzJKg6nXjVrlYAu0'
#
# bot = Bot(token=mytoken, parse_mode="HTML")
# dp = Dispatcher()
# galochka = "✔️"
#
# rasm1 = "https://t4.ftcdn.net/jpg/05/50/95/87/360_F_550958748_OeGcRonEUNoVhd0wjd9zSEMhLFIGO9Bt.jpg"
# rasm2 = "https://images.unsplash.com/photo-1509479200622-4503f27f12ef?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGhhY2tlcnxlbnwwfHwwfHx8MA%3D%3D"
# rasm3 = "https://t3.ftcdn.net/jpg/05/56/29/10/360_F_556291020_q2ieMiOCKYbtoLITrnt7qcSL1LJYyWrU.jpg"
# rasm4 = "https://i.pinimg.com/550x/d3/a5/b7/d3a5b77b86f84e2d55a09605cdcbb666.jpg"
# rasm5 = "https://w0.peakpx.com/wallpaper/165/445/HD-wallpaper-neon-mask-hacker-hackers-lonely-hacker-neon-mask.jpg"
# rasm6 = "https://c4.wallpaperflare.com/wallpaper/220/261/280/anarchy-anonymous-binary-code-wallpaper-preview.jpg"
#
# quarter2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAQgQ5Z43K72j-eOntChrksbSDHvOqqeTm6Q&usqp=CAU"
# question1 = "https://tinker.ly/wp-content/uploads/2022/10/1_RJMxLdTHqVBSijKmOO5MAg.jpeg"
#
#
# @dp.message(Command("start"))
# async def cmd_start(message: Message):
#     await message.answer(
#         f"<b>salom {message.from_user.full_name} botga xush kelibsiz{galochka} bizni botimizda nimalar borligini bilishni xoxlasangiz /help ni ustiga bosing </b>")
#     print(message.from_user.full_name)
#
#     @dp.message(Command("help"))
#     async def cmd_help(message2: Message):
#         await message2.answer(
#             f" <b> 1. /question --> ni ustiga bossangiz python haqida malumotlarni bilib olasiz!\n2.  /Hacker_Photo --> sizga hacker rasmlarini random tarzida chiqarib beradi\n3. /Full_Photo --> sizga botda bor rasmlarni hamasin chiqarib beradi\n4. /Muzic  --> sizga botda bor muzikalarni tashlab beradi \n5. /contact_and_location --> ? \n\n6. /Mahsulotlar --> sizga turli xil telefonlar sotib olishizga yordam beradi</b>",reply_markup=help1,
#             parse_mode="HTML")
#
#
# @dp.message(Command("Muzic"))
# async def audio(message: Message):
#     await message.reply_audio(audio="https://file.muznavo.net/mp3/dilmurod-sultonov-onalarga-yuz-yosh-bersin.mp3")
#
#
# @dp.message(Command("Foto"))
# async def rasm(message0: Message):
#     imageList = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6]
#     img = random.choice(imageList)
#     await message0.answer_photo(photo=f"{img}")
#
#
# @dp.message(Command("Full_Photo"))
# async def full(message7: Message):
#     imageList = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6]
#     for i in imageList:
#         await message7.answer_photo(photo=i)
#
#         @dp.message(Command("question"))
#         async def javob(message: Message):
#             await message.answer("""<b> 🟢savol
#
# 1) Python nima? va kim tomonidan yaratilgan?
#
# 2) Nima uchun aynan Python dasturlash tili?
#
# 3) Python dasturlash tili qachon ishlab chiqarilgan?
#
# 4) Python da Web dasturlash.
#
# 5) Python da Suniy intilekt AI.\n\n Javobni bilmoqchi bosez /Answer ni ustizga bosing va savolni raqamini kiriting!</b>""")
#
#             @dp.message(Command("Answer"))
#             async def cmd_javob(message: Message):
#                 if message.text == "1":
#                     await message.answer_photo(photo=question1, caption="""<b>
# Python maʼlumotlar tahlili, mashinani oʻrganish, DevOps va veb-ishlab chiqishda, shu jumladan oʻyinlarni ishlab chiqishda qoʻllaniladigan eng mashhur tillardan biri hisoblanadi.  O'qilishi, sodda sintaksisi va kompilyatsiya etishmasligi tufayli til dasturlashni o'rgatish uchun juda mos keladi, bu sizga algoritmlar, tushunchalar va paradigmalarni o'rganishga e'tiboringizni qaratish imkonini beradi.  Nosozliklarni tuzatish va eksperiment o'tkazishga tilning talqin qilinishi katta yordam beradi.  Bu tildan Google yoki Facebook kabi koʻplab yirik kompaniyalar foydalanadi..</b>""")
#
#                     await message.answer_photo(photo=quarter2, caption="""Python tashkil topgan yili: 1991-yil 20-fevral
#
#
#
# Avtor: Guido van Rossum
#
# Dasturchi: Python Software Foundation va Gvido van Rossum
#
# Rasmiy sayt: python.org """)
#                 elif message.text == "2":
#                     await message.reply("""<b>
# Bu dasturlash tili o'rganish uchun oson, foydalanish uchun qulay, ko'p qirrali dasturlash tili bo'lib, dasturlashga yangi kirganlar uchun ham, soha mutaxassislari uchun ham zo'r tanlov.
#
# Python turli xil platformalarda ishlaydi (Windows, Mac, Linux, Raspberry Pi va boshqalar).
#
# Python ingliz tiliga o'xshash oddiy sintaksisga ega.
# Python dasturlash tiliga bo'lgan talab yildan yilga oshib kelmoqda. CodingDojo portalining tadqiqotlariga ko'ra, 2020 yilda aynan Python tilida dasturlovchi mutaxassislarga eng ko'p talab bo'lgan.
#
# Python Artificial Intelligence (Sun'iy intellekt) va Data Science (Ulkan ma'lumotlar bilan ishlash) sohalarining tili hisoblanadi. Bugungi kunda keng ommalashib borayotgan sun'iy intellekt asosida ishlovchi dasturlarning aksari Pythonda yozilgan. Bu sohalardagi mutaxassislar bugungi kunda eng noyob va qimmatbaho kadrlar hisoblanadi.
# Keng qamrovli va universal til. Python dasturlari deyarli barcha operativ tizimlarda va platformalarda ishlaydi.
#
# O'rganish uchun ham, tushunish uchun ham juda qulay va sodda kod.
#
# Moslashuvchanlik Python dasturlash tili ma'lum bir masalalarni yechish bilan chegaralanmagan. Bu til dasturchilarga yangi va yangi yo'nalishlarga ki'rish imkonini beradi. Python quyidagi sohalarda qo'llaniladi: Web va Internet dasturlash, kompyuter o'yinlarini yaratish, ma'lumotlar bazasi bilan ishlash (DB), computer vision, foydalanuvchilar uchun grafik interfeys (GUI), juda tez rivojlanayotgan buyumlar interneti (IoT) texnologiyasi va hokazo.</b>""")
#                 elif message.text == "3":
#                     await message.reply("""
#                         Python - mashhur dasturlash tili. U Guido van Rossum tomonidan 1991 yilda ishlab chiqilgan.""")
#                 elif message.text == "4":
#                     await message.reply("""<b>
#                         Python veb-saytlarni ishlab chiqish uchun bir qator frameworklar bor. Mashhur frameworklar Django, Flask, Pylons va boshqalar. Ushbu frameworklar Python-da yozilganligi sababli , kodni tez va barqaror qilishiga asosiy sabab .
#
#                         Boshqa veb-saytlardan ma'lumotlarni olish mumkin bo'lgan joylarda veb-qirqishlarni ham amalga oshirishingiz mumkin. Shuningdek, Instagram, bit chelak, Pinterest kabi ko'plab veb-saytlar faqat ushbu frameworklar bilan yozilgan.Yana bir pythonni gigant kompanyalar ishlatishi misol uchun google, facebook va boshqalar.</b>""")
#                 elif message.text == "5":
#                     await message.reply("""<b>
#                         AI texnologiya dunyoda tez va jadal rivojlanib borayotgan yo'nalishlardan biri.Siz aslida inson miyasiday o'ylaydigan, tahlil qiladigan va qaror qabul qiladigan robotlar yaratishingiz mumkin.Bularni barchasini Keras va TensorFlow kutubxonalari bilan qilsa bo'ladi.Hozirda o'zim ham computer vision sohasida bir-ikkita loyihalar ham qilyapman. Computer vision bu rasmga qarab uni kimligini va uni harakatlarini aniqlaydigan yo'nalishlar bu albatta pythonda sodda ko'p qatorlik kod yozmaydi. Buni amalga oshirish uchun openCv kabi kutubxonalar mavjud.</b>""")
#                 else:
#                     await message.reply("<b> Bu sonda savol mavjud emas!</b>",
#                                         parse_mode="HTML")
#
#
# @dp.message(Command("contact"))
# async def contact(message: Message):
#     f = message.from_user.full_name
#     await message.answer_contact("+998-90-555-54-55", first_name=f)
#
#     await message.answer_contact("+998-90-555-54-55", first_name=f)
#
#
# @dp.message(Command("Mahsulotlar"))
# async def cmd_shop(message: Message):
#     await message.answer_photo(photo="https://images.app.goo.gl/YV8Erkdhx15kKXWU6", reply_markup=keyboard1)
#
#     @dp.message(F.text == "Kiyimlar")
#     async def kiyim(message: Message):
#         await message.answer_photo(photo="https://images.app.goo.gl/ovGFKdZmGYA4WnsL8",
#                                    caption="siz qanaqa koylak harid qilmoqchisiz Erkak yoki Ayol\n\nPastdagi bolimlardan bittasini tanlang❗️",
#                                    reply_markup=board1)
#
#         @dp.message(F.text == "Ayol")
#         async def ayol(message: Message):
#             await message.answer("qaysi fasldagi kiyimlarni xarid qilmoqchisiz?", reply_markup=sezonkey)
#
#             @dp.message(F.text == "Qish 🥶")
#             async def qish(message: Message):
#                 await message.answer_photo(
#                     photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3Jb9zW3YC-IdUzGUttcg3bT0a3ESvG7fgx73RMJ0erfj7qegIVgkSoIjzBIJ-gMNhmNM&usqp=CAU",
#                     caption="sizga qanaqa kiyim kerak?\n\nPastdagi bolimlardan bittasini tanlang❗️",
#                     reply_markup=kiyim1)
#
#             @dp.message(F.text == "Jenfir")
#             async def jenfr(message: Message):
#                 await message.answer_photo(photo="https://i.ebayimg.com/images/g/DrQAAOSwGPRhPFjU/s-l1200.webp",
#                                            caption="Narxi --> 200 min\nRangi --> kulrang , Qizil , Qora ranglilari bor\nichi mexli🧸\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️",
#                                            reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "kurtka")
#             async def jenfr(message: Message):
#                 await message.answer_photo(
#                     photo="https://charisma.ua/image/cache/catalog/H21FL306.542/1-1100x1400.jpg",
#                     caption="Narxi --> 230 min\nRangi --> Oq\nichi mexli🧸\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️",
#                     reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "Etik")
#             async def etik(message: Message):
#                 await message.answer_photo(
#                     photo="https://ae01.alicdn.com/kf/S998ee1ad5a8c44be8c436240cbbacaadE.jpg?width=800&height=800&hash=1600",
#                     caption="Narxi --> 260 min\nRangi --> seriy\nRazmeri --> 36 dan 40 gacha\nichi mexli🧸\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️",
#                     reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "Shapka")
#             async def etik(message: Message):
#                 await message.answer_photo(
#                     photo="https://images.prom.ua/3314322134_w640_h640_shapka-girl-v.jpg",
#                     caption="Narxi --> 60 min\nRangi --> seriy, qizil, sariq, pushti, kulrang, malochniy\n\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️",
#                     reply_markup=inline.as_markup())
#
#         @dp.message(F.text == "Kiyimlar")
#         async def kiyim(message: Message):
#             await message.answer_photo(photo="https://images.app.goo.gl/ovGFKdZmGYA4WnsL8",
#                                            caption="siz qanaqa koylak harid qilmoqchisiz Erkak yoki Ayol\n\nPastdagi bolimlardan bittasini tanlang❗️",
#                                            reply_markup=board1)
#
#         @dp.message(F.text == "Erkak")
#         async def erkak(message: Message):
#             await message.answer("qaysi fasldagi kiyimlarni xarid qilmoqchisiz?", reply_markup=sezonkey)
#
#             @dp.message(F.text == "Qish 🥶")
#             async def qish1(message: Message):
#                 await message.answer_photo(
#                     photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT3Jb9zW3YC-IdUzGUttcg3bT0a3ESvG7fgx73RMJ0erfj7qegIVgkSoIjzBIJ-gMNhmNM&usqp=CAU",
#                     caption="sizga qanaqa kiyim kerak?\n\nPastdagi bolimlardan bittasini tanlang❗️",
#                     reply_markup=kiyim1)
#
#             @dp.message(F.text == "Jenfir")
#             async def jenfr_erkak(message: Message):
#                 await message.answer_photo(photo="https://m.media-amazon.com/images/I/51onyOZk1IL._AC_UY780_.jpg",
#                                            caption="Narxi --> 100 min\nRangi --> Kulrang, Oq, Jigarang, Qora\n\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️ ",
#                                            reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "kurtka")
#             async def kurtka_erkak(message: Message):
#                 await message.answer_photo(
#                     photo="https://www.mr.dk/img/684/855/resize/1/0/10081796_JET_BLACK_SL_FAUX_0_73a1.jpg",
#                     caption="Narxi --> 180 min\nRangi --> Qora\n\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️ ",
#                     reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "Etik")
#             async def etik_erkak(message: Message):
#                 await message.answer_photo(
#                     photo="https://olcha.uz/image/400x400/products/supplier/stores/1/2023-09-10/aj7TZ9ioyoumvoZgio6knEh0fvepJnBGMRJEslfuvpWg3TTcPVB9gHr8XD9s.jpg",
#                     caption="Narxi --> 210 min\nRangi --> Jigarang\n\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️ ",
#                     reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "Shapka")
#             async def etik_erkak(message: Message):
#                 await message.answer_photo(photo="https://images.uzum.uz/ccv199jb3ho5lmuq0n7g/original.jpg",
#                                            caption="Narxi --> 60 min\nRangi --> Oq, Qora, Kulrang\n\n➡️sizga yoqdimi❤️?⬅️\n\n➡️yoqqan bo'lsa sotib olish uchun pastdagi odamga murojat qiling👇🏼🛍❗️ ",
#                                            reply_markup=inline.as_markup())
#
#         @dp.message(F.text == "Texnika")
#         async def phone(message1: types.Message):
#             await message1.answer_photo(photo="https://images.app.goo.gl/U55LL6bxFwGffQK38",
#                                         caption="<b>\nQanaqa telefonni xarid oloqchisiz❓\n\nPastdagi bolimlardan bittasini tanlang❗️</b>",
#                                         reply_markup=keyboard2, parse_mode="HTML")
#
#             @dp.message(F.text == "Iphone")
#             async def cmd_Iphone(message: types.Message):
#                 await message.answer_photo(photo="https://images.app.goo.gl/ggauiCr5u9GuSo2f6",
#                                            caption="<b>nomi --> Iphone \n yili --> 2022 \n joyi --> 256 gb\n rangi --> qora\n narxi --> 800$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
#                                            parse_mode="HTML", reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "Samsung")
#             async def cmd_samsung(message: types.Message):
#                 await message.answer_photo(
#                     photo="https://unsplash.com/photos/black-sony-remote-control-beside-white-tissue-paper-uCqMa_s-JDg",
#                     caption="<b>nomi --> Galaxy S21 Ultra\nyili --> 2022\njoyi --> 256 gb \nrangi --> qora \nnarxi --> 650$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
#                     parse_mode="HTML", reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "Redmi")
#             async def cmd_Redmi(message: types.Message):
#                 await message.answer_photo(photo="https://s0.rbk.ru/v6_top_pics/media/img/9/38/756669508108389.webp",
#                                            caption="<b>nomi --> Redmi not 12c \n yili --> 2022 \n joyi --> 128 gb\n rangi --> qora\n narxi --> 800$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
#                                            parse_mode="HTML", reply_markup=inline.as_markup())
#
#             @dp.message(F.text == "vivo")
#             async def cmd_vivo(message: types.Message):
#                 await message.answer_photo(
#                     photo="https://grab.mobile2go.com.my/images/thumbs/0018082_vivo-y76-5g-8gb4gb-ram-128gb-rom-original-vivo-malaysia_511.png",
#                     caption="<b>nomi --> Vivo Y76 5G \n yili --> 2022 \n joyi --> 128 gb\n rangi --> Gold\n narxi --> 300$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
#                     parse_mode="HTML", reply_markup=inline.as_markup())
#
#
# @dp.message(Command("contact_and_location"))
# async def cmd_special_buttons(message: types.Message):
#     kb1 = [
#
#         [types.KeyboardButton(text="Lokatsiya olish", request_location=True)],
#         [types.KeyboardButton(text="Contact yuborish", request_contact=True)],
#
#     ]
#
#     keyboard = types.ReplyKeyboardMarkup(
#         keyboard=kb1,
#         resize_keyboard=True,
#         input_field_placeholder="Word"
#     )
#     await message.answer("Как подавать котлеты?", reply_markup=keyboard)
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
