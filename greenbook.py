

from telegram import Update, User,Contact,InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup,CallbackQuery,ReplyKeyboardRemove
import os
from typing import Any, Dict, Tuple
from dotenv import load_dotenv 
from telegram.ext import MessageHandler,CommandHandler,filters,Application,ContextTypes,ConversationHandler,CallbackQueryHandler
from databasehandler import NEWROOM, USERUPDATE,NEWUSER,CHECKUSER,SEARCHROOM
load_dotenv()

# starting all functions

async def Profile(update:Update, context:ContextTypes.DEFAULT_TYPE):
    pass

async def AskName(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    context.user_data['Name']=update.message.text
    context.user_data['UniqueId']=update.message.chat.id
    print(context.user_data.get('UniqueId'))
    try:
        print("Adding user to database")
        data = NEWUSER(str(context.user_data.get('Name')),str(context.user_data.get('PhoneNumber')),str(context.user_data.get('UniqueId')))
        print(data[1])
        print(data)
        keyboard = [
                    [InlineKeyboardButton("Find Room",callback_data="find")],
                    [InlineKeyboardButton("Add Room",callback_data="addroom")],
                ]
        await update.message.reply_text("Choose a service to start -",reply_markup=InlineKeyboardMarkup(keyboard))
        return 3
    except Exception as e:
       
        await update.message.reply_text("Sorry Server is busy. Check Back Later. /start")
    
    ConversationHandler.END

async def ExitAll(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Good Bye Thanks for Using. start again /start ",) 
    return ConversationHandler.END
async def ExitFor(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("Good Bye Thanks for Using. start again /start ",) 
    context.user_data['OFFSET'] = 0
    return ConversationHandler.END


async def CheckProfile(update:Update, context:ContextTypes.DEFAULT_TYPE):
    if(update.message.text == "Exit"):
        await update.message.reply_text("Conversation ended.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    else:
        await update.message.reply_text("Hello",reply_markup=ReplyKeyboardRemove())
        to = update.message.chat.id
        context.user_data['PhoneNumber']=update.message.contact.phone_number
        try:
            rat = CHECKUSER(to)
            print(update.message.contact.first_name)
            print(type(to))
            print(rat[2])
            print(type(rat[2]))
            if(rat[2]!=0):
                keyboard = [
                    [InlineKeyboardButton("Find Room",callback_data="find")],
                    [InlineKeyboardButton("Add Room",callback_data="addroom")],
                ]
                await update.message.reply_html(
'''
Hello sir,
Welcome Back.
Choose a Service to Begin.
''',reply_markup=InlineKeyboardMarkup(keyboard)
            )
                return 3
                
            else:
                await update.message.reply_html(
'''
Hello sir,
You are New to us.
What is your Name ?
'''
            )
            return 2
        except Exception as e:
            print(e)
            await update.message.reply_text("Soory Server is not Responding. Try back later. /start")
            return ConversationHandler.END
        
    
async def Help(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_html(
'''
Watch this video.
<a>https://youtu.be/CMGdVo15Z1g</a>

Lets begin /start
'''
    )
async def Start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    context.user_data['OFFSET'] = 0
    Keyboard = [[
        KeyboardButton("Continue",request_contact=True),
        KeyboardButton("Exit"),
            
    ]]
   
    await update.message.reply_html(
'''
Hello This Bot can help you to find and sell Rooms. Share Your Phone Number to Continue
/help - How to use
''',reply_markup=ReplyKeyboardMarkup(Keyboard,one_time_keyboard=True,resize_keyboard=True))
    return 1


async def AddRoom_type(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("reached add room type")
    query = update.callback_query
    await query.answer()
    keyboard = [
                    [InlineKeyboardButton("Room",callback_data="01")],
                    [InlineKeyboardButton("Flat",callback_data="02")],
                    [InlineKeyboardButton("Shop/Commercial",callback_data="03")],
                    [InlineKeyboardButton("PG/Hostel",callback_data="04")],
                ]
    await  query.edit_message_text(
'''
Give us some details to add your Property to Our List. 
What type of Propery is Yours 
''',reply_markup=InlineKeyboardMarkup(keyboard))
    return 3

async def AddRoom_water(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("reached add water type")
    query = update.callback_query
    await query.answer()
    context.user_data['RoomType']=query.data
    print(query.data)
    keyboard = [
                    [InlineKeyboardButton("Yes",callback_data="05")],
                    [InlineKeyboardButton("No",callback_data="06")],
                    
                ]
    await query.edit_message_text(
'''
Do You have pure dirinking water.
''',reply_markup=InlineKeyboardMarkup(keyboard))
    return 3

async def AddRoom_inverter(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("reached add inverter type")
    query = update.callback_query
    await query.answer()
    context.user_data['RoomWater']=query.data
    print(query.data)
    keyboard = [
                    [InlineKeyboardButton("Yes",callback_data="07")],
                    [InlineKeyboardButton("No",callback_data="08")],
                    
                ]
    await query.edit_message_text(
'''
Do You have Inverter.
''',reply_markup=InlineKeyboardMarkup(keyboard))
    return 3

async def AddRoom_wifi(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("reached add wifi type")
    query = update.callback_query
    await query.answer()
    context.user_data['RoomInverter']=query.data
    print(query.data)
    keyboard = [
                    [InlineKeyboardButton("Yes",callback_data="09")],
                    [InlineKeyboardButton("No",callback_data="010")],
                    
                ]
    await query.edit_message_text(
'''
Do You have wifi.
''',reply_markup=InlineKeyboardMarkup(keyboard))
    return 3

async def AddRoom_furniture(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("reached add furniture type")
    query = update.callback_query
    await query.answer()
    context.user_data['RoomWifi']=query.data
    print(query.data)
    keyboard = [
                    [InlineKeyboardButton("Yes",callback_data="011")],
                    [InlineKeyboardButton("No",callback_data="012")],
                    
                ]
    await query.edit_message_text(
'''
Do You have furniture (fan,bed,light).
''',reply_markup=InlineKeyboardMarkup(keyboard))
    return 3
async def Gettingforcordss(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(type(context.user_data.get('OFFSET')))
    tat = int(context.user_data.get('OFFSET'))
    lat  = context.user_data.get('Slat')
    log  = context.user_data.get('Slot')
    data = SEARCHROOM(lat,log,6,tat)
    if(data[0]==0):
        for i in range(len(data[3])):
            ren = data[3][i][10]
            whc = data[3][i][9]
            lad = data[3][i][7]
            rmt = data[3][i][3]
            inv = data[3][i][4]
            wat = data[3][i][5]
            
            wif = data[3][i][6]
            Pnh = data[3][i][8]
            await update.message.reply_html(
'''
Monthly Rent - {}
Room Type -    {}
Address -      {}
WhoCanLive -   {}
Facilities 
Pure Water -   {}
Wifi -         {}
Inverter -     {}
Mobile -       {}
'''.format(ren,rmt,lad,whc,wat,wif,inv,Pnh)
            )
        await update.message.reply_text("All data found /MORE  /EXIT",)
        context.user_data['OFFSET'] = int(context.user_data.get('OFFSET'))+len(data[3])
        return 3
    else:
        await update.message.reply_text("Soory can not show data now. Chech back later. /start")
        return ConversationHandler.END
    
    
async def GettingDatacords(update:Update, context:ContextTypes.DEFAULT_TYPE):
    cord = update.message.text
    cord = cord.split(",")
    lat = cord[1]
    log = cord[0]
    context.user_data['Slat']=lat
    context.user_data['Slot']=log
    tat = int(context.user_data.get('OFFSET'))
    data = SEARCHROOM(lat,log,6,tat)
    if(data[0]==0):
        for i in range(len(data[3])):
            ren = data[3][i][10]
            whc = data[3][i][9]
            lad = data[3][i][7]
            rmt = data[3][i][3]
            inv = data[3][i][4]
            wat = data[3][i][5]
            
            wif = data[3][i][6]
            Pnh = data[3][i][8]
            
            await update.message.reply_html(
'''
Monthly Rent - {}
Room Type -    {}
Address -      {}
WhoCanLive -   {}
Facilities 
Pure Water -   {}
Wifi -         {}
Inverter -     {}
Mobile -       {}
'''.format(ren,rmt,lad,whc,wat,wif,inv,Pnh)
            )
        await update.message.reply_text("All data found /MORE  /EXIT",)
        context.user_data['OFFSET'] = int(context.user_data.get('OFFSET'))+len(data[3])
        return 3
    else:
        await update.message.reply_text("Soory can not show data now. Chech back later. /start")
        return ConversationHandler.END
    

async def GettingData(update:Update, context:ContextTypes.DEFAULT_TYPE):
    log = update.message.location.latitude
    lat = update.message.location.longitude
    context.user_data['Slat']=lat
    context.user_data['Slot']=log
    tat = int(context.user_data.get('OFFSET'))
    data = SEARCHROOM(lat,log,6,tat)
    if(data[0]==0):
        for i in range(len(data[3])):
            ren = data[3][i][10]
            whc = data[3][i][9]
            lad = data[3][i][7]
            rmt = data[3][i][3]
            inv = data[3][i][4]
            wat = data[3][i][5]
            
            wif = data[3][i][6]
            Pnh = data[3][i][8]
            
            await update.message.reply_html(
'''
Monthly Rent - {}
Room Type -    {}
Address -      {}
WhoCanLive -   {}
Facilities 
Pure Water -   {}
Wifi -         {}
Inverter -     {}
Mobile -       {}
'''.format(ren,rmt,lad,whc,wat,wif,inv,Pnh)
            )
        await update.message.reply_text("All data found /MORE  /EXIT",)
        context.user_data['OFFSET'] = int(context.user_data.get('OFFSET'))+len(data[3])
        return 3
    else:
        await update.message.reply_text("Soory can not show data now. Chech back later. /start")
        return ConversationHandler.END
    

async def AddRoom_location(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("reached add furniture type")
    query = update.callback_query
    await query.answer()
    context.user_data['RoomFurniture']=query.data
    print(query.data)
    await query.edit_message_text(
'''
Share Location of the Property.
''',)
    return 4

async def FinalAdd(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("location function is not geetind data")
    print(update.message.location.longitude)
    context.user_data['longitude']=update.message.location.longitude
    context.user_data['latitude']=update.message.location.latitude
    await update.message.reply_text("Give Your brief local address to find the property.")
    return 6

async def WhoCanLive(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    context.user_data['LocalAddress']=update.message.text
    keyboard = [
                    [InlineKeyboardButton("Girls",callback_data="013")],
                    [InlineKeyboardButton("Boys",callback_data="014")],
                    [InlineKeyboardButton("Any/Family",callback_data="015")],
                    
                ]
    await update.message.reply_text("Who can Rent the Property :",reply_markup=InlineKeyboardMarkup(keyboard))
    return 3

async def AddRoom_rent(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['WhoCanLive']=query.data
    await query.edit_message_text("What is the monthly Rent for the property :")
    return 5
    

async def localAdd(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print("rent of room is",update.message.text)
    a = str(context.user_data.get('RoomType'),)
    b=str(context.user_data.get('RoomWater'),)
    c=str(context.user_data.get('RoomInverter'),)
    d=str(context.user_data.get('RoomWifi'),)
    e=str(context.user_data.get('RoomFurniture'),)
    f=str(context.user_data.get('LocalAddress'),)
    g=str(context.user_data.get('longitude'),)
    h=str(context.user_data.get('latitude'),)
    i=str(context.user_data.get('WhoCanLive'))
    j=update.message.text
    print(a,b,c,d,e)
    if(a == '01'):
        a ='Room'
    if(a=='02'):
        a='Flat'
    if(a=='03'):
        a='Shop/Commercial'
    if(a=='04'):
        a='PG/Hostel'
    if(b=='05'):
        b='Yes'
    if(b=='06'):
        b='No'
    if(c=='07'):
        c='Yes'
    if(c=='08'):
        c='No'
    if(d=='09'):
        d='Yes'
    if(d=='010'):
        d=' No'
    if(e=='011'):
        e='Yes'
    if(e=='012'):
        e='No'
    if(i=='013'):
        i='Girls'
    if(i=='014'):
        i='Boys'
    if(i=='015'):
        i='Any/Family'
        
    
    await update.message.reply_html(
'''
All your Details are :
Property Type - {}
Water - {}
Inverter - {}
Wifi - {}
Furniture - {}
Local Address - {}
Location data - {} | {}
WhocanLive - {}
Monthly Rent - {}
'''.format(a,b,c,d,e,f,g,h,i,j)
    )
    ram = NEWROOM(
            address=g,
            address1=h,
            localaddress=f,
            inverter=c,
            mobile=str(context.user_data.get('PhoneNumber')),
            purewater=b,
            rent=j,
            roomtype=a,
            username=update.message.chat.id,
            whocanlive=i,
            wifi=d,
            )
    print(type(ram))
    if(ram[0]==0):
        await update.message.reply_html(
'''
Your Property has been listed. 
Thank you ,  
Please share this bot to others 
start again /start .
'''
            )
        return ConversationHandler.END
    else:
        await update.message.reply_text("Soory server is busy. Try back later. /start")
        return ConversationHandler.END


async def FindRoom(update:Update, context:ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
'''
Send Location of the nearby area or Cordinates.
You can copy Cordinates form googel map
cordinate format should be like 
25.47858957,81.447745 .
''' 
    )
    return 7
    

# starting main function
offset = 0
def main():
    print("Bot is Online")
    app = Application.builder().token(os.getenv("Token")).build()
    
    Profile_checker = ConversationHandler(entry_points = [CommandHandler("start",Start)],
                                          states= {
                                              1 : [MessageHandler(filters.Regex("^Exit$"),CheckProfile),
                                                  MessageHandler(filters.CONTACT,CheckProfile),
                                                   ],
                                              2: [MessageHandler(filters.TEXT,AskName)],
                                              3:[CallbackQueryHandler(FindRoom,"^find$"),
                                                 CallbackQueryHandler(AddRoom_type,"^addroom$"),
                                                 CommandHandler("MORE",Gettingforcordss),
                                                 CallbackQueryHandler(AddRoom_water,"^01$"),
                                                 CommandHandler("EXIT",ExitAll),
                                                 CallbackQueryHandler(AddRoom_water,"^02$"),
                                                 CallbackQueryHandler(AddRoom_water,"^03$"),
                                                 CallbackQueryHandler(AddRoom_water,"^03$"),
                                                 CallbackQueryHandler(AddRoom_water,"^04$"),
                                                 CallbackQueryHandler(AddRoom_inverter,"^05$"),
                                                 CallbackQueryHandler(AddRoom_inverter,"^06$"),
                                                 CallbackQueryHandler(AddRoom_wifi,"^07$"),
                                                 CallbackQueryHandler(AddRoom_wifi,"^08$"),
                                                 CallbackQueryHandler(AddRoom_furniture,"^09$"),
                                                 CallbackQueryHandler(AddRoom_furniture,"^010$"),
                                                 CallbackQueryHandler(AddRoom_location,"^011$"),
                                                 CallbackQueryHandler(AddRoom_location,"^012$"),
                                                 CallbackQueryHandler(AddRoom_rent,"^013$"),
                                                 CallbackQueryHandler(AddRoom_rent,"^014$"),
                                                 CallbackQueryHandler(AddRoom_rent,"^015$"),
                                                 
                                                ],
                                              6: [MessageHandler(filters.TEXT,WhoCanLive)],
                                              5: [MessageHandler(filters.TEXT,localAdd)],
                                              4: [MessageHandler(filters.LOCATION,FinalAdd)],
                                              7: [MessageHandler(filters.TEXT,GettingDatacords),
                                                  MessageHandler(filters.LOCATION,GettingData)]
                                              
                                              
                                              },
                                          fallbacks= [CommandHandler("start",Start)]
                                          )
    app.add_handler(Profile_checker)
    app.add_handler(MessageHandler(filters.Regex("^Exit$"),ExitAll))
    app.add_handler(CommandHandler("help",Help))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

main()
# main function closed

