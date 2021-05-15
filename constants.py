from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

default_lang = "en"

prefix = ["/", "!", "#"]


welcome_text = '\n 𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐨 𝐚𝐥 𝐫𝐨𝐛𝐨𝐭 𝐝𝐞 𝐫𝐞𝐜𝐨𝐧𝐨𝐜𝐢𝐦𝐢𝐞𝐧𝐭𝐨 𝐎𝐩𝐭𝐢𝐜𝐨 𝐝𝐞 𝐜𝐚𝐫𝐚𝐜𝐭𝐞𝐫𝐞𝐬.\n\n 𝘚𝘪𝘮𝘱𝘭𝘦𝘮𝘦𝘯𝘵𝘦 𝘦𝘯𝘷𝘪𝘦𝘮𝘦 𝘶𝘯𝘢 𝘪𝘮𝘢𝘨𝘦𝘯 𝘤𝘭𝘢𝘳𝘢 𝘺 𝘳𝘦𝘤𝘰𝘯𝘰𝘤𝘦𝘳𝘦 𝘦𝘭 𝘵𝘦𝘹𝘵𝘰 𝘦𝘯 𝘭𝘢 𝘪𝘮𝘢𝘨𝘦𝘯 𝘺 𝘭𝘰 𝘦𝘯𝘷𝘪𝘢𝘳𝘦 𝘤𝘰𝘮𝘰 𝘶𝘯 𝘮𝘦𝘯𝘴𝘢𝘫𝘦..'
start_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "❔ Ayuda", callback_data="help"),
                                        InlineKeyboardButton(
                                            "💳 Donar 🤝", url="https://mpago.la/1ouJa3s"),
                                        InlineKeyboardButton(
                                            "💻 Novedades", url="https://t.me/botnovedades")
                                    ]]
                            )
reply_to_text_message = 'Oye yo\'No estoy diseñado para responder a mensajes de texto. 😕\n Usa /start y lee las instrucciones!'
donate_text = 'Gracias ❤️ por considerar mi trabajo digno de una donación.\nTodos me usan y luego se olvidan. A veces pienso en dejar de funcionar, pero luego pocas personas como tú piensan en mí y vienen aquí. 🥰 https://paypal.me/donartelegram?locale.x=es_XC  o https://mpago.la/1ouJa3s'
donate_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "💳 Paypal ", url="https://paypal.me/donartelegram?locale.x=es_XC"),
                                        InlineKeyboardButton(
                                            "💳 Mercado Pago 🤝", url="https://mpago.la/1ouJa3s")
                                    ]]
                            )
no_text_found = 'Es hora de llamar mi atención 👀 Probandome \n No puedo leer ningún texto en esta imagen 😔 \n Confía en mí, incluso lo intenté con mi 👓 puesto!'