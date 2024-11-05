from email import message

import telebot
from telebot import types
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import kaleido

df = pd.read_csv('IQ_level.csv')

bot = telebot.TeleBot('6922790002:AAFsAG9jh-NocOWhaOaba74ArmJGJ8DmYEI')


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Start')
    markup.row(but1)
    bot.send_message(message.chat.id, 'Hello! This I am a telegram bot made '
                                   'for better visualization of the project! '
                                   'You can investigate it by using buttons below.', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == 'Start' or message.text == 'Back':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Statistics')
        but2 = types.KeyboardButton('Dataset on kaggle')
        markup.row(but1, but2)
        bot.send_message(message.chat.id, 'Choose what do you want', reply_markup=markup)
    elif message.text == 'Statistics':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Back')
        but2 = types.KeyboardButton('IQ Pure statistics')
        but3 = types.KeyboardButton('Average Income Pure statistics')
        but4 = types.KeyboardButton('Education Expenditure Pure statistics')
        but5 = types.KeyboardButton('Correlation between them')
        but6 = types.KeyboardButton('Choose by Yourself')
        markup.row(but2)
        markup.row(but3)
        markup.row(but4)
        markup.row(but6)
        markup.row(but1, but5)
        bot.send_message(message.chat.id, 'Choose which statistic would you like to see', reply_markup=markup)
    elif message.text == 'Choose by Yourself':
        keyboard = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton('Click here afterwards', callback_data='country')
        keyboard.add(but1)
        bot.send_message(message.chat.id, 'Now you are able to choose a country whose statistics you '
                                          'would like to see. \n \nAt first write a name of the country'
                                          ' you are interested in', reply_markup=keyboard)

    elif message.text == 'IQ Pure statistics':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Back')
        but2 = types.KeyboardButton('IQ Pure statistics')
        but3 = types.KeyboardButton('Average Income Pure statistics')
        but4 = types.KeyboardButton('Education Expenditure Pure statistics')
        but5 = types.KeyboardButton('Correlation between them')
        but6 = types.KeyboardButton('Choose by Yourself')
        markup.row(but2)
        markup.row(but3)
        markup.row(but4)
        markup.row(but6)
        markup.row(but1, but5)
        with open('iqbars.png', 'rb') as f:
            photo1 = f.read()
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'IQ mean -> 86.116505 \n IQ median -> 88.000000 \n IQ standard deviation -> 12.624518', reply_markup=markup)
        bot.send_message(message.chat.id, 'IQ scores are spread evenly by countries(Because mean and median values are nearly equal)')

    elif message.text == 'Average Income Pure statistics':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Back')
        but2 = types.KeyboardButton('IQ Pure statistics')
        but3 = types.KeyboardButton('Average Income Pure statistics')
        but4 = types.KeyboardButton('Education Expenditure Pure statistics')
        but5 = types.KeyboardButton('Correlation between them')
        but6 = types.KeyboardButton('Choose by Yourself')
        markup.row(but2)
        markup.row(but3)
        markup.row(but4)
        markup.row(but6)
        markup.row(but1, but5)
        with open('rich.png', 'rb') as f:
            photo1 = f.read()
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'Average Income mean -> 17525.048544 \n Average Income median -> 7586.000000 \n Average Income standard deviation -> 21067.803552', reply_markup=markup)
        bot.send_message(message.chat.id, 'The smaller part of countries have the average income of the citizens much bigger than in the larger part')
    elif message.text == 'Education Expenditure Pure statistics':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Back')
        but2 = types.KeyboardButton('IQ Pure statistics')
        but3 = types.KeyboardButton('Average Income Pure statistics')
        but4 = types.KeyboardButton('Education Expenditure Pure statistics')
        but5 = types.KeyboardButton('Correlation between them')
        but6 = types.KeyboardButton('Choose by Yourself')
        markup.row(but2)
        markup.row(but3)
        markup.row(but4)
        markup.row(but6)
        markup.row(but1, but5)
        bot.send_message(message.chat.id, 'Education Expenditure mean -> 903.058252 \n Education Expenditure median -> 336.000000 \n Education Expenditure standard deviation -> 1166.625835', reply_markup=markup)
        bot.send_message(message.chat.id, 'Strong skew to the right side of the selection, so we could say, that a little amount of countries are spending way more money on education, then the bigger part does.')
    elif message.text == 'Correlation between them':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Back')
        but2 = types.KeyboardButton('IQ Pure statistics')
        but3 = types.KeyboardButton('Average Income Pure statistics')
        but4 = types.KeyboardButton('Education Expenditure Pure statistics')
        but5 = types.KeyboardButton('Correlation between them')
        but6 = types.KeyboardButton('Choose by Yourself')
        markup.row(but2)
        markup.row(but3)
        markup.row(but4)
        markup.row(but6)
        markup.row(but1, but5)
        bot.send_message(message.chat.id, 'Hypothesis: Both Average Income and Education Expenditure affect the IQ level in the country, but not the other way around.')
        bot.send_message(message.chat.id, 'Proof of the hypothesis:')
        bot.send_message(message.chat.id, 'At first we need to be sure if Education Expenditure and Average Income are connected to each other.')
        with open('twographs.png', 'rb') as f:
            photo1 = f.read()
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'We can see, that both graphs look familiar, both of them have low indicators when iq is low, and both of them start fluctuating in the same places after the border of 90 IQ scores. To have a more detailed view we need to make a correlation check.')
        with open('Correlation.png', 'rb') as f:
            photo1 = f.read()
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'Here we could see, that both Education Expenditure and Average Income are connected with the IQ scores at the country on the same level.')
        with open('threelines.png', 'rb') as f:
            photo1 = f.read()
        bot.send_photo(message.chat.id, photo1)
        bot.send_message(message.chat.id, 'Here we can see that all of the countries below 80 IQ scores are poor, and also that rich countries are spending much more money on education, than the other ones.\n \n '
                         'The most important thing to notice is that poor countries could have any of the iq levels, so it is not IQ, who is affecting the average income of the country, only the education expenditure affects on IQ level of the country. \n \n'
                         'So, the hypothesis is approved')

    elif message.text == 'Dataset on kaggle':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Statistics')
        but2 = types.KeyboardButton('Dataset on kaggle')
        markup.row(but1, but2)
        bot.send_message(message.chat.id, 'https://www.kaggle.com/datasets/abhijitdahatonde/worldwide-average-iq-levels', reply_markup=markup)

    else:
        global count
        if message.text == message.text.lower():
            count = message.text[0].upper() + message.text[1:]
        else:
            count = message.text
            condition = df['country'] == count

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'country':
        condition = df['country'] == count
        fig = px.histogram(df[condition], x='country', y='IQ', title="IQ in comparison to median")
        fig.update_traces(marker=dict(color='green'))
        median = df['IQ'].median()
        fig.add_shape(
            go.layout.Shape(type="line", x0=-0.3, x1=0.3, y0=median, y1=median, line=dict(color="red", width=2), ))
        fig.update_layout(bargap=0.3, bargroupgap=0.5)
        image_bytes = fig.to_image(format='png')
        bot.send_photo(call.message.chat.id, image_bytes)

        fig = px.histogram(df[condition], x='country', y='avg_income', title="Average income in comparison to median")
        fig.update_traces(marker=dict(color='green'))
        median = df['avg_income'].median()
        fig.add_shape(
            go.layout.Shape(type="line", x0=-0.3, x1=0.3, y0=median, y1=median, line=dict(color="red", width=2), ))
        fig.update_layout(bargap=0.3, bargroupgap=0.5)
        image_bytes = fig.to_image(format='png')
        bot.send_photo(call.message.chat.id, image_bytes)

        fig = px.histogram(df[condition], x='country', y='education_expenditure', title="Education expenditure in comparison to median")
        fig.update_traces(marker=dict(color='green'))
        median = df['education_expenditure'].median()
        fig.add_shape(
            go.layout.Shape(type="line", x0=-0.3, x1=0.3, y0=median, y1=median, line=dict(color="red", width=2), ))
        fig.update_layout(bargap=0.3, bargroupgap=0.5)
        image_bytes = fig.to_image(format='png')
        bot.send_photo(call.message.chat.id, image_bytes)

        fig = px.histogram(df[condition], x='country', y='avg_temp', title="Average income in comparison to median")
        fig.update_traces(marker=dict(color='green'))
        median = df['avg_temp'].median()
        fig.add_shape(
            go.layout.Shape(type="line", x0=-0.3, x1=0.3, y0=median, y1=median, line=dict(color="red", width=2), ))
        fig.update_layout(bargap=0.3, bargroupgap=0.5)
        image_bytes = fig.to_image(format='png')
        bot.send_photo(call.message.chat.id, image_bytes)

    elif message.text == 'Automotive':
        (industry) = message.text
        industry_data = df[df['industry'] == industry]
        countries = industry_data['country'].unique()
        correlations = []
        for country in countries:        correlations.append(
            industry_data[industry_data['country'] == country]['net_worth'].corr(industry_data['net_worth']))
        ratios = []
        for correlation in correlations:
            ratios.append(correlation / max(correlations) * 100)
            fig = px.bar(countries, x=countries, y=ratios, title='Correlation between industry and countries')
            img_bytes = fig.to_image(format="png")
            bot.send_photo(message.chat.id, img_bytes, caption='Correlation between industry and countries')

bot.infinity_polling()