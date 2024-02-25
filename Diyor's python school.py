import asyncio
import types

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import logging
import random
from Texnika import users, value, keys, top, Bank, phone1,samsun
from button1 import python1
from button2 import pomosh
from inlinekeyboarsd import inline
from aiogram import types


logging.basicConfig(level=logging.INFO)

mytoken = '6522409645:AAHZUmVprtZIwYySBeTwzJKg6nXjVrlYAu0'

bot = Bot(token=mytoken, parse_mode="HTML")
dp = Dispatcher()
galochka = "✔️"







async def start_answer(bot: Bot):
    await bot.send_message(1747966069, "Bot ishga tushdi")

async def stop_answer1(bot: Bot):
    await bot.send_message(1747966069, "Bot toxtadi")

rasm1 = "https://t4.ftcdn.net/jpg/05/50/95/87/360_F_550958748_OeGcRonEUNoVhd0wjd9zSEMhLFIGO9Bt.jpg"
rasm2 = "https://images.unsplash.com/photo-1509479200622-4503f27f12ef?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjB8fGhhY2tlcnxlbnwwfHwwfHx8MA%3D%3D"
rasm3 = "https://t3.ftcdn.net/jpg/05/56/29/10/360_F_556291020_q2ieMiOCKYbtoLITrnt7qcSL1LJYyWrU.jpg"
rasm4 = "https://i.pinimg.com/550x/d3/a5/b7/d3a5b77b86f84e2d55a09605cdcbb666.jpg"
rasm5 = "https://w0.peakpx.com/wallpaper/165/445/HD-wallpaper-neon-mask-hacker-hackers-lonely-hacker-neon-mask.jpg"
rasm6 = "https://c4.wallpaperflare.com/wallpaper/220/261/280/anarchy-anonymous-binary-code-wallpaper-preview.jpg"

quarter2 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAQgQ5Z43K72j-eOntChrksbSDHvOqqeTm6Q&usqp=CAU"
question1 = "https://tinker.ly/wp-content/uploads/2022/10/1_RJMxLdTHqVBSijKmOO5MAg.jpeg"


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"<b>🎉 Tabriklaymiz {message.from_user.full_name} botga xush kelibsiz!\nKerakli bo'limni tanlang.👇 </b>",
        reply_markup=pomosh, parse_mode="HTML")
    print(message.from_user.full_name)

    @dp.message(F.text == "💬 Biz bilan aloqa")
    async def cmdd(message: Message):
        await message.answer("💬 Biz bilan aloqa", reply_markup=inline.as_markup())

    @dp.message(F.text == "🌐 Python haqida")
    async def cmd_python(message: Message):
        await message.answer_photo(photo=question1, caption="""<b>
Python maʼlumotlar tahlili, mashinani oʻrganish, DevOps va veb-ishlab chiqishda, shu jumladan oʻyinlarni ishlab chiqishda qoʻllaniladigan eng mashhur tillardan biri hisoblanadi.  O'qilishi, sodda sintaksisi va kompilyatsiya etishmasligi tufayli til dasturlashni o'rgatish uchun juda mos keladi, bu sizga algoritmlar, tushunchalar va paradigmalarni o'rganishga e'tiboringizni qaratish imkonini beradi.  Nosozliklarni tuzatish va eksperiment o'tkazishga tilning talqin qilinishi katta yordam beradi.  Bu tildan Google yoki Facebook kabi koʻplab yirik kompaniyalar foydalanadi..</b>""")
        await message.answer_photo(photo=quarter2, caption="""Python tashkil topgan yili: 1991-yil 20-fevral
 Avtor: Guido van Rossum
 
 Dasturchi: Python Software Foundation va Gvido van Rossum
 
 Rasmiy sayt: python.org """, reply_markup=python1)

    @dp.message(F.text == "0 dan o'rganish 📚")
    async def cmd(message: Message):
        await message.answer("hozircha hech nima yo'q!", reply_markup=pomosh)

    @dp.message(F.text == "Python va sun'iy intellekt 🦾")
    async def cmd1(message: Message):
        await message.answer("hozircha hech nima yo'q!", reply_markup=pomosh)

    @dp.message(F.text == "📸 Foto")
    async def cmd_photo(message: Message):
        imageList = [rasm1, rasm2, rasm3, rasm4, rasm5, rasm6]
        img = random.choice(imageList)
        await message.answer_photo(photo=f"{img}")

    @dp.message(F.text == "🎼 Musiqa")
    async def cmd_music(message: Message):
        await message.answer_audio(audio="https://file.muznavo.net/mp3/dilmurod-sultonov-onalarga-yuz-yosh-bersin.mp3")

    @dp.message(F.text == "🛒 Xarid qilish")
    async def cmd_magazin(message: Message):
        await message.answer_photo(photo="https://images.app.goo.gl/kdz9wzFs81AgKGVQA", reply_markup=value)

        @dp.message(F.text == "Texnika")
        async def phone(message1: types.Message):
            await message1.answer(
                "<b>\nQanaqa telefonni xarid oloqchisiz❓\n\nPastdagi bolimlardan bittasini tanlang❗️</b>",
                reply_markup=users, parse_mode="HTML")

            @dp.message(F.text == "Noutbuk")
            async def noutbuk(message1: Message):
                await message1.answer("O'zingizga kerakli noutbukni tanlang!", reply_markup=top)

                @dp.message(F.text == "HP")
                async def laptop(message1: Message):
                    await message1.answer_photo(photo="https://images.app.goo.gl/pKjaVHxFrT6C3CSp6",
                                                caption="Nomi --> HP x360\njoyi --> 256\nrangi --> Kulrang, Qora, Oq\nYili --> 2024 yangi\nnarxi --> 950$\n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️",
                                                reply_markup=inline.as_markup())

                @dp.message(F.text == "Acer")
                async def laptop1(message1: Message):
                    await message1.answer_photo(photo="https://images.app.goo.gl/XyZ33PChhzd29jSC8",
                                                caption="Nomi --> Acer tez va katta monitor\njoyi --> 512\nYili --> 2024 hali yangi\nnarxi --> 11.000$\n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️",
                                                reply_markup=inline.as_markup())

                @dp.message(F.text == "Lenovo")
                async def laptop2(message1: Message):
                    await message1.answer_photo(photo="https://images.app.goo.gl/LKjNu1iZXTvpS4jDA",
                                                caption="nomi --> Lenovo\nmalumot --> gamerla uchun\nyili --> 2024 hali yangi\nnarxi --> 700$\n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️",
                                                reply_markup=inline.as_markup())

                @dp.message(F.text == "Macbook")
                async def laptop3(message1: Message):
                    await message1.answer_photo(
                        photo="https://unsplash.com/photos/black-sony-remote-control-beside-white-tissue-paper-uCqMa_s-JDg",
                        caption="<b>nomi --> Macbook \n yili --> 2024 \n joyi --> 1 tb gb\n rangi --> kulrang\n narxi --> 12.000$ \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                        parse_mode="HTML", reply_markup=inline.as_markup())

            @dp.message(F.text == "Telefon")
            async def phone(message1: Message):
                await message1.answer("O'zingizga kerakli telefponi tanlang!", reply_markup=keys)

                @dp.message(F.text == "Iphone")
                async def cmd_Iphone(message: types.Message):
                    await message.answer_photo(photo="https://images.app.goo.gl/neRHwid2tb1JmLDT8",
                                               caption="<b>Iphoneni qaysi turi kerak\n\nPastdagi bo'limlardan bitasini tanlang!</b>",
                                               parse_mode="HTML", reply_markup=phone1)

                    @dp.message(F.text == "Iphone 11,pro,max")
                    async def cmd_Iphone1(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/g89kK8hbVyhcpg1t5",
                                                   caption="<b>nomi --> Iphone 11 \n yili --> 2021 \n joyi --> 64 gb\n rangi --> Rasmdagidan hammasi bor\nnarxi --> 380$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/1z3hoBjdGPkMzEnr8",
                                                   caption="<b>nomi --> Iphone 11 pro \n yili --> 2021 \n joyi --> 256 gb\n rangi --> qora,oq\nnarxi --> 415$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/eCE8sGfzvn2zD9s67",
                                                   caption="<b>nomi --> Iphone pro max\n yili --> 2021 \n joyi --> 128 gb\n rangi --> kulrang\nnarxi --> 430$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())



                    @dp.message(F.text == "Iphone 12,pro,max")
                    async def cmd_Iphone2(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/Lh1YKLq1JDkseoSR8",
                                               caption="<b>nomi --> Iphone 12 \n yili --> 2022 \n joyi --> 64 gb\n rangi --> Rasmdagidan hammasi bor\nnarxi --> 470$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                               parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/BiUEA91q99nkbs7h9",
                                               caption="<b>nomi --> Iphone 12 pro \n yili --> 2022 \n joyi --> 128 gb\n rangi --> ko'k sifat \nnarxi --> 490$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                               parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/HdtazSBfcEHA6Bau5",
                                               caption="<b>nomi --> Iphone 12 pro max\n yili --> 2022 \n joyi --> 256 gb\n rangi --> Gold\nnarxi --> 510$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                               parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Iphone 13,pro,max")
                    async def cmd_Iphone2(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/YB5t5p18x438Luuw5",
                                                   caption="<b>nomi --> Iphone 13 \n yili --> 2023 \n joyi --> 64 gb\n rangi --> To'q yashil\nnarxi --> 550$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/2Z4rXRLcLCgxxHEu9",
                                                   caption="<b>nomi --> Iphone 13 pro \n yili --> 2023 \n joyi --> 256 gb\n rangi --> ko'k sifat \nnarxi --> 570$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/T8SFLzuUmd4hpSUaA",
                                                   caption="<b>nomi --> Iphone 13 pro max\n yili --> 2023 \n joyi --> 512 gb\n rangi --> Ko'k\nnarxi --> 595$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Iphone 14,pro,max")
                    async def cmd_Iphone2(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/JhhTFEpm5hYzeNfk7",
                                                   caption="<b>nomi --> Iphone 14 \n yili --> 2023 \n joyi --> 256 gb\n rangi --> Oq\nnarxi --> 740$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/eoXhTC3vkWmzX8ut7",
                                                   caption="<b>nomi --> Iphone 14 pro \n yili --> 2023 \n joyi --> 256 gb\n rangi --> ko'k sifat \nnarxi --> 795$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/yE5kAgJAAf9yzU9c7",
                                                   caption="<b>nomi --> Iphone 14 pro max\n yili --> 2023 \n joyi --> 512 gb\n rangi --> Ko'k\nnarxi --> 830$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Iphone 15,pro,max")
                    async def cmd_Iphone2(message: Message):
                        await message.answer_photo(photo="https://images.app.goo.gl/zfnwAXon24ZX6nLx8",
                                                   caption="<b>nomi --> Iphone 15 \n yili --> 2023 \n joyi --> 256 gb\n rangi --> Oq\nnarxi --> 1100$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/1nRzVqCp4LwBpc5aA",
                                                   caption="<b>nomi --> Iphone 15 pro \n yili --> 2023 \n joyi --> 256 gb\n rangi --> To'q kulrang \nnarxi --> 1600$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(photo="https://images.app.goo.gl/HgiNMCZGubcjkcbT7",
                                                   caption="<b>nomi --> Iphone 15 pro max\n yili --> 2023 \n joyi --> 512 gb\n rangi --> To'q ko'k\nnarxi --> 2300$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                                                   parse_mode="HTML", reply_markup=inline.as_markup())
                # @dp.message(F.text == "Iphone")
                # async def cmd_Iphone(message: types.Message):
                #     await message.answer_photo(photo="https://images.app.goo.gl/neRHwid2tb1JmLDT8",
                #                                caption="<b>nomi --> Iphone \n yili --> 2022 \n joyi --> 256 gb\n rangi --> qora\n narxi --> 800$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                #                                parse_mode="HTML", reply_markup=inline.as_markup())


                #
                @dp.message(F.text == "Samsung")
                async def cmd_samsun(message: types.Message):
                    await message.answer("<b>Iphoneni qaysi turi kerak\n\nPastdagi bo'limlardan bitasini tanlang!</b>",
                                               parse_mode="HTML",reply_markup=samsun)

                    @dp.message(F.text == "Samsung A21")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(photo="https://i5.walmartimages.com/seo/For-Samsung-Galaxy-A21-Waterproof-Case-Shockproof-Rugged-Full-Body-Clear-Cover_399ab252-e6e0-4374-b2fe-181ecf01fa6e.68f54cc044524dc63f4ae87b132963b9.jpeg",
                                                   caption="<b>nomi --> Galaxy A21\nyili --> 2019\njoyi --> 256 gb \nrangi --> qora \nnarxi --> 100$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                                                   parse_mode="HTML",reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung A34")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(
                            photo="https://images.samsung.com/is/image/samsung/p6pim/ph/sm-a346elvephl/gallery/ph-galaxy-a34-5g-sm-a346-sm-a346elvephl-535653497?$650_519_PNG$",
                            caption="<b>nomi --> Galaxy A34\nyili --> 2019\njoyi --> 256 gb \nrangi --> qora \nnarxi --> 120$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung A50")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(
                            photo="https://i.ebayimg.com/images/g/w1EAAOSw7PFht37v/s-l1200.webp",
                            caption="<b>nomi --> Galaxy A50\nyili --> 2020\njoyi --> 256 gb \nrangi --> qora \nnarxi --> 140$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung A51")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(
                                photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSm_SI_mJiUD1y4AFvsgPuR5RO6_ysHYaNvpg&usqp=CAU",
                                caption="<b>nomi --> Galaxy A51\nyili --> 2020\njoyi --> 128 gb \nrangi --> Oq \nnarxi --> 149$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                                parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung A54")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(
                            photo="https://images.samsung.com/is/image/samsung/p6pim/uk/sm-a546blgdeub/gallery/uk-galaxy-a54-5g-sm-a546-sm-a546blgdeub-535771507?$650_519_PNG$",
                            caption="<b>nomi --> Galaxy A54\nyili --> 2021\njoyi --> 256 gb \nrangi --> Oq \nnarxi --> 165$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung A62")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(
                            photo="https://i.ytimg.com/vi/_ejP69EQG3s/maxresdefault.jpg",
                            caption="<b>nomi --> Galaxy A62\nyili --> 2021\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 175$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung A71")
                    async def cmd_samsung(message: types.Message):
                        await message.answer_photo(
                            photo="https://www.jebtechaiti.com/wp-content/uploads/2023/07/Samsung-Galaxy-A71-128GB-1_1024x.jpg",
                            caption="<b>nomi --> Galaxy A71\nyili --> 2022\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 210$\nkarobka dakumenti bor \n\n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())


                    @dp.message(F.text == "Samsung S21, Ultra, Plus")
                    async def cmd_samsung1(message: types.Message):
                        await message.answer_photo(
                            photo="https://image-us.samsung.com/SamsungUS/home/mobile/phones/pdp/galaxy-s21-fe-5g/gallery/SM-G990U-graphite-1.png?$product-details-jpg$",
                            caption="<b>nomi --> Galaxy S21 \nyili --> 2021\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://image-us.samsung.com/us/smartphones/galaxy-s21/gallery-images-palette-exclusive/P3-Exclusive-Phantom-Brown/PDP-P3-Phantom-Brown-lockup-01-1600x1200.jpg?$product-details-jpg$",
                            caption="<b>nomi --> Galaxy S21 Ultra \nyili --> 2021\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://openshop.uz/public/storage/uploads/products/photos/202204/UhDmBQasUAXeW7RXdeHYiuCuK98VEVqP9hnM7k6M.jpg",
                            caption="<b>nomi --> Galaxy S21 Plus\nyili --> 2021\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung S22, Ultra, Plus")
                    async def cmd_samsung2(message: types.Message):
                        await message.answer_photo(
                            photo="https://itoutlet.ie/wp-content/uploads/2023/11/samsung-galaxy-s22-s901b-5g-8gb-128gb-black.png",
                            caption="<b>nomi --> Galaxy S22 \nyili --> 2022\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://mandg.com.ng/wp-content/uploads/2022/03/1.jpg",
                            caption="<b>nomi --> Galaxy S22 Ultra \nyili --> 2022\njoyi --> 256 gb \nrangi --> Qora \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://m.media-amazon.com/images/I/71-xEwCrTRL._AC_UF1000,1000_QL80_.jpg",
                            caption="<b>nomi --> Galaxy S22 Plus\nyili --> 2022\njoyi --> 256 gb \nrangi --> Green \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung S23, Ultra, Plus")
                    async def cmd_samsung2(message: types.Message):
                        await message.answer_photo(
                            photo="https://cellucity.co.za/wp-content/uploads/2023/04/Samsung-Galaxy-S23-Plus-Green-1.jpg",
                            caption="<b>nomi --> Galaxy S23 \nyili --> 2023\njoyi --> 256 gb \nrangi --> Green \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://images.samsung.com/uk/smartphones/galaxy-s23-ultra/buy/03_Color_Selection/S23Ultra_Basic_Color/S23Ultra_Green_MO.jpg",
                            caption="<b>nomi --> Galaxy S23 Ultra \nyili --> 2023\njoyi --> 512 gb \nrangi --> Brown \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://m.media-amazon.com/images/I/61bM8Mojf6L.jpg",
                            caption="<b>nomi --> Galaxy S23 Plus\nyili --> 2023\njoyi --> 256 gb \nrangi --> White \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                    @dp.message(F.text == "Samsung S24, Ultra, Plus")
                    async def cmd_samsung2(message: types.Message):
                        await message.answer_photo(
                            photo="https://v.wpimg.pl/ODU1ODZjYCU0Uzl3dRFtMHcLbS0zSGNmIBN1ZnUJYHVnCX88dQwmKDBDKjQ1RCg2IEEuMypEPyh6UD8tdRx-azFYPDQ2CzZrMFwtIT5FKiVnASwiYgticGVTLGluUn1xeFB9Ij5HenxmAHdxb1J5JzcFbTk",
                            caption="<b>nomi --> Galaxy S24 \nyili --> 2024\njoyi --> 512 gb \nrangi --> Green \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://cdn.mos.cms.futurecdn.net/fTgcHFcoCnZ7BrnPeiRFJi-1200-80.jpg",
                            caption="<b>nomi --> Galaxy S24 Ultra \nyili --> 2024\njoyi --> 1 Tb \nrangi --> Brown \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())

                        await message.answer_photo(
                            photo="https://static-www.o2.co.uk/sites/default/files/2024-01/E1-Grey-sku-header-081223_0.png",
                            caption="<b>nomi --> Galaxy S24 Plus\nyili --> 2024\njoyi --> 256 gb \nrangi --> White \nnarxi --> 230$\nkarobka dakumenti bor \n\n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                            parse_mode="HTML", reply_markup=inline.as_markup())











                #
                # @dp.message(F.text == "Redmi")
                # async def cmd_Redmi(message: types.Message):
                #     await message.answer_photo(
                #         photo="https://s0.rbk.ru/v6_top_pics/media/img/9/38/756669508108389.webp",
                #         caption="<b>nomi --> Redmi not 12c \n yili --> 2022 \n joyi --> 128 gb\n rangi --> qora\n narxi --> 800$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                #         parse_mode="HTML", reply_markup=inline.as_markup())
                #
                # @dp.message(F.text == "vivo")
                # async def cmd_vivo(message: types.Message):
                #     await message.answer_photo(
                #         photo="https://grab.mobile2go.com.my/images/thumbs/0018082_vivo-y76-5g-8gb4gb-ram-128gb-rom-original-vivo-malaysia_511.png",
                #         caption="<b>nomi --> Vivo Y76 5G \n yili --> 2022 \n joyi --> 128 gb\n rangi --> Gold\n narxi --> 300$ \n karobka dakumenti bor \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗</b>",
                #         parse_mode="HTML", reply_markup=inline.as_markup())

            @dp.message(F.text == "PowerBank")
            async def cmd_PowerBank0(message: Message):
                await message.answer("PowerBankni qanaqa telefon uchun xarid qilmoqchisiz", reply_markup=Bank)

                @dp.message(F.text == "Iphone uchun")
                async def cmd_PowerBank(message: Message):
                    await message.answer_photo(
                        photo="https://images.app.goo.gl/xApN4H2VvzMdKP2W7",
                        caption="<b>nomi --> PowerBank \n☎sotib olmoqchi bolsangiz pastdagi odamga murojat qiling❗️</b>",
                        parse_mode="HTML", reply_markup=inline.as_markup())

                @dp.message(F.text == "Samsung uchun")
                async def cmd_Power(message: Message):
                    await message.answer_photo(
                        photo="",
                        caption="<b>nomi --> PowerBank \n��sotib olmoqchi bolsangiz pastdagi odamga murojat qiling��️</b>",
                        parse_mode="HTML", reply_markup=inline.as_markup())


        @dp.message(F.text == "Telefonlarga qaytish")
        async def cmd_Telefonlarga(message: Message):
            await message.answer("Telefonlarga qaytildi", reply_markup=keys)


        @dp.message(F.text == "Ortga qaytish")
        async def cmd_orqaga(message: types.Message):
            await message.answer("Noutbuk va Telefonlarga qaytildi", reply_markup=users)

    @dp.message(F.text == "Texnikaga qaytish")
    async def cmd_sahifaga(message: types.Message):
        await message.answer("Texnikaga qaytildi", reply_markup=value)


@dp.message(F.text == "Boshiga qaytish")
async def cmd_orqaga(message: types.Message):
    await message.answer("Boshiga qaytildi", reply_markup=pomosh)


@dp.message(Command("contact_and_location"))
async def cmd_special_buttons(message: types.Message):
    kb1 = [

        [types.KeyboardButton(text="Lokatsiya olish", request_location=True)],
        [types.KeyboardButton(text="Contact yuborish", request_contact=True)],

    ]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb1,
        resize_keyboard=True,
        input_field_placeholder="Word"
    )
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)
    dp.startup.register(start_answer)
    dp.startup.register(stop_answer1)


if __name__ == "__main__":
    asyncio.run(main())
