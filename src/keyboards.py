from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton

start_keyboard = [[KeyboardButton(text='Нажми на меня', request_contact=True)]]

main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='🧋 Меню', callback_data='menu'),
        InlineKeyboardButton(text='💼 Вакансии', callback_data='vacancy')
    ],
    [
        InlineKeyboardButton(text='🎟️ Мероприятия на месяц', callback_data='events')
    ],
    [
        InlineKeyboardButton(text='📣 Обратная связь', callback_data='feedback'),
        InlineKeyboardButton(text='✉️ Сотрудничество', callback_data='cooperation')
    ]
])

vacancy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='☕ Бариста', callback_data='barista')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='back')
    ]
])

in_vacancy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📥 Откликнуться', callback_data='respond_barista')
    ],
    [
        InlineKeyboardButton(text='Назад', callback_data='back_from_vacancy')
    ]
])

back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Назад', callback_data='back')]
])