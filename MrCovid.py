# -*-encode:utf-8-*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from covid import Covid

updater = Updater("1396634348:AAFKhd_8C8me4h3nYeli_s7vzIosDzCKaog", use_context=True)
dp = updater.dispatcher
covid = Covid()
covid2 = Covid(source="worldometers")

def start(update, context):
    update.message.reply_text(f"Hi this is 🦠Covid-19🦠 Status Bot👋🏻😄\nSend /help to get help\n\n👻Total active cases in world: {covid2.get_total_active_cases()}\n☠️Total Deaths in world: {covid2.get_total_deaths()}\n💪🏻😁Total Recovered: {covid2.get_total_recovered()}")

def nocom(update, context):
    update.message.reply_text("⚠️Command not found!\n🆘Send /help to get help", quote=True)

def getCovid(update, context):
    if context.args == []:
        update.message.reply_text("⚠️Please Use this form\n\n/get CountryName", quote=True)
    elif len(context.args) == 2:
        EnterCountry = f"{context.args[0]} {context.args[1]}"
        try:
            CountryList = covid2.get_status_by_country_name(EnterCountry)
            ptxt = f"🏳️‍🌈Country Name: {CountryList['country']}\nConfirmed: {CountryList['confirmed']}\n🦠New Cases: {CountryList['new_cases']}\n☠️Death: {CountryList['deaths']}\n💪🏻Recovered: {CountryList['recovered']}\n🦠Active: {CountryList['active']}\n💀New Deaths: {CountryList['new_deaths']}\n🦠Total Tests: {CountryList['total_tests']}\n\n🤖Created by @MrRobot811"
            update.message.reply_text(ptxt, quote=True)
        except:
            update.message.reply_text(f"{EnterCountry} Not found!", quote=True)
    elif len(context.args) == 1:
        EnterCountry = context.args[0]
        try:
            CountryList = covid2.get_status_by_country_name(EnterCountry)
            ptxt = f"🏳️‍🌈Country Name: {CountryList['country']}\nConfirmed: {CountryList['confirmed']}\n🦠New Cases: {CountryList['new_cases']}\n☠️Death: {CountryList['deaths']}\n💪🏻Recovered: {CountryList['recovered']}\n🦠Active: {CountryList['active']}\n💀New Deaths: {CountryList['new_deaths']}\n🦠Total Tests: {CountryList['total_tests']}\n\n🤖Created by @MrRobot811"
            update.message.reply_text(ptxt, quote=True)
        except:
            update.message.reply_text(f"⚠️{EnterCountry} Not found!\nSend /countries to see Available Countries", quote=True)

def Clist(update, context):
    conlist = ""
    for con in covid2.list_countries():
        conlist += con + "\n"
    update.message.reply_text(f"Available Countries:\n\n{conlist}", quote=True)

def help(update, context):
    update.message.reply_text("/start - to Start bot and Show world status\n/get CountryName - to Show Country Status\n/countries - to Show Available Countries\n/help - to Show help\n\nMade by @MrRobot811", quote=True)

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, nocom))
dp.add_handler(CommandHandler("get", getCovid))
dp.add_handler(CommandHandler("countries", Clist))
dp.add_handler(CommandHandler("help", help))

updater.start_polling()
updater.idle()

covid2.get_total_deaths()

#print(covid.list_countries())
#print(covid.get_status_by_country_name("Iran"))
#print(covid.get_total_active_cases())

#{'country': 'Iran', 'confirmed': 264561, 'new_cases': 2388, 'deaths': 13410, 'recovered': 227561, 'active': 23590, 'critical': 3411, 'new_deaths': 199, 'total_tests': 2048049, 'total_tests_per_million': Decimal('0'), 'total_cases_per_million': Decimal('3148'), 'total_deaths_per_million': Decimal('160'), 'population': Decimal('84030066')}
#{'id': '97', 'country': 'Iran', 'confirmed': 264561, 'active': 23590, 'deaths': 13410, 'recovered': 227561, 'latitude': 32.427908, 'longitude': 53.688046, 'last_update': 1594820077000}
