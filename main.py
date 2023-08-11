# -*- coding: utf-8 -*-
from urllib.parse import quote
from aiogram import Bot
import aiohttp
import hashlib
import config
import keep_alive
import asyncio
import csv
from pyrogram import Client
from pyrogram.types import InputPhoneContact
import json
import requests
from requests.structures import CaseInsensitiveDict
from aiogram import Bot
from bs4 import BeautifulSoup
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
import random
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import Throttled
import socket
# --------------------------------------------------------

token='5308416438:AAGhpSnx2eUyJRgH6cKYGUsF-mCWkmKuTL4'
#----------------------------
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


# --------------------------------------------------------------

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("❌* Не так быстро! *Подождите 3 секунды.", parse_mode='Markdown')
  
# --------------------------------------------------------------
@dp.message_handler(commands=['start'])
async def main(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id='@visiiione', user_id=message.from_user.id)):
        global z
        z = 0
        subn = InlineKeyboardButton('🎓 Подписаться', url='https://t.me/+JI-8OuLfufU5ZGU1')
        subkaa = InlineKeyboardMarkup.add(subn)
        await message.answer('🕷️ Приветствую, бот принимает запросы по:\n\n📲 Номер телефона\n🐦‍⬛ Адрес эл. почты\n🥷 Telegram ID\n🕷️ IP-адрес\n\n🐜 Фио', reply_markup=nav.menu_b, parse_mode="Markdown")
        arg = message.get_args().replace("['", '').replace("']", '')
        argi = arg
        with open('exists.txt') as file:
          for line in file:
            if str(message.from_user.id) in line:
              
              z = 1
        
        with open('refff.txt', 'a') as file:
              print(z)
              if z == 0:
                ff = str(arg)+'\n'
                file.write(ff+'\n')
                await bot.send_message(argi, text='🥷 По вашей реферальной ссылке перешел 1 чел', parse_mode='Markdown')
                
        with open('exists.txt', 'a') as file:
          file.write(str(message.from_user.id)+'\n')
    else:
        await message.answer('Подпишитесь, для дальнейшего пользования ботом', reply_markup=nav.subchanneldonw)
    
# --------------------------------------------------------------
# Обработчик ---------------------------------------------------

  






  
@dp.message_handler()
@dp.throttled(anti_flood,rate=3)
async def buttons(message: types.Message):
    global tarifan
    tarifan = 0
    user_id = str(message.from_user.id)
    with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                if user_id in line:
                  tarifan = 1
    token_yandex = '7d982772d748841b9bc505d72c131845b59f4d3977b7a303bb8a6809a609c892'
    indata = message.text
    phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
    print(str(tarifan)+'t')
    try:
      phonse = int(phonse)
      ogogg = 0
    except:
      ogogg = 1
    if 'import' in indata:
      pass
    if ogogg == 0:
        phonse = indata.replace('+', '').replace('-', '').replace('(', '').replace(')', '').replace(' ', '')
        lenz = len(phonse)
        validat = requests.get('	https://demo.phoneinfoga.crvx.fr/api/numbers/'+phonse+'/scan/local')
        if validat.status_code == 200:
          with open('alarm.txt', encoding='utf-8', errors='ignore') as file:
              for line in file:
                  if phonse in line:
                    id = line.split(';')[0]
                    await bot.send_message(id, text="🕷️ Срочное уведомление! Вас пытались пробить, но мы отклонили запрос", parse_mode='Markdown')
          if lenz == 11:
              global phone
              phone = phonse[1:]
              phonse = phonse[1:]
              phonse = '7' + phonse
          else:
              phone = phonse
          # Дефолт данные -------------------
  
          fstep_msg = await message.answer('🎩 Определяю город, и оператора', parse_mode="Markdown")
          async with aiohttp.ClientSession() as session:
            async with session.get(f'https://fincalculator.ru/api/tel/{phonse}') as SBnum:
              #SBnum = requests.get(f"https://fincalculator.ru/api/tel/{phonse}")
              datae = await SBnum.json()
          # перенос номера -----------------------------
          
          #urlMNP = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phonse}"
          mnp = 'Неизвестно'
          whatsapp = InlineKeyboardButton('🐦‍⬛ Whatsapp', url='wa.me/' + phonse)
          viber = InlineKeyboardButton('🕷️ Viber', url='viber.click/' + phonse)
          telega = InlineKeyboardButton('🎩 Телеграм', url='t.me/+' + phonse)
          yandexs = InlineKeyboardButton('🎓 Яндекс', url='https://yandex.ru/search/?text='+phonse)
          goog = InlineKeyboardButton('🐜 Google', url='https://www.google.com/search?q='+phonse)
  
          name='empty'
          head = {
                "Host": "api.vkpay.io",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://ea-miniapp.vkpay.io",
                "X-App-Params": '{"vk_access_token_settings":"notify,friends,groups","vk_app_id":"7131443","vk_are_notifications_enabled":"0","vk_experiment":"eyIxNjE4IjowfQ","vk_is_app_user":"1","vk_is_favorite":"0","vk_language":"ru","vk_platform":"desktop_web","vk_ref":"other","vk_ts":"1650541292","vk_user_id":"616028231","sign":"zOQRbuQQcD95SmmTcHR_EtmeDkhwL4VCjQ7LS6PcYMI"}',
                "X-VKApp-Token": "f7b1f08d-ee0c-479f-bdb0-912bd38ddaa9"
            }
           
          async with aiohttp.ClientSession(headers=head) as session:
                  async with session.post("https://api.vkpay.io/visa-alias/p2p/options", json={"phone": str(phonse)}) as r:
                    r = await r.json()
                    print(r)
                    data = r
                    # data = json.loads(r.text)
            
                    name = data["additional_data"]["user_name"].replace(' ', '+')
          vkments = InlineKeyboardButton('🎩 Поиск ВК', url='https://www.social-searcher.com/social-buzz/?q5='+name)
          if name != '':
            variations = InlineKeyboardMarkup().add(whatsapp, viber, telega, yandexs, goog, vkments)
          else:
            variations = InlineKeyboardMarkup().add(whatsapp, viber, telega, yandexs, goog)
  
          await fstep_msg.delete()
          mnp_msg = await message.answer('🕷️ Определяем, есть ли у данного абонента второй номер', parse_mode="Markdown")
          # Перенос номера ------------------------
          mnp = ''
          try:
            urlMNP = f"https://xn----dtbofgvdd5ah.xn--p1ai/php/mnp.php?nomer={phonse}"
            mnpSiteSourc = requests.get(urlMNP).text.strip()
            mnp = mnpSiteSourc.replace('no',
                                           'Номер не переносился')
          except:
            mnp = 'Неизвестно'
          try:
              countrys = datae["country"]
              regions = datae["region"]
              operators = datae["operator"]
              if countrys != 'Россия':
                  fstep = f'📲 *Номер телефона:* `{phonse}`\n ├ *Страна:* `{countrys}`\n ├ *Перенос номера:* `{mnp}`\n └ *Оператор:* `{regions}`'
                  fstep_html = f'Страна {countrys}<br>Перенос номера: {mnp}<br>Оператор: {regions}'
              else:
                  fstep = f'🎩 Номер телефона:{phonse}\n Страна: {countrys}\n Регион:`{regions}`\n ├ *Перенос номера:* `{mnp}`\n └ *Оператор:* `{operators}`'
                  fstep_html = f'Страна {countrys}<br>Регион: {regions}<br>Перенос номера: {mnp}<br>Оператор: {operators}'
          except:
              countrys = 'Не опознано'
              regions = 'Не опознано'
              operators = 'Не опознано'
          await mnp_msg.delete()
          # Сбер -----------------------------------------
          sber_msg = await message.answer('🕸️ Ищем сбер', parse_mode="Markdown")
          sberbank_message = ''
          maskedPhone = ''
          tarifan = 0
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                      if user_id in line:
                        tarifan = 1
          if tarifan == 1:
            try:
                sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?phone={phone}")
                datas = sberbank.json()
    
                get_date = datas['client']['createdDate']
                get_date2 = get_date[:10]
                rep1 = get_date2.replace(".01.", " января ")
                rep2 = rep1.replace(".02.", " февраля ")
                rep3 = rep2.replace(".03.", " марта ")
                rep4 = rep3.replace(".04.", " апреля ")
                rep5 = rep4.replace(".05.", " мая ")
                rep6 = rep5.replace(".06.", " июня ")
                rep7 = rep6.replace(".07.", " июля ")
                rep8 = rep7.replace(".08.", " августа ")
                rep9 = rep8.replace(".09.", " сентября ")
                rep10 = rep9.replace(".10.", " октября ")
                rep11 = rep10.replace(".11.", " ноября ")
                rep12 = rep11.replace(".12.", " декабря ")
                rep13 = get_date[11:-7]
    
                maskedPhone = datas['client']['maskedPhone']
                created_date = f'{rep12} г. в {rep13}'
                sberbank_message = f"🕸️ Сбербанк: есть({created_date})\n"
                sberbank_message_html = f"Сбербанк: есть ({created_date})<br>"
            except:
                sberbank_message = ''
                sberbank_message_html = ''
            await sber_msg.delete()
          else:
            try:
                sberbank = requests.post(f"https://securepayments.sberbank.ru/sbersafe/client/find?phone={phone}")
                datas = sberbank.json()
    
                get_date = datas['client']['createdDate']
                get_date2 = get_date[:10]
                rep1 = get_date2.replace(".01.", " января ")
                rep2 = rep1.replace(".02.", " февраля ")
                rep3 = rep2.replace(".03.", " марта ")
                rep4 = rep3.replace(".04.", " апреля ")
                rep5 = rep4.replace(".05.", " мая ")
                rep6 = rep5.replace(".06.", " июня ")
                rep7 = rep6.replace(".07.", " июля ")
                rep8 = rep7.replace(".08.", " августа ")
                rep9 = rep8.replace(".09.", " сентября ")
                rep10 = rep9.replace(".10.", " октября ")
                rep11 = rep10.replace(".11.", " ноября ")
                rep12 = rep11.replace(".12.", " декабря ")
                rep13 = get_date[11:-7]
    
                maskedPhone = datas['client']['maskedPhone']
                created_date = f'{rep12} г. в {rep13}'
                sberbank_message = f"🕸️ Сбербанк: есть\n"
                sberbank_message_html = 'Сбербанк: есть<br>'
            except:
                sberbank_message = ''
                sberbank_message_html = ''
            await sber_msg.delete()
          # 2GIS ----------------------------------------
          tgis_html = ''
          tgis = ''
          head = {'Host': 'id.2gis.com',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
  'Content-Length': '30'}
          rt = requests.post('https://id.2gis.com/api/v1/send_confirm_sms',
                             json={"phone": phonse, "locale": "ru-RU"}, headers=head).json()
          print(rt)
          try:
              exe = rt['phone']
              vho = 1
          except Exception as e:
              print(f'Exception 2GIS is: {e}')
              tgis = ''
              vho = 0
          if vho == 1:
              tgis = '📗 *Аккаунт на ГИС: есть'
              tgis_html = 'ДубльГИС: существует<br>'
          else:
                    tgis = ''
                    tgis_html = ''
                
          
                  
          
          # Одноклассники -------------------------------
          ok_msg = await message.answer('🕷️ Чекаю, есть ли аккаунт в одноклассниках',
                                        parse_mode="Markdown")
          # одноклассники
          session = requests.Session()
          session.get(
              f'https://www.ok.ru/dk?st.cmd=anonymMain&st.accRecovery=on&st.error=errors.password.wrong&st.email={phonse}')
          request = session.get(
              f'https://www.ok.ru/dk?st.cmd=anonymRecoveryAfterFailedLogin&st._aid=LeftColumn_Login_ForgotPassword')
          root_soup = BeautifulSoup(request.content, 'html.parser')
          soup = root_soup.find('div', {'data-l': 'registrationContainer,offer_contact_rest'})
          if soup:
              account_info = soup.find('div', {'class': 'ext-registration_tx taCenter'})
              masked_email = soup.find('button', {'data-l': 't,email'})
              masked_phone = soup.find('button', {'data-l': 't,phone'})
              if masked_phone:
                  masked_phone = masked_phone.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
              if masked_email:
                  masked_email = masked_email.find('div', {'class': 'ext-registration_stub_small_header'}).get_text()
                  masked_email = f'Почта: `{masked_email}`,'
              else:
                  masked_email = ''
              if account_info:
                  masked_name = account_info.find('div', {'class': 'ext-registration_username_header'})
                  if masked_name:
                      masked_name = masked_name.get_text()
                  account_info = account_info.findAll('div', {'class': 'lstp-t'})
                  if account_info:
                      profile_info = account_info[0].get_text()
                      profile_registred = account_info[1].get_text()
                  else:
                      profile_info = None
                      profile_registred = None
              else:
                  pass
          await ok_msg.delete()
  
          try:
              age = profile_info[:7].replace(',', '')
              cityok = profile_info[8:].replace(',', '')
              age = f''
              cityok = f'`{cityok}`'
              tarifan = 0
              user_id = str(message.from_user.id)
              with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                        for line in file:
                          if user_id in line:
                            tarifan = 1
              if tarifan == 1:
                ok = f'\n Одноклассники:{masked_name}` (`{profile_info}`, {masked_email} `{profile_registred})`\n'
                ok_html = f'Одноклассники: {masked_name} ({profile_info},<br> {masked_email}, {profile_registred})<br>'.replace('`', '').replace(',,', ',')
              elif tarifan == 0:
                ok = f'\nОдноклассники: нашел\n'
                ok_html = 'Одноклассники: найдены<br>'
              
          except:
              ok = ''
              cityok = ''
              age = ''
              masked_email = ''
              ok_html = ''
          # Яндекс ---------------------------------------
          yand_msg = await message.answer('🕸️ Чекаю, привязан ли яндекс к номеру',
                                          parse_mode="Markdown")
          # yandex
          try:
              eqereq = message.text.strip()
              email_login = (eqereq.split("@"))[0]
              async with aiohttp.ClientSession() as session:
                async with session.get(f"https://yandex.ru/collections/api/users/{email_login}") as yandex:
                  try:
                      yamail = phonse + '@yandex.ru'
                  except:
                      yamail = ''
                  yamailo = f', `{yamail}`'
                  yadata = await yandex.json()
                  public_id = yadata['public_id']
                  display_name = yadata['display_name']
                  try:
                      yaname = f' ({display_name})'
                  except:
                      yaname = ''
                  try:
                    if tarifan != 0:
                      yandexx = f'\n㊗ *Яндекс ID:* `{public_id}`{yaname}\n'
                      yandexx_html = f'Яндекс: {public_id}{yaname}<br>'
                    else:
                      yandexx = f'\n㊗ *Яндекс ID:* `найден`\n'
                      yandexx_html = f'Яндекс: найден<br>'
                  except:
                    if tarifan != 0:
                      yandexx = f'\n㊗ *Яндекс ID:* `{public_id}`\n'
                      yandexx_html = f'Яндекс: {public_id}<br>'
                    else:
                      yandexx = f'\n㊗ *Яндекс ID:* `найден`\n'
                      yandexx_html = f'Яндекс: найден<br>'
          except:
                  display_name = ''
                  public_id = ''
                  yandexx = ''
                  yandexx_html = ''
                  yamail = ''
                  yaname = display_name
                  if yandexx == '':
                    yamailo = ''
          await yand_msg.delete()
          # ВКонтакте -----------------------------------
          nameqs_html = ''
          vkmsg = await message.answer('🤖 *Ищем ВКонтакте...*', parse_mode="Markdown")
          try:
            head = {
                "Host": "api.vkpay.io",
                "Accept": "application/json, text/plain, */*",
                "Origin": "https://ea-miniapp.vkpay.io",
                "X-App-Params": '{"vk_access_token_settings":"notify,friends,groups","vk_app_id":"7131443","vk_are_notifications_enabled":"0","vk_experiment":"eyIxNjE4IjowfQ","vk_is_app_user":"1","vk_is_favorite":"0","vk_language":"ru","vk_platform":"desktop_web","vk_ref":"other","vk_ts":"1650541292","vk_user_id":"616028231","sign":"zOQRbuQQcD95SmmTcHR_EtmeDkhwL4VCjQ7LS6PcYMI"}',
                "X-VKApp-Token": "f7b1f08d-ee0c-479f-bdb0-912bd38ddaa9"
            }
            async with aiohttp.ClientSession(headers=head) as session:
                  async with session.post("https://api.vkpay.io/visa-alias/p2p/options", json={"phone": str(phonse)}) as r:
                    r = await r.json()
                    print(r)
                    data = r
                    # data = json.loads(r.text)
            
                    name = data["additional_data"]["user_name"]
                    hasVk = data["additional_data"]["has_vk"]
                    vk_gua = name.replace(' ', '+')
                    if name != '':
                        vk = '🤖 *ВКонтакте:* `' + name + '`\n—  Сведения про ВК пользователя: `vk.com/search?c[section]=name&c[q]=' + vk_gua + '`\n—  Получить город и аватарку: `vk.com/restore`\n'
                        vk_html = 'ВКонтакте: '+name+'<br>'
                    else:
                        vk = ''
                        vk_html = ''
            await vkmsg.delete()
          except:
            vk = ''
          # ДомРУ ----------------------------------------
          address = ''
          domru_msg = await message.answer('🏠 *Ищем адрес по договору DOM.RU...*', parse_mode="Markdown")
          tarifan = 0
          user_id = str(message.from_user.id)
          with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                    for line in file:
                      if user_id in line:
                        tarifan = 1
          if tarifan == 1:
            if "#" in message.text:
                regions = 'Иркутская область'
            if "-" in message.text:
                regions = 'Иркутская область'
            if regions == 'Москва и Московская область':
                gorod = 'msk'
            elif regions == 'Иркутская область':
                gorod = 'irkutsk'
            elif regions == 'Алтайский край':
                gorod = 'barnaul'
            elif regions == 'Пермский край':
                gorod = 'ber'
            elif regions == 'Брянская область':
                gorod = 'bryansk'
            elif regions == 'Волгоградская область':
                gorod = 'volgograd'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Удмуртская республика':
                gorod = 'votkinsk'
            elif regions == 'Нижегородская область':
                gorod = 'dzr'
            elif regions == 'Ульяновская область':
                gorod = 'ulsk'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Республика Марий Эл':
                gorod = 'yola'
            elif regions == 'Респубика Татарстан':
                gorod = 'kazan'
            elif regions == 'Кировская область':
                gorod = 'kirov'
            elif regions == 'Краснодарский край':
                gorod = 'krd'
            elif regions == 'Красноярский край':
                gorod = 'krsk'
            elif regions == 'Курганская область':
                gorod = 'kurgan'
            elif regions == 'Курская область':
                gorod = 'kursk'
            elif regions == 'Липецкая область':
                gorod = 'lipetsk'
            elif regions == 'Челябинская область':
                gorod = 'chel'
            elif regions == 'Тамбовская область':
                gorod = 'mich'
            elif regions == 'Новосибирская область':
                gorod = 'nsk'
            elif regions == 'Омская область':
                gorod = 'omsk'
            elif regions == 'Оренбургская область':
                gorod = 'oren'
            elif regions == 'Пензенская область':
                gorod = 'penza'
            elif regions == 'Ростовская область':
                gorod = 'rostov'
            elif regions == 'Рязанская область':
                gorod = 'ryazan'
            elif regions == 'Самарская область':
                gorod = 'samara'
            elif regions == 'Санкт-Петербург':
                gorod = 'interzet'
            elif regions == 'Саратовская область':
                gorod = 'saratov'
            elif regions == 'Воронежская область':
                gorod = 'voronezh'
            elif regions == 'Томская область':
                gorod = 'tomsk'
            elif regions == 'Тверская область':
                gorod = 'tver'
            elif regions == 'Тульская область':
                gorod = 'tula'
            elif regions == 'Тюменская область':
                gorod = 'tmn'
            elif regions == 'Республика Бурятия':
                gorod = 'ulu'
            elif regions == 'Республика Башкоторстан':
                gorod = 'ufa'
            elif regions == 'Республика Чувашия':
                gorod = 'cheb'
            elif regions == 'Ярославская область':
                gorod = 'yar'
            else:
                gorod = "msk"
            urldru = 'https://api-profile.domru.ru/v1/unauth/contract-asterisked?contact=' + phonse + '&amp;isActive=1'
    
            headersd = CaseInsensitiveDict()
            headersd["Host"] = "api-profile.domru.ru"
            headersd["Domain"] = gorod
            async with aiohttp.ClientSession(headers=headersd) as session:
              async with session.get(urldru) as resp:
                resp = await resp.json()
                domruu = ''
                try:
                  dataa = resp['contacts'][0]['address']
                  domruu = f'🔌 *Найден договор с интернет провайдером ДОМ.RU*\n🏠 Адрес предоставления услуги: `{dataa}`\n'
                  domruu_html = 'ДомРУ: '+dataa+'<br>'
                except:
                  domruu = ''
                  domruu_html = ''
                phonke = '+'+phonse
                phonee = phonse
                phonio = phonee.replace('', ' ')
                dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                adcs = ''
                try:
                  rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                  adcs = ''
                  address_html = ''
                  for i in range(len(rw)):
                                if phonke in rw[i]:
                                    ee = i
                                    datacd = rw[ee]
                                    print(rw[ee])
                                    
                                    if datacd[1] != '':
                                      adcs = adcs+f'{datacd[1]}, {datacd[2]}, дом {datacd[3]}, подьезд {datacd[4]}, кв {datacd[5]}\n'
                                else:
                                      pass
                  try:
                                dataa = resp['contacts'][0]['address']
                                address = f'🏠 *Возможные места проживания*: `{adcsasdsda}`\n'
                                address_html = f'Возможные адреса: {adcsasdsda}<br>'
                  except:
                              if adcs != '':
                                address = f'🏠 *Возможные места проживания*: `{adcs}`\n'
                                address_html = f'Возможные адреса: {adcs}<br>'
                except:
                  address = ''
                  address_html = ''
          elif tarifan == 0:
              if "#" in message.text:
                  regions = 'Иркутская область'
              if "-" in message.text:
                  regions = 'Иркутская область'
              if regions == 'Москва и Московская область':
                  gorod = 'msk'
              elif regions == 'Иркутская область':
                  gorod = 'irkutsk'
              elif regions == 'Алтайский край':
                  gorod = 'barnaul'
              elif regions == 'Пермский край':
                  gorod = 'ber'
              elif regions == 'Брянская область':
                  gorod = 'bryansk'
              elif regions == 'Волгоградская область':
                  gorod = 'volgograd'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Удмуртская республика':
                  gorod = 'votkinsk'
              elif regions == 'Нижегородская область':
                  gorod = 'dzr'
              elif regions == 'Ульяновская область':
                  gorod = 'ulsk'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Республика Марий Эл':
                  gorod = 'yola'
              elif regions == 'Респубика Татарстан':
                  gorod = 'kazan'
              elif regions == 'Кировская область':
                  gorod = 'kirov'
              elif regions == 'Краснодарский край':
                  gorod = 'krd'
              elif regions == 'Красноярский край':
                  gorod = 'krsk'
              elif regions == 'Курганская область':
                  gorod = 'kurgan'
              elif regions == 'Курская область':
                  gorod = 'kursk'
              elif regions == 'Липецкая область':
                  gorod = 'lipetsk'
              elif regions == 'Челябинская область':
                  gorod = 'chel'
              elif regions == 'Тамбовская область':
                  gorod = 'mich'
              elif regions == 'Новосибирская область':
                  gorod = 'nsk'
              elif regions == 'Омская область':
                  gorod = 'omsk'
              elif regions == 'Оренбургская область':
                  gorod = 'oren'
              elif regions == 'Пензенская область':
                  gorod = 'penza'
              elif regions == 'Ростовская область':
                  gorod = 'rostov'
              elif regions == 'Рязанская область':
                  gorod = 'ryazan'
              elif regions == 'Самарская область':
                  gorod = 'samara'
              elif regions == 'Санкт-Петербург':
                  gorod = 'interzet'
              elif regions == 'Саратовская область':
                  gorod = 'saratov'
              elif regions == 'Воронежская область':
                  gorod = 'voronezh'
              elif regions == 'Томская область':
                  gorod = 'tomsk'
              elif regions == 'Тверская область':
                  gorod = 'tver'
              elif regions == 'Тульская область':
                  gorod = 'tula'
              elif regions == 'Тюменская область':
                  gorod = 'tmn'
              elif regions == 'Республика Бурятия':
                  gorod = 'ulu'
              elif regions == 'Республика Башкоторстан':
                  gorod = 'ufa'
              elif regions == 'Республика Чувашия':
                  gorod = 'cheb'
              elif regions == 'Ярославская область':
                  gorod = 'yar'
              else:
                  gorod = "msk"
              urldru = 'https://api-profile.domru.ru/v1/unauth/contract-asterisked?contact=' + phonse + '&amp;isActive=1'
      
              headersd = CaseInsensitiveDict()
              headersd["Host"] = "api-profile.domru.ru"
              headersd["Domain"] = gorod
              async with aiohttp.ClientSession(headers=headersd) as session:
                async with session.get(urldru) as resp:
                  resp = await resp.json()
                  domruu = ''
                  try:
                      dataa = resp['contacts'][0]['address']
                      domruu = f'🔌 *Найден договор с интернет провайдером ДОМ.RU*\n🏠 Адрес предоставления услуги: `{dataa}`\n'
                      domruu_html = f'ДомРУ: {dataa}<br>'
                  except:
                    domruu = ''
                    domruu_html = ''
                  phonke = '+'+phonse
                  phonee = phonse
                  phonio = phonee.replace('', ' ')
                  dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                  try:
                    rw = requests.get('https://saverudata.info/db/'+dd+'/00000-99999.json').json()
                    adcs = ''
                    for i in range(len(rw)):
                                  if phonke in rw[i]:
                                      ee = i
                                      datacd = rw[ee]
                                      print(rw[ee])
                                      
                                      if datacd[1] != '':
                                        adcs = adcs+f'{datacd[1]}, {datacd[2]}, дом {datacd[3]}, подьезд {datacd[4]}, кв {datacd[5]}\n'
                                  else:
                                        pass
                    try:
                        address_html = ''
                        address = osdfo
                    except:
                        if adcs != '':
                          address = f'🏠 *Возможные места проживания*: `найдено`\n'
                          address_html = f'Возможные адреса: найдено<br>'
                  except:
                    address = ''
                    address_html = ''
          await domru_msg.delete()
          # Телеграм -------------------------------------
          tg = ''
          tg_html = ''
          rt = requests.get('https://capitalcloudytriangle.hkfdsfsdfh.repl.co/info?d='+phonse).content.decode("utf-8", "ignore")
          rt = str(rt).replace('b', '').replace("'", '')
          print(rt)
          tg = '🛅 *Telegram: *`'+str(rt)+'`\n'
          tg = tg.replace('🛅 *Telegram: *`Упс... Такого контакта в TG не обнаружено.`\n', '')
          tg_html = 'Telegram: '+str(rt)+"<br>"
          tg_html = tg_html.replace('Telegram: Упс... Такого контакта в TG не обнаружено.<br>', 'Telegram: ')
          # Чек вацап
          nameqs = ''
          try:
            whatt = await message.answer('✅ *Проверяем существование Whatsapp...*', parse_mode='Markdown')
            whwh = ''
            permq = 1
            with open('tickets.txt', encoding='utf-8', errors='ignore') as file:
                              for line in file:
                                if user_id in line:
                                  permq = 1
            if permq == 1:
              rwh = requests.get('http://ovh.foxodever.com:65535/whatsapp/'+phonse).json()
              whwh_nac = rwh['exists']
              print(whwh)
              whwh = str(whwh_nac).replace('True', '\n✅* Whatsapp:* `есть`').replace('False', '')
              whwh_html = str(whwh_nac).replace('True', 'Whatsapp: есть<br>').replace('False', '')
            else:
              whwh = ''
              whwh_html = ''
            await whatt.delete()
          except:
            whwh = ''
            whwh_html = ''
          # Кол-во обьявлений
          obbd = await message.answer('🏪* Считаем кол-во обьявлений в интернете...*', parse_mode="Markdown")
          rrtr = requests.get('http://ovh.foxodever.com:65535/avito/'+phonse).json()
          try:
            clvobd = str(rrtr['count'])
            clvob = f'\n🏪 *Кол-во обьявлений в интернете:* `{clvobd}`'
            clvob_html = f'Кол-во обьявлений в интернете: {clvobd}<br>'
          except:
            clvob = ''
            clvob_html = ''
          await obbd.delete()
          gogop = 1
          if gogop == 1:
                      phonke = '+'+phonse
                      phonee = phonse
                      phonio = phonee.replace('', ' ')
                      dd = phonio.split()[0]+'/'+phonio.split()[1]+'/'+phonio.split()[2]+'/'+phonio.split()[3]+'/'+phonio.split()[4]+'/'+phonio.split()[5]
                      
                      
                      fiof = ''
                      emcd = ''
                      print(phonke)
                      fight = 0
                      nameqs = ''
                      fiof_html = ''
                      emcd_html = ''
                      nameqs_html = ''
                      
          try: 
              URLavito = "https://opredelitel.com/pay/7" + phone
              HEADERS = {
                  "User-Agent":
                      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
              }
              ra = requests.get(URLavito, headers=HEADERS)
              soup = BeautifulSoup(ra.content, 'html.parser')
              items = soup.findAll('div', class_='preview_da_line')
              comps = []
              for item in items:
                  comps.append({
                      'titlew':
                          item.find('div', class_='da_title').get_text(strip=True),
                      'infow':
                          item.find('div', class_='da_info').get_text(strip=True)
                  })
          except:
              pass
          try:
              for comp in comps:
                
                  comp['infow'] = comp['infow'].replace(' / Адрес: скрыт в ознакомительном отчёте', '')
                  obyavss = obyavss+f"Найдено обьявление: {comp['titlew']}<br>Подробная информация: {comp['infow']}<br><br>"
              if obyavss == '':
                obyavss = 'Не обнаружены'
          except:
              pass