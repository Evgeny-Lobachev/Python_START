from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_token
import polynom_g
import sum_polynom
import time


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    'Этот бот поможет сложить многочлены')
    time.sleep(3)
    await update.message.reply_text('Введите степень многочлена после команды /poly (Например: /poly 5)\n'
                                    'После того, как сгенерировано нужное количество многочленов, введите команду /sum')


app = ApplicationBuilder().token(bot_token.token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("poly", polynom_g.view_polynom))
app.add_handler(CommandHandler("sum", sum_polynom.view_sum_polynom))
app.run_polling()