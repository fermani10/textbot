from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

default_lang = "en"

prefix = ["/", "!", "#"]


welcome_text = '\n ๐๐ข๐๐ง๐ฏ๐๐ง๐ข๐๐จ ๐๐ฅ ๐ซ๐จ๐๐จ๐ญ ๐๐ ๐ซ๐๐๐จ๐ง๐จ๐๐ข๐ฆ๐ข๐๐ง๐ญ๐จ ๐๐ฉ๐ญ๐ข๐๐จ ๐๐ ๐๐๐ซ๐๐๐ญ๐๐ซ๐๐ฌ.\n\n ๐๐ช๐ฎ๐ฑ๐ญ๐ฆ๐ฎ๐ฆ๐ฏ๐ต๐ฆ ๐ฆ๐ฏ๐ท๐ช๐ฆ๐ฎ๐ฆ ๐ถ๐ฏ๐ข ๐ช๐ฎ๐ข๐จ๐ฆ๐ฏ ๐ค๐ญ๐ข๐ณ๐ข ๐บ ๐ณ๐ฆ๐ค๐ฐ๐ฏ๐ฐ๐ค๐ฆ๐ณ๐ฆ ๐ฆ๐ญ ๐ต๐ฆ๐น๐ต๐ฐ ๐ฆ๐ฏ ๐ญ๐ข ๐ช๐ฎ๐ข๐จ๐ฆ๐ฏ ๐บ ๐ญ๐ฐ ๐ฆ๐ฏ๐ท๐ช๐ข๐ณ๐ฆ ๐ค๐ฐ๐ฎ๐ฐ ๐ถ๐ฏ ๐ฎ๐ฆ๐ฏ๐ด๐ข๐ซ๐ฆ..'
start_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "โ Ayuda", callback_data="help"),
                                        InlineKeyboardButton(
                                            "๐ณ Donar ๐ค", url="https://mpago.la/1ouJa3s"),
                                        InlineKeyboardButton(
                                            "๐ป Novedades", url="https://t.me/botnovedades")
                                    ]]
                            )
reply_to_text_message = 'Oye yo\'No estoy diseรฑado para responder a mensajes de texto. ๐\n Usa /start y lee las instrucciones!'
donate_text = 'Gracias โค๏ธ por considerar mi trabajo digno de una donaciรณn.\nTodos me usan y luego se olvidan. A veces pienso en dejar de funcionar, pero luego pocas personas como tรบ piensan en mรญ y vienen aquรญ. ๐ฅฐ https://paypal.me/donartelegram?locale.x=es_XC  o https://mpago.la/1ouJa3s'
donate_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "๐ณ Paypal ", url="https://paypal.me/donartelegram?locale.x=es_XC"),
                                        InlineKeyboardButton(
                                            "๐ณ Mercado Pago ๐ค", url="https://mpago.la/1ouJa3s")
                                    ]]
                            )
no_text_found = 'Es hora de llamar mi atenciรณn ๐ Probandome \n No puedo leer ningรบn texto en esta imagen ๐ \n Confรญa en mรญ, incluso lo intentรฉ con mi ๐ puesto!'