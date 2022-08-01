# Библиотеки
from aiogram.utils.callback_data import CallbackData
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import datetime

def Num_to_WeekDay(num):
    weekday=[]
    for i in range (len(num)):
        if num[i]==0:
            weekday.append("(Понедельник)")
        if num[i]==1:
            weekday.append("(Вторник)")
        if num[i]==2:
            weekday.append("(Среда)")
        if num[i]==3:
            weekday.append("(Четверг)")
        if num[i]==4:
            weekday.append("(Пятница)")
        if num[i]==5:
            weekday.append("(Суббота)")
        if num[i]==6:
            weekday.append("(Воскресенье)")
    return(weekday)

cb=CallbackData("type","item_name", "count")

type_of_rent=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Арендовать зал", callback_data=cb.new(item_name='Аренда', count="type_of_rent")),
            ],
            [
                InlineKeyboardButton(text="Присоединиться к сборной игре (Баскетбол)", callback_data=cb.new(item_name='Сборная игра', count="type_of_rent")),
            ],
            [
                InlineKeyboardButton(text="Отмена 🚫", callback_data=cb.new(item_name='Отмена', count=1))
            ]
        ]
    )

sport=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=" Баскетбол 🏀 ", callback_data=cb.new(item_name='Баскетбол', count=1)),
                InlineKeyboardButton(text=" Футбол/Воллейбол ⚽", callback_data=cb.new(item_name='Футбол/Воллейбол', count=1))
            ],
            [
                InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
            ]
        ]
    )

def Choose_Date_0():
    two_weeks = []
    current_day = []
    for i in range(0, 14):
        now = datetime.datetime.today() + datetime.timedelta(days=i)
        current_day.append(now.weekday())
        two_weeks.append(str(now)[8:10] + "." + str(now)[5:7])
    actual_current_day = Num_to_WeekDay(current_day)
    two_weeks_keyboard = InlineKeyboardMarkup(row_width=2)
    button_cancel = InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
    button_list = [InlineKeyboardButton(text=two_weeks[i] + " " + actual_current_day[i], callback_data=two_weeks[i] + " " + actual_current_day[i] + " week0") for i in range(len(two_weeks))]
    two_weeks_keyboard.add(*button_list, button_cancel)
    return (two_weeks_keyboard)

def Choose_Date_1():
    two_weeks = []
    current_day = []
    for i in range(0, 14):
        now = datetime.datetime.today() + datetime.timedelta(days=i)
        current_day.append(now.weekday())
        two_weeks.append(str(now)[8:10] + "." + str(now)[5:7])
    actual_current_day=Num_to_WeekDay(current_day)
    two_weeks_keyboard = InlineKeyboardMarkup(row_width=2)
    button_cancel=InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
    button_list = [InlineKeyboardButton(text=two_weeks[i]+" "+actual_current_day[i], callback_data=two_weeks[i]+ " " + actual_current_day[i]+" week1") for i in range(len(two_weeks))]
    two_weeks_keyboard.add(*button_list, button_cancel)
    return(two_weeks_keyboard)

def Choose_Date_3():
    two_weeks = []
    current_day = []
    for i in range(0, 14):
        now = datetime.datetime.today() + datetime.timedelta(days=i)
        current_day.append(now.weekday())
        two_weeks.append(str(now)[8:10] + "." + str(now)[5:7])
    actual_current_day = Num_to_WeekDay(current_day)
    actual_current_day_len=len(actual_current_day)
    two_weeks_sol=[]
    actual_current_day_sol=[]
    for i in range(actual_current_day_len):
        if (actual_current_day[i]== "(Суббота)" or actual_current_day[i]=="(Воскресенье)"):
            two_weeks_sol.append(two_weeks[i])
            actual_current_day_sol.append(actual_current_day[i])
    two_weeks_keyboard = InlineKeyboardMarkup(row_width=2)
    button_cancel = InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
    button_list = [InlineKeyboardButton(text=two_weeks_sol[i] + " " + actual_current_day_sol[i], callback_data=two_weeks_sol[i] + " week3") for i in range(len(two_weeks_sol))]
    two_weeks_keyboard.add(*button_list, button_cancel)
    return (two_weeks_keyboard)

def Time(time_list, week_day):
    if week_day[6:]=="(Суббота)" or week_day[6:]=="(Воскресенье)":
        for x in ["18:00!","18:30!","19:00!","19:30!"]:
            if x in time_list:
                time_list.remove(x)
    free_time = InlineKeyboardMarkup()
    button_cancel=InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
    button_list = [InlineKeyboardButton(text=i[:-1], callback_data=i) for i in time_list]
    free_time.add(*button_list, button_cancel)
    return(free_time)

how_many_hours=InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="30 минут", callback_data=cb.new(item_name='30 minutes', count="end")),
                InlineKeyboardButton(text="1 час", callback_data=cb.new(item_name='1 hour', count="end"))
            ],
[
                InlineKeyboardButton(text="1 час 30 минут", callback_data=cb.new(item_name='1 hour 30 minutes', count="end")),
                InlineKeyboardButton(text="2 часа", callback_data=cb.new(item_name='2 hours', count="end"))
            ],
[
                InlineKeyboardButton(text="2 часа 30 минут", callback_data=cb.new(item_name='2 hours 30 minutes', count="end")),
                InlineKeyboardButton(text="3 часа", callback_data=cb.new(item_name='3 hours', count="end"))
            ],
[
                InlineKeyboardButton(text="3 часа 30 минут", callback_data=cb.new(item_name='3 hours 30 minutes', count="end")),
                InlineKeyboardButton(text="4 часа", callback_data=cb.new(item_name='4 hours', count="end"))
            ],
[
                InlineKeyboardButton(text="4 часа 30 минут", callback_data=cb.new(item_name='4 hours 30 minutes', count="end")),
                InlineKeyboardButton(text="5 часов", callback_data=cb.new(item_name='5 hours', count="end"))
        ],
[
                InlineKeyboardButton(text="Другое количество времени", callback_data="other"),
        ],
        [
                InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
        ]
    ]
    )
no_free_time=InlineKeyboardMarkup(
    inline_keyboard=[
        InlineKeyboardButton(text="Назад ⬅", callback_data=cb.new(item_name='Отмена', count=1))
    ]
)

check_info=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ок", callback_data=cb.new(item_name='check1', count=1))],
        [InlineKeyboardButton(text="Изменить параметры аренды", callback_data=cb.new(item_name='check0', count=0))]
    ]
)
