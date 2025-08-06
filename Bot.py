import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8041026552:AAE0k5EuiM-GeayE3jTtcnvWsNGpP2v6qw0'
bot = telebot.TeleBot(API_TOKEN)

admin_id = 6250893240

users = {}
withdraw_requests = []

MIN_WITHDRAW = 150000
TASK_REWARD = 1000
REFERRAL_PERCENT = 0.10

def get_user(user_id):
    if user_id not in users:
        users[user_id] = {'balance': 0, 'ref_by': None}
    return users[user_id]

@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.from_user.id
    args = msg.text.split()
    user = get_user(user_id)

    if len(args) > 1:
        ref_id = int(args[1])
        if user['ref_by'] is None and ref_id != user_id:
            user['ref_by'] = ref_id
            ref_user = get_user(ref_id)
            bonus = int(TASK_REWARD * REFERRAL_PERCENT)
            ref_user['balance'] += bonus
            bot.send_message(ref_id, f"🎉 আপনি 1 জন রেফার করেছেন এবং পেয়েছেন {bonus} bonk!")

    bot.send_message(user_id, "👋 স্বাগতম! আপনি প্রতি টাস্কে পাবেন 1000 bonk।\n/refer - আপনার রেফার লিংক\n/balance - ব্যালেন্স দেখুন\n/withdraw - টাকা তুলুন")

@bot.message_handler(commands=['refer'])
def refer(msg):
    user_id = msg.from_user.id
    bot.send_message(user_id, f"🔗 আপনার রেফার লিংক:\
