# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 00:02:29 2018
@author: Andrey
"""
import random
import telebot
import io
import os
from count import count
from telebot import types
from rate import rate
token = '676409274:AAEkNw7HgOzrjagjSR74pJ1vIYvcuo5OO84'
bot = telebot.TeleBot(token)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup.row('Stone', 'Paper')
markup.row('Scissors')

@bot.message_handler(commands = ['start'])
def send_welcome(message):
    q = io.open('Player_info/players.txt', 'r', encoding='utf-8')
    text3 = q.read()
    c3 = text3.count(str(message.chat.id))
    q.close()
    if c3 == 0:
         bot.send_message(message.chat.id, 'Who are you??\nEnter your nickname (for the Rating table)')
         q1 = io.open('Player_info/'+str(message.chat.id)+'R.txt', 'w', encoding='utf-8')
         q1.write(('1').decode('unicode_escape'))
         q1.close()
    else:
         bot.send_message(message.chat.id, 'To start playing, just send "/game"')
    count((str(message.chat.id)).decode('unicode_escape'), '.start')
    return
@bot.message_handler(commands=['rating'])
def handle_rating(message):
    rate()
    f = io.open('Player_info/players1.txt', 'r', encoding='utf-8')
    rating = f.read()
    f.close()
    bot.send_message(message.chat.id, rating)
    return

@bot.message_handler(commands = ['help'])
def Help(message):
    bot.send_message(message.chat.id, 'Hi! If you want to play, just send /game\n/rating - to see rating of all players\n/help - to repeat this message')

@bot.message_handler(commands = ['game'])
def Game(message):
    bot.send_message(message.chat.id, 'Stone, Scissors, Paper?\n', reply_markup=markup)
@bot.message_handler(regexp = "Stone")
def Kamen(message):
    opp = random.randint(1,3)
    if opp==1:
        bot.send_message(message.chat.id,'Opponent: Stone\nStone to Stone!\nOne more time...')
        count((str(message.chat.id)).decode('unicode_escape'), '.draft') 
    elif opp==2:
        bot.send_message(message.chat.id,'Opponent: Scissors\nYou crashed Scissors!\nWinner winner chicken dinner!')
        count((str(message.chat.id)).decode('unicode_escape'), '.rating')
    else: 
        bot.send_message(message.chat.id,'Opponent: Paper\nPaper has wrapped your Stone!\nLOST!!!')
        count((str(message.chat.id)).decode('unicode_escape'), '.lose') 
    bot.send_message(message.chat.id,'If you want to play again, just send "Stone", "Scissors" or "Paper"')
@bot.message_handler(regexp = "Scissors")
def Scissors(message):
    opp = random.randint(1,3)
    if opp==1:
        bot.send_message(message.chat.id,'Opponent: Stone\nStone crashed your Scissors!\nLOST!!!')
        count((str(message.chat.id)).decode('unicode_escape'), '.lose')
    elif opp==2:
        bot.send_message(message.chat.id,'Opponent: Scissors\nScissors to Scissors!\nOne more time...')
        count((str(message.chat.id)).decode('unicode_escape'), '.draft')
    else: 
        bot.send_message(message.chat.id,'Opponent: Paper\nYou have cut the Paper!\nEeeasy win!\n\nIf you want to play again, just send Stone, Scissors or Paper')
        count((str(message.chat.id)).decode('unicode_escape'), '.rating')
        
    bot.send_message(message.chat.id,'If you want to play again, just send "Stone", "Scissors" or "Paper"')
@bot.message_handler(regexp = "Paper")
def Paper(message):
    opp = random.randint(1,3)
    if opp==1:
        bot.send_message(message.chat.id,'Opponent: Stone\nYou have wrapped the stone!\nNewborn child! Congrats)')
        count((str(message.chat.id)).decode('unicode_escape'), '.rating')
    elif opp==2:
        bot.send_message(message.chat.id,'Opponent: Scissors\nYou have been cut with the Scissors!\nLOST!!!')
        count((str(message.chat.id)).decode('unicode_escape'), '.lose')
    else: 
        bot.send_message(message.chat.id,'Opponent: Paper\nPaper to Paper!\nOne more time...')
        count((str(message.chat.id)).decode('unicode_escape'), '.draft')
    bot.send_message(message.chat.id,'If you want to play again, just send "Stone", "Scissors" or "Paper"')
@bot.message_handler(content_types = ['text'])
def DontUnderstand(message):
    if  os.path.exists('Player_info/'+str(message.chat.id)+'R.txt'):
        q2 = io.open('Player_info/players.txt', 'a', encoding='utf-8')
        q2.write(str(message.text)+ (' = ').decode('unicode_escape')+str(message.chat.id)+('\n').decode('unicode_escape'))
        q2.close()
        os.remove('Player_info/'+str(message.chat.id)+'R.txt')
        bot.send_message(message.chat.id, "My name is Kamen, glad to meet you! To start playing send me /game, for reference - send /help")
    else:
        bot.reply_to(message, 'Шо?')
if __name__ == '__main__':    
    bot.polling(none_stop=True)