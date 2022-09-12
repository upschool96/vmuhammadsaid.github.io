from aiogram import InlineKeyboardMarkup

web_app=WebAppInfo(url="https://vosidovmsaid.github.io/vosidovmuhammadsaid.github.io/")

keyboard=ReplyKeyboardMarkup(
	keyboard=[
		[keyboardButton(text="Site",web_app)]
	],
	resize_keyboard=True
)
cb=CallbackData('btn','action')
key=InlineKeyboardMarkup(
	inline_keyboard=[[InlineKeyboardMarkup('Pay',callback_data='btn:buy')]]
)