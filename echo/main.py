from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from echo.config import BOT_TOKEN

CALLBACK_BUTTON_PRICES = "callback_button_prices"
CALLBACK_BUTTON_CALENDAR = "callback_button_calendar"
CALLBACK_BUTTON_FACULTIES = "callback_button_faculties"

CALLBACK_BUTTON_BACK = "callback_button_back"

CALLBACK_BUTTON_FACULTIES1 = "callback_button_faculties1"
CALLBACK_BUTTON_FACULTIES2 = "callback_button_faculties2"
CALLBACK_BUTTON_FACULTIES3 = "callback_button_faculties3"
CALLBACK_BUTTON_FACULTIES4 = "callback_button_faculties4"
CALLBACK_BUTTON_FACULTIES5 = "callback_button_faculties5"
CALLBACK_BUTTON_FACULTIES6 = "callback_button_faculties6"
CALLBACK_BUTTON_FACULTIES7 = "callback_button_faculties7"

CALLBACK_BUTTON1_DEP1 = "callback_button1_department1"
CALLBACK_BUTTON1_DEP2 = "callback_button1_department2"
CALLBACK_BUTTON1_DEP3 = "callback_button1_department3"
CALLBACK_BUTTON1_DEP4 = "callback_button1_department4"
CALLBACK_BUTTON2_DEP1 = "callback_button2_department1"
CALLBACK_BUTTON2_DEP2 = "callback_button2_department2"
CALLBACK_BUTTON2_DEP3 = "callback_button2_department3"
CALLBACK_BUTTON2_DEP4 = "callback_button2_department4"
CALLBACK_BUTTON2_DEP5 = "callback_button2_department5"
CALLBACK_BUTTON2_DEP6 = "callback_button2_department6"
CALLBACK_BUTTON2_DEP7 = "callback_button2_department7"
CALLBACK_BUTTON3_DEP1 = "callback_button3_department1"
CALLBACK_BUTTON3_DEP2 = "callback_button3_department2"
CALLBACK_BUTTON3_DEP3 = "callback_button3_department3"
CALLBACK_BUTTON3_DEP4 = "callback_button3_department4"
CALLBACK_BUTTON3_DEP5 = "callback_button3_department5"
CALLBACK_BUTTON3_DEP6 = "callback_button3_department6"
CALLBACK_BUTTON4_DEP1 = "callback_button4_department1"
CALLBACK_BUTTON5_DEP1 = "callback_button5_department1"
CALLBACK_BUTTON5_DEP2 = "callback_button5_department2"
CALLBACK_BUTTON5_DEP3 = "callback_button5_department3"
CALLBACK_BUTTON5_DEP4 = "callback_button5_department4"
CALLBACK_BUTTON5_DEP5 = "callback_button5_department5"
CALLBACK_BUTTON5_DEP6 = "callback_button5_department6"
CALLBACK_BUTTON5_DEP7 = "callback_button5_department7"
CALLBACK_BUTTON6_DEP1 = "callback_button6_department1"
CALLBACK_BUTTON6_DEP2 = "callback_button6_department2"
CALLBACK_BUTTON6_DEP3 = "callback_button6_department3"
CALLBACK_BUTTON6_DEP4 = "callback_button6_department4"
CALLBACK_BUTTON6_DEP5 = "callback_button6_department5"
CALLBACK_BUTTON7_DEP1 = "callback_button7_department1"
CALLBACK_BUTTON7_DEP2 = "callback_button7_department2"
CALLBACK_BUTTON7_DEP3 = "callback_button7_department3"
CALLBACK_BUTTON7_DEP4 = "callback_button7_department4",

TITLES = {
    CALLBACK_BUTTON_PRICES: "Узнать цены",
    CALLBACK_BUTTON_CALENDAR: "Календарь 📆",
    CALLBACK_BUTTON_FACULTIES: "🧬 Факультеты и кафедры 🔬",
}

GLOBAL = {
    CALLBACK_BUTTON_BACK: "В начало ⏮",
}

FACULTIES = {
    CALLBACK_BUTTON_FACULTIES1: "1",
    CALLBACK_BUTTON_FACULTIES2: "2",
    CALLBACK_BUTTON_FACULTIES3: "3",
    CALLBACK_BUTTON_FACULTIES4: "4",
    CALLBACK_BUTTON_FACULTIES5: "5",
    CALLBACK_BUTTON_FACULTIES6: "6",
    CALLBACK_BUTTON_FACULTIES7: "7",
}

DEPARTMENTS = {
    CALLBACK_BUTTON1_DEP1: "1",
    CALLBACK_BUTTON1_DEP2: "2",
    CALLBACK_BUTTON1_DEP3: "3",
    CALLBACK_BUTTON1_DEP4: "4",

    CALLBACK_BUTTON2_DEP1: "1",
    CALLBACK_BUTTON2_DEP2: "2",
    CALLBACK_BUTTON2_DEP3: "3",
    CALLBACK_BUTTON2_DEP4: "4",
    CALLBACK_BUTTON2_DEP5: "5",
    CALLBACK_BUTTON2_DEP6: "6",
    CALLBACK_BUTTON2_DEP7: "7",

    CALLBACK_BUTTON3_DEP1: "1",
    CALLBACK_BUTTON3_DEP2: "2",
    CALLBACK_BUTTON3_DEP3: "3",
    CALLBACK_BUTTON3_DEP4: "4",
    CALLBACK_BUTTON3_DEP5: "5",
    CALLBACK_BUTTON3_DEP6: "6",

    CALLBACK_BUTTON4_DEP1: "1",

    CALLBACK_BUTTON5_DEP1: "1",
    CALLBACK_BUTTON5_DEP2: "2",
    CALLBACK_BUTTON5_DEP3: "3",
    CALLBACK_BUTTON5_DEP4: "4",
    CALLBACK_BUTTON5_DEP5: "5",
    CALLBACK_BUTTON5_DEP6: "6",
    CALLBACK_BUTTON5_DEP7: "7",

    CALLBACK_BUTTON6_DEP1: "1",
    CALLBACK_BUTTON6_DEP2: "2",
    CALLBACK_BUTTON6_DEP3: "3",
    CALLBACK_BUTTON6_DEP4: "4",
    CALLBACK_BUTTON6_DEP5: "5",

    CALLBACK_BUTTON7_DEP1: "1",
    CALLBACK_BUTTON7_DEP2: "2",
    CALLBACK_BUTTON7_DEP3: "3",
    CALLBACK_BUTTON7_DEP4: "4",
}


def get_base_inline_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_PRICES], callback_data=CALLBACK_BUTTON_PRICES),
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_CALENDAR], callback_data=CALLBACK_BUTTON_CALENDAR),
        ],
        [
            InlineKeyboardButton(TITLES[CALLBACK_BUTTON_FACULTIES], callback_data=CALLBACK_BUTTON_FACULTIES),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard2():
    keyboard = [
        [
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES1], callback_data=CALLBACK_BUTTON_FACULTIES1),
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES2], callback_data=CALLBACK_BUTTON_FACULTIES2),
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES3], callback_data=CALLBACK_BUTTON_FACULTIES3),
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES4], callback_data=CALLBACK_BUTTON_FACULTIES4),
        ],
        [
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES5], callback_data=CALLBACK_BUTTON_FACULTIES5),
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES6], callback_data=CALLBACK_BUTTON_FACULTIES6),
            InlineKeyboardButton(FACULTIES[CALLBACK_BUTTON_FACULTIES7], callback_data=CALLBACK_BUTTON_FACULTIES7),
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty1():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON1_DEP1], callback_data=CALLBACK_BUTTON1_DEP1),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON1_DEP2], callback_data=CALLBACK_BUTTON1_DEP2),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON1_DEP3], callback_data=CALLBACK_BUTTON1_DEP3),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON1_DEP4], callback_data=CALLBACK_BUTTON1_DEP4),
        ],
        [
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty2():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP1], callback_data=CALLBACK_BUTTON2_DEP1),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP2], callback_data=CALLBACK_BUTTON2_DEP2),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP3], callback_data=CALLBACK_BUTTON2_DEP3),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP4], callback_data=CALLBACK_BUTTON2_DEP4),
        ],
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP5], callback_data=CALLBACK_BUTTON2_DEP5),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP6], callback_data=CALLBACK_BUTTON2_DEP6),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON2_DEP7], callback_data=CALLBACK_BUTTON2_DEP7),
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty3():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON3_DEP1], callback_data=CALLBACK_BUTTON3_DEP1),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON3_DEP2], callback_data=CALLBACK_BUTTON3_DEP2),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON3_DEP3], callback_data=CALLBACK_BUTTON3_DEP3),

        ],
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON3_DEP4], callback_data=CALLBACK_BUTTON3_DEP4),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON3_DEP5], callback_data=CALLBACK_BUTTON3_DEP5),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON3_DEP6], callback_data=CALLBACK_BUTTON3_DEP6),
        ],
        [
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty4():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON4_DEP1], callback_data=CALLBACK_BUTTON4_DEP1),
        ],
        [
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty5():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP1], callback_data=CALLBACK_BUTTON5_DEP1),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP2], callback_data=CALLBACK_BUTTON5_DEP2),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP3], callback_data=CALLBACK_BUTTON5_DEP3),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP4], callback_data=CALLBACK_BUTTON5_DEP4),
        ],
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP5], callback_data=CALLBACK_BUTTON5_DEP5),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP6], callback_data=CALLBACK_BUTTON5_DEP6),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON5_DEP7], callback_data=CALLBACK_BUTTON5_DEP7),
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty6():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON6_DEP1], callback_data=CALLBACK_BUTTON6_DEP1),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON6_DEP2], callback_data=CALLBACK_BUTTON6_DEP2),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON6_DEP3], callback_data=CALLBACK_BUTTON6_DEP3),
        ],
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON6_DEP4], callback_data=CALLBACK_BUTTON6_DEP4),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON6_DEP5], callback_data=CALLBACK_BUTTON6_DEP5),
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def get_keyboard_faculty7():
    keyboard = [
        [
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON7_DEP1], callback_data=CALLBACK_BUTTON7_DEP1),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON7_DEP2], callback_data=CALLBACK_BUTTON7_DEP2),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON7_DEP3], callback_data=CALLBACK_BUTTON7_DEP3),
            InlineKeyboardButton(DEPARTMENTS[CALLBACK_BUTTON7_DEP4], callback_data=CALLBACK_BUTTON7_DEP4),
        ],
        [
            InlineKeyboardButton(GLOBAL[CALLBACK_BUTTON_BACK], callback_data=CALLBACK_BUTTON_BACK),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


def keyboard_callback_handler(bot: Bot, update: Update, chat_data=None, **kwargs):
    query = update.callback_query
    data = query.data

    chat_id = update.effective_message.chat_id
    current_text = update.effective_message.text

    if data == CALLBACK_BUTTON_PRICES:
        query.edit_message_text(
            text="Стоимость обучения на\n"
                 "2020-2021 академический год\n\n"
                 "http://alatoo.edu.kg/view/public/pages/page.xhtml?id=8673"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard(),
        )

    elif data == CALLBACK_BUTTON_CALENDAR:
        query.edit_message_text(
            text="Это Академический календарь\n"
                 "на весь актуальный учебный год\n\n"
                 "http://iaau.edu.kg/view/public/pages/page.xhtml\n\n"
                 "/home - Вернуться домой",
            reply_markup=get_base_inline_keyboard(),
        )

    elif data == CALLBACK_BUTTON_FACULTIES:
        query.edit_message_text(
            text="Для выбора конкретного направления\n"
                 "выберите один из следующих факультетов\n\n"
                 "1 - Факультет инженерии и информатики\n\n"
                 "2 - Факультет гуманитарных наук\n\n"
                 "3 - Факультет экономики и управления\n\n"
                 "4 - Медицинский факультет\n\n"
                 "5 - Среднее - профессиональное образование\n\n"
                 "6 - Центр дистанционного обучения\n\n"
                 "7 - Институт языков\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard2(),
        )

    elif data == CALLBACK_BUTTON_BACK:
        query.edit_message_text(
            text="Вы в самом начале\n\n"
                 "Пожалуйста выберите что-то\n"
                 "из ниже перечисленного\n\n"
                 "или нажмите /help\n"
                 "чтобы увидеть весь список\n"
                 "доступных команд",
            reply_markup=get_base_inline_keyboard(),
        )

    elif data == CALLBACK_BUTTON_FACULTIES1:
        query.edit_message_text(
            text="Факультет инженерии и информатики\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Информатика и вычислительная техника\n\n"
                 "2 - Электроника и наноэлектроника\n\n"
                 "3 - Прикладная математика и информатика\n\n"
                 "4 - Управление качеством (инженер-менеджер)\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty1(),
        )

    elif data == CALLBACK_BUTTON1_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Информатики и вычислительной техники\n"
                 "перейдя по ссылке\n\n"
                 "http://com.iaau.edu.kg/index.html\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON1_DEP2:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Электроники и наноэлектроники\n"
                 "перейдя по ссылке\n\n"
                 "http://electronic.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON1_DEP3:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Прикладной математики и информатики\n"
                 "перейдя по ссылке\n\n"
                 "http://mat.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON1_DEP4:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Управление качеством (инженер-менеджер)\n"
                 "перейдя по ссылке\n\n"
                 "http://ie.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON_FACULTIES2:
        query.edit_message_text(
            text="Факультет гуманитарных наук\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Зарубежная филология\n"
                 "(турецкая филология, со знанием английского языка)\n\n"
                 "2 - Филология\n"
                 "(английский язык и литература)\n\n"
                 "3 - Перевод и переводоведение\n"
                 "(перевод и переводоведение)\n\n"
                 "4 - Перевод и переводоведение\n"
                 "(китайский язык)\n\n"
                 "5 - Педагогика\n"
                 "(психолого-педагогическая консультация и помощь)\n\n"
                 "6 - Педагогика\n"
                 "(педагогика и методика начального образования)\n\n"
                 "7 - Журналистика\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty2(),
        )

    elif data == CALLBACK_BUTTON2_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Зарубежная филология\n"
                 "(турецкая филология, со знанием английского языка)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://turkology.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON2_DEP2:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Филология\n"
                 "(английский язык и литература)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://english.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON2_DEP3:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Перевод и переводоведение\n"
                 "(перевод и переводоведение)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://simultaneous.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON2_DEP4:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Перевод и переводоведение\n"
                 "(китайский язык)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://chineese.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON2_DEP5:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Педагогика\n"
                 "(психолого-педагогическая консультация и помощь)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://pcg.iaau.edu.kg/n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON2_DEP6:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Педагогика\n"
                 "(педагогика и методика начального образования)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://pcg.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON2_DEP7:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Журналистика\n\n"
                 "перейдя по ссылке\n\n"
                 "http://journalism.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON_FACULTIES3:
        query.edit_message_text(
            text="Факультет экономики и управления\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Экономика\n"
                 "((Международная Экономика и Бизнес)\n\n"
                 "2 - Экономика\n"
                 "(финансы и кредит)\n\n"
                 "3 - Экономика\n"
                 "(бухгалтерский учет и аудит)\n\n"
                 "4 - Международные отношения\n\n"
                 "5 - Менеджмент\n\n"
                 "6 - Юриспруденция\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty3(),
        )

    elif data == CALLBACK_BUTTON3_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Экономика\n"
                 "(Международная Экономика и Бизнес)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://economy.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON3_DEP2:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Экономика\n"
                 "(финансы и кредит)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://fin.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON3_DEP3:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Экономика\n"
                 "(бухгалтерский учет и аудит)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://fin.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON3_DEP4:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Международные отношения\n\n"
                 "перейдя по ссылке\n\n"
                 "http://ir.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON3_DEP5:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Менеджмент\n\n"
                 "перейдя по ссылке\n\n"
                 "http://management.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON3_DEP6:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Юриспруденция\n\n"
                 "перейдя по ссылке\n\n"
                 "http://law.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON_FACULTIES4:
        query.edit_message_text(
            text="Медицинский факультет\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Лечебное дело - Педиатрия\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty4(),
        )

    elif data == CALLBACK_BUTTON4_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Лечебное дело - Педиатрия\n\n"
                 "перейдя по ссылке\n\n"
                 "http://med.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON_FACULTIES5:
        query.edit_message_text(
            text="Среднее - профессиональное образование\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Экономика и бухгалтерский учет\n\n"
                 "2 - Банковское дело\n\n"
                 "3 - Маркетинг\n\n"
                 "4 - Компьютерные системы и комплексы\n\n"
                 "5 - Программное обеспечение вычислительной техники\n"
                 "и автоматизированных систем\n\n"
                 "6 - Дизайн\n"
                 "(компьютерно-графический)\n\n"
                 "7 - Правоведение\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty5(),
        )

    elif data == CALLBACK_BUTTON5_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Экономика и бухгалтерский учет\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON5_DEP2:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Банковское дело\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON5_DEP3:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Маркетинг\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON5_DEP4:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Компьютерные системы и комплексы\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON5_DEP5:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Программное обеспечение вычислительной техники\n"
                 "и автоматизированных систем\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON5_DEP6:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Дизайн\n"
                 "(компьютерно-графический)\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON5_DEP7:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Правоведение\n\n"
                 "перейдя по ссылке\n\n"
                 "http://college.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON_FACULTIES6:
        query.edit_message_text(
            text="Среднее - профессиональное образование\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Менеджмент\n\n"
                 "2 - Финансы и кредит\n\n"
                 "3 - Бухгалтерский учет, анализ и аудит\n\n"
                 "4 - Международная экономика и бизнес\n\n"
                 "5 - Педагогика\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty6(),
        )

    elif data == CALLBACK_BUTTON6_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Mенеджмент\n\n"
                 "перейдя по ссылке\n\n"
                 "http://dlc.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON6_DEP2:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Финансы и кредит\n\n"
                 "перейдя по ссылке\n\n"
                 "http://dlc.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON6_DEP3:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Бухгалтерский учет, анализ и аудит\n\n"
                 "перейдя по ссылке\n\n"
                 "http://dlc.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON6_DEP4:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Международная экономика и бизнес\n\n"
                 "перейдя по ссылке\n\n"
                 "http://dlc.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON6_DEP5:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Педагогика\n\n"
                 "перейдя по ссылке\n\n"
                 "http://dlc.alatoo.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON_FACULTIES7:
        query.edit_message_text(
            text="Институт языков\n\n"
                 "Выберите кафедру\n\n"
                 "1 - Kыргызский язык\n\n"
                 "2 - Pусский язык\n\n"
                 "3 - Tурецкий языкn\n"
                 "4 - Aнглийский язык\n\n",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_keyboard_faculty7(),
        )

    elif data == CALLBACK_BUTTON7_DEP1:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Kыргызский язык\n\n"
                 "перейдя по ссылке\n\n"
                 "http://kg.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON7_DEP2:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Pусский язык\n\n"
                 "перейдя по ссылке\n\n"
                 "http://ru.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON7_DEP3:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Tурецкий язык\n\n"
                 "перейдя по ссылке\n\n"
                 "http://hazirlik.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )

    elif data == CALLBACK_BUTTON7_DEP4:
        query.edit_message_text(
            text="Вы можете ознакомиться с кафедрой\n\n"
                 "Aнглийский язык\n\n"
                 "перейдя по ссылке\n\n"
                 "http://preparatory.iaau.edu.kg/\n\n"
                 "/home - Вернуться домой",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=get_base_inline_keyboard()
        )


def do_contacts(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Международный университет Ала-Tоо\n"
             "ул.Анкара 1/8, Тунгуч, 720048\n"
             "Бишкек, Кыргызстан\n\n"
             "Телефон: +996 (312) 631425\n"
             "Факс: +996(312) 630409\n"
             "E-mail: info@iaau.edu.kg\n\n"
             "Как добраться?\n"
             "https://go.2gis.com/tu00l\n\n"
             "Общественный транспорт:\n"
             "5 - троллейбус\n7 - троллейбус\n6 - автобус\n7 - автобус\n"
             "102 - маршрутка\n105 - маршрутка\n128 - маршрутка\n"
             "137 - маршрутка\n147 - маршрутка\n154 - маршрутка\n"
             "166 - маршрутка\n258 - маршрутка\n262 - маршрутка\n\n"
             "Приемная  комиссия:\n\n"
             "Международный Университет Ала-Tоо\n"
             "(A-Блок), 107 кабинет\n"
             "Телефон: +996 (312) 630407\n"
             "WhatsApp: +996 555 820 000\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_twitter(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Мы в Twitter\n\n"
             "https://twitter.com/alatooedukg/\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_vk(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Мы в VK\n\n"
             "https://vk.com/aiuedukg\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_instagram(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Мы в Instagram\n\n"
             "https://www.instagram.com/alatoo.edu.kg/\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_facebook(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Мы в Facebook\n\n"
             "https://www.facebook.com/ALATOOinternationalUniversity1996/\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_website(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Здесь наш сайт\n\n"
             "http://iaau.edu.kg/\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_youtube(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Наш YouTube канал\n\n"
             "https://www.youtube.com/channel/UCRwPUKmeoiUausG3luv7d3Q\n\n"
             "/home - Вернуться домой",
        reply_markup=get_base_inline_keyboard(),
    )


def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Добро пожаловать!\n\n"
             "Ala-Too International University - это бот\n"
             "созданный чтобы быть вашим помощником и гидом\n\n"
             "Здесь вы можете узнать о всех факультетах и кафедрах\n"
             "распологаемых университетом\n\n"
             "Узнать актуальные цены\n\n"
             "Получить необходимую информацию\n\n"
             "/help - чтобы увидеть весь список доступны команд",
        reply_markup=get_base_inline_keyboard()
    )


def do_home(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Вы в самом начале\n\n"
             "Пожалуйста выберите что-то\n"
             "из ниже перечисленного\n\n"
             "или нажмите /help\n"
             "чтобы увидеть весь список\n"
             "доступных команд",
        reply_markup=get_base_inline_keyboard()
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Список доступных команд\n\n"
             "/contacts - Обратная связь\n"
             "/twitter - Мы в Twitter\n"
             "/vk - Мы в VK\n"
             "/instagram - Мы в Instagram\n"
             "/facebook - Мы в Facebook\n"
             "/website - Наш сайт\n"
             "/youtube - Наш YouTube канал\n"
             "/start - Инициализация\n"
             "/home - Вернуться к началу\n"
             "/help - Помощь",
        reply_markup=get_base_inline_keyboard()
    )


def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Ваш ID = {}\n\n{}".format(chat_id, update.message.text)
    bot.send_message(
        chat_id=chat_id,
        text="Мы раотаем над внедрением пользовательских сообщений\n\n"
        "Вскоре будет добавлена возможность оставлять заявки прямо здесь\n\n"
             "Спасибо за понимание 😊\n",
        reply_markup=get_base_inline_keyboard(),
    )


def main():
    bot = Bot(
        token=BOT_TOKEN,
        # base_url=TG_API_URL,

    )
    updater = Updater(
        bot=bot,
    )

    buttons_handler = CallbackQueryHandler(callback=keyboard_callback_handler, pass_chat_data=True)
    message_handler = MessageHandler(Filters.text, do_echo)
    contacts_handler = CommandHandler("contacts", do_contacts)
    twitter_handler = CommandHandler("twitter", do_twitter)
    vk_handler = CommandHandler("vk", do_vk)
    instagram_handler = CommandHandler("instagram", do_instagram)
    facebook_handler = CommandHandler("facebook", do_facebook)
    website_handler = CommandHandler("website", do_website)
    youtube_handler = CommandHandler("youtube", do_youtube)
    start_handler = CommandHandler("start", do_start)
    home_handler = CommandHandler("home", do_home)
    help_handler = CommandHandler("help", do_help)

    updater.dispatcher.add_handler(buttons_handler)
    updater.dispatcher.add_handler(message_handler)
    updater.dispatcher.add_handler(contacts_handler)
    updater.dispatcher.add_handler(twitter_handler)
    updater.dispatcher.add_handler(vk_handler)
    updater.dispatcher.add_handler(instagram_handler)
    updater.dispatcher.add_handler(facebook_handler)
    updater.dispatcher.add_handler(website_handler)
    updater.dispatcher.add_handler(youtube_handler)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(home_handler)
    updater.dispatcher.add_handler(help_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()