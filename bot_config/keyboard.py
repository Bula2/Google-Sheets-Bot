# Библиотеки
from aiogram import types
import bot_config.free_time
import bot_config.data
from aiogram.types.callback_query import CallbackQuery
import bot_config.inline_keyboard as inline
import bot_config.utils
from dataBase import main as db


def Buttoms(dp, bot):

    id_dict = {}

    @dp.message_handler(commands="start", state="*")# Команда приветствия и выбора вида спорта /start
    async def start(message: types.Message):
        id_dict[message.from_user.id]=[]
        await message.answer(text="Выберите тип записи ✍ : ", reply_markup=inline.type_of_rent)

    @dp.callback_query_handler(inline.cb.filter(item_name="Отмена"), state="*") # Кнопка отмены
    async def cancel(call: CallbackQuery):
        if len(id_dict[call.from_user.id])>0:
            del id_dict[call.from_user.id][-1]
        await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    @dp.callback_query_handler(inline.cb.filter(count="type_of_rent"),state="*")  # Кнопка выбора типа услуги (аренда/солянка)
    async def bask(call: CallbackQuery, callback_data: dict):
        id_dict[call.from_user.id].clear()
        id_dict[call.from_user.id].append(callback_data["item_name"])
        if callback_data["item_name"]=="Сборная игра":
            if len(id_dict[call.from_user.id]) > 1:
                del id_dict[call.from_user.id][-1]
            id_dict[call.from_user.id].append("Баскетбол")
            await call.answer(cache_time=60)
            await call.message.answer(text="Выберите дату для записи🗓: \n"
                                           "Запись доступна только на Баскетбол\n"
                                           "в субботу и воскресенье с 18:00 до 20:00", reply_markup=inline.Choose_Date_3())
        else:
            await call.answer(cache_time=60)
            await call.message.answer(text="Выберите вид спорта: ", reply_markup=inline.sport)

    @dp.callback_query_handler(inline.cb.filter(item_name="Баскетбол"), state="*")# Кнопка выбора аренды зала для баскетбола
    async def bask(call: CallbackQuery, callback_data: dict):
        if len(id_dict[call.from_user.id]) > 1:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(callback_data["item_name"])
        await call.answer(cache_time=60)
        await call.message.answer(text="Выберите дату аренды🗓: ", reply_markup=inline.Choose_Date_1())

    @dp.callback_query_handler(inline.cb.filter(item_name="Футбол/Воллейбол"), state="*")# Кнопка выбора аренды зала для футбола/воллейбола
    async def foot(call: CallbackQuery,callback_data: dict):
        if len(id_dict[call.from_user.id]) > 1:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(callback_data["item_name"])
        await call.answer(cache_time=60)
        await call.message.answer(text="Выберите дату аренды🗓: ", reply_markup=inline.Choose_Date_0())


    @dp.callback_query_handler(text_contains="week1", state="*")# Инлайн кнопки, срабатывающие для спорта: Баскетбол; Выбор дня аренды
    async def days1(call: CallbackQuery):
        if len(id_dict[call.from_user.id])>2:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(call.data[:-6])
        greed_status = bot_config.free_time.Date(call.data[:5], 1)
        if greed_status==False:
            del id_dict[call.from_user.id][-1]
            await call.answer(cache_time=60)
            await call.message.answer("К сожалению на данную дату запись не доступна😪, \n"
                                      "Пожалуйста выберите другую дату", reply_markup=inline.Choose_Date_1())
        elif len(greed_status) > 0:
            await call.answer(cache_time=360)
            await call.message.answer("Выберите время аренды⏰: ", reply_markup=inline.Time(greed_status, id_dict[call.from_user.id][2]))
        else:
            del id_dict[call.from_user.id][-1]
            await call.answer(cache_time=60)
            await call.message.answer("К сожалению на данную дату нет свободного времени😪, \n"
                                      "Пожалуйста выберите другой день", reply_markup=inline.Choose_Date_1())

    @dp.callback_query_handler(text_contains="week0", state="*")  # Инлайн кнопки, срабатывающие для спорта: Баскетбол; Выбор дня аренды
    async def days1(call: CallbackQuery):
        if len(id_dict[call.from_user.id])>2:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(call.data[:-6])
        greed_status = bot_config.free_time.Date(call.data[:5], 1)
        if greed_status == False:
            del id_dict[call.from_user.id][-1]
            await call.answer(cache_time=60)
            await call.message.answer("К сожалению на данную дату запись не доступна😪, \n"
                                      "Пожалуйста выберите другую дату", reply_markup=inline.Choose_Date_0())
        elif len(greed_status) > 0:
            await call.answer(cache_time=360)
            await call.message.answer("Выберите время аренды⏰: ", reply_markup=inline.Time(greed_status, id_dict[call.from_user.id][2]))
        else:
            del id_dict[call.from_user.id][-1]
            await call.answer(cache_time=60)
            await call.message.answer("К сожалению на данную дату нет свободного времени😪, \n"
                                      "Пожалуйста выберите другой день", reply_markup=inline.Choose_Date_0())

    @dp.callback_query_handler(text_contains="week3", state="*")  # Инлайн кнопки, срабатывающие для спорта: Баскетбол; Выбор дня аренды
    async def days1(call: CallbackQuery):
        if len(id_dict[call.from_user.id]) > 2:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(call.data[:5])
        id_dict[call.from_user.id].append("18:00")
        id_dict[call.from_user.id].append("2 hours")
        await call.answer(cache_time=60)
        await call.message.answer("Введите пожалуйста ваше имя (сообщением): ")
        await bot_config.utils.Other.number.set()

    @dp.callback_query_handler(text_contains="!", state="*")# Выбор времени аренды
    async def how_many_hours(call: CallbackQuery):
        if len(id_dict[call.from_user.id])>3:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(call.data[:-1])
        await call.answer(cache_time=60)
        await call.message.answer("Выберите продолжительность аренды⌛: ", reply_markup=inline.how_many_hours)

    @dp.callback_query_handler(inline.cb.filter(count="end"), state="*")# Продолжительность аренды
    async def end(call: CallbackQuery, callback_data: dict):
        if len(id_dict[call.from_user.id])>4:
            del id_dict[call.from_user.id][-1]
        id_dict[call.from_user.id].append(callback_data["item_name"])
        await call.answer(cache_time=60)
        await call.message.answer("Введите пожалуйста ваше имя (сообщением): ")
        await bot_config.utils.Other.number.set()


    @dp.callback_query_handler(text_contains="other", state="*")# Продолжительность аренды, заданная пользователем
    async def other(call: CallbackQuery):
        await call.message.answer("Введите количество времени в любом формате⌛: ")
        await bot_config.utils.Other.contact.set()

    @dp.message_handler(state=bot_config.utils.Other.contact)# Запрос данных пользователя
    async def contacts(message: types.Message):
        if len(id_dict[message.from_user.id])>4:
            del id_dict[message.from_user.id][-1]
        id_dict[message.from_user.id].append(message.text)
        await message.answer("Введите пожалуйста ваше имя (сообщением): ")
        await bot_config.utils.Other.number.set()

    @dp.message_handler(state=bot_config.utils.Other.number)  # Запрос данных пользователя
    async def contacts(message: types.Message):
        if len(id_dict[message.from_user.id]) > 5:
            del id_dict[message.from_user.id][-1]
        id_dict[message.from_user.id].append(message.text)
        await message.answer("Введите пожалуйста ваш номер телефона (собщение):")
        await bot_config.utils.Other.check.set()

    @dp.message_handler(state=bot_config.utils.Other.check) # Проверка корректности введенных данных
    async def other_end(message: types.Message):
        if len(id_dict[message.from_user.id])>6:
            del id_dict[message.from_user.id][-1]
        id_dict[message.from_user.id].append(message.text)
        user_info_return = "; ".join(id_dict[message.from_user.id])
        await bot.send_message(chat_id=message.from_user.id, text=f"Проверьте корректность введенных вами данных: \n"
                             f"<b>{user_info_return}</b>.\n"
                             "Если все верно, нажмите: <b>Ok</b> \n"
                             "Если данные введены неверно, нажмите: <b>Изменить параметры аренды</b>", reply_markup=inline.check_info)
        await bot_config.utils.Other.state_no.set()

    @dp.callback_query_handler(inline.cb.filter(item_name="check1"), state="*")  # Досвидули
    async def cancel(call: CallbackQuery):
        await call.answer(cache_time=60)
        user_info_return = "; ".join(id_dict[call.from_user.id])
        #await bot.send_message(645454958, user_info_return)
        id=call.from_user.id
        #db.data_processing(id, id_dict[call.from_user.id])
        id_dict[call.from_user.id].clear()
        await call.message.answer("Спасибо за оставленную заявку! \n"
                             "В скором времени оператор свяжется с Вами для подтверждения брони👍.")


    @dp.callback_query_handler(inline.cb.filter(item_name="check0"), state="*")  # Чел ошибся, все по новой
    async def mistake(call: CallbackQuery):
        await call.answer(cache_time=60)
        await call.message.answer("В таком случае, пожалуйста, нажмите кнопку: /start \n"
                                  "и заполните заявку на аренду заново.")


    dp.register_message_handler(start, commands="start")

