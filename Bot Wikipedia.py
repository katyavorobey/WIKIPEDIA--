# pip install wikipedia
#
# import telebot, wikipedia, re
# bot = telebot.TeleBot ('5211694794:AAERBTcyohjF38YqfNdHhBK3DTcLsyW6K9E')
# wikipedia.set_lang("ru")
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext=ny.content[:1000]
#         # Разделяем по точкам
#         wikimas=wikitext.split('.')
#         # Отбрасываем всЕ после последней точки
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
#         for x in wikimas:
#             if not('==' in x):
#                     # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
#                 if len((x.strip()))>3:
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'
#
# def start(m, res=False):
# bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# # Получение сообщений от юзера
# def handle_text(message):
#     bot.send_message(message.chat.id, getwiki(message.text))
#
# # Запускаем бота
# bot.polling(none_stop=True, interval=0)
