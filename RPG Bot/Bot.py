# cd /d E:Python/RPG Bot
# python bot.py

from pyquery import PyQuery as pq
import sqlite3
import math
import os
import random
import discord
import Modules.Enemy as Enemy
import Modules.Dungeon as Dungeon
import Modules.Drops as Drop
from dotenv import load_dotenv
from re import search



load_dotenv()
TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
client = discord.Client(intents=intents)
                
                # Jothan               DAWSON                  DREW                REECE
Admins = ["747615592432426821", "419571596366442592", "466027928985296399", "276495567923982336"]

GlobalColor = 0x469F70

prefix = "gr"

def Initialize():
    conn = sqlite3.connect('GrimmRPG.db')
    c = conn.cursor()
    queries = ["""
                CREATE TABLE IF NOT EXISTS inventory (
                  user_Id text,
                  item_Name text,
                  item_Count integer,
                  item_description text,
                  item_emote text,
                  item_type text,
                  item_level integer
                  )
                
            """,
            """
               CREATE TABLE IF NOT EXISTS userdata (
            	"user_id"	TEXT,
            	"user_level"	INTEGER,
            	"user_gold"	INTEGER,
            	"user_dungeon"	TEXT,
            	"user_progress"	INTEGER
                )
                
                """]

    for query in queries:
        c.execute(query)

    
    conn.close()
    

def GetRawID(UserPing):
    # FirstPass = UserPing.split('!')
    # SecondPass = FirstPass[1].split('>')
    # ID = str(SecondPass[0])
    
    ID = search("\d+", UserPing).group()
    
    return ID
           
def GetData(UserID, Item, Table = "inventory"):
    
    # Create database or connect to one
    conn = sqlite3.connect('GrimmRPG.db')
    
    #Create Cursor
    c = conn.cursor()
    
    if Item.lower() == "all":
        c.execute("SELECT * FROM " + Table + " WHERE user_Id = ?1", (UserID, ))
        results = c.fetchall()
    else:
        c.execute("SELECT * FROM " + Table + " WHERE user_Id = ?1 AND item_name = ?2", (UserID, Item))
        results = c.fetchall()
        
    conn.close()

    return results

def SetData(UserID, Item, Data, Description = "", Emote = "", Type = "", Level = 0):
    
    # Retrieve User Inventory Data
    Inventory = GetData(UserID, "All")
    
    # Create database or connect to one
    conn = sqlite3.connect('GrimmRPG.db')
    
    #Create Cursor
    c = conn.cursor()

    
    #Check if item exists in inventory
    
    
    itemExists = False
    
    for table in Inventory:
        if Item in table:
            itemExists = True
    
    if not itemExists:
        c.execute("INSERT INTO inventory VALUES (:user_Id, :item_Name, :item_Count, :item_description, :item_emote, :item_type, :item_level)",
                  {
                      "user_Id": UserID,
                      "item_Name": Item,
                      "item_Count": Data,
                      "item_description": Description,
                      "item_emote": Emote,
                      "item_type": Type,
                      "item_level": Level
                      
                      
                      })
    
    c.execute("UPDATE inventory SET item_Count = ?1 WHERE item_Name = ?2 AND user_Id = ?3",(Data, Item, UserID))
    c.execute("DELETE FROM inventory WHERE item_count=0")
    
    
    conn.commit()
    
    conn.close()

def GeneratePages(Table, ItemsPerPage):
    Pages = math.ceil(len(Table)/ItemsPerPage)
    
    NewTable = []
    
    for page in range(Pages):
        
        Item = 0
        NewPage = []
        
        while Item < ItemsPerPage and len(Table) > 0:
            NewPage.append(Table[0])
            del Table[0]
            Item += 1
            
        NewTable.append(NewPage)
    
    return NewTable


def WhatIs(Item=""):
    Punctuation = [ '.', '?', '!', '\n' ]
    
    d = pq(url="https://en.wikipedia.org/wiki/"+str(Item.lower()))
    p = d('p')
    
    p = p.text()
    
    text = ""
    
    for i in p:
        if i in Punctuation:
            text += i
            return text
        else:
            text += i
    
    p = d('ul')
    p = p.text()
    text = ""
 
    for i in p:
        if i in Punctuation:
            text += i
            return text
        else:
            text += i
    return "Nothing found"

@client.event
async def on_ready():
    stream_url = "https://www.twitch.tv/lofi_lyf"
    await client.change_presence(activity=discord.Streaming(name="gr help", url=stream_url))
    
@client.event    
async def on_message(message):
    
    if message.author == client.user:
        return

    Command = message.content.split(' ')
    
    
    if Command[0] == prefix.lower():
        
        if message.channel.type is discord.ChannelType.private:
        
            embed=discord.Embed(title="Grimm DM's", url="", description="Hello " + "<@!"+str(message.author.id)+">, \nI regret to inform you that the bot cannot be used in DM's at this time.", color=0x00FF00)
            await message.channel.send(embed=embed)
            return        
        
        # if Command[1] == ".":
        #     for i in range (15):
        #         await message.channel.send("<@!678669973434138645>")
        
        if Command[1] == "help":
            embed=discord.Embed(title="Grimm Help", url="", description="Grimm is still working on the bot " + "<@!"+str(message.author.id)+">", color=0xFF5733)
            await message.channel.send(embed=embed)
            
        elif Command[1] == "inventory" or Command[1] == "inv":
        
            
            
            
            Inventory = GetData(str(message.author.id), "All")
            Inventory = GeneratePages(Inventory, 5)
            
            GoldCount = GetData(str(message.author.id), "user_gold")
            Text = "**Your Loot**\n\n"
        
            # Get page number input and check if it is valid
            try:
                if int(Command[2]) > 0:
                    Page = int(Command[2])
                else:
                    Page = 1
            except:
                Page = 1 
            
            if Page > len(Inventory) or Page < 1:
                Page = 1
                
                
            # Print current active page.
            for item in Inventory[Page-1]:
                Text += item[4] + " " + item[1] + "**-**" + str(item[2]) + "\n" + item[3] + "\n\n" # 0 = AuthorID, 1 = ItemName, 2 = ItemCount, 3 = Description, 4 = Emote
            Auth = str(message.author).split('#')
            embed=discord.Embed(title=str(Auth[0]) + "'s Inventory", url="", description=Text, color=0xFF5733)
            embed.set_footer(text="\nPage " + str(Page) + " of "+str(len(Inventory)))
            await message.channel.send(embed=embed)

        elif Command[1] == "dungeon":
            pass
        
        elif Command[1] == "whatis":
            text = WhatIs(Command[2])
            embed=discord.Embed(title=Command[2], url="https://en.wikipedia.org/wiki/"+Command[2], description=text, color=0x16A112)
            await message.channel.send(embed=embed)
        
        elif str(message.author.id) in Admins:
                
            if Command[1] == "id":
                
                await message.channel.send(GetRawID(Command[2]))
            
            elif Command[1] == "ahelp":
                
                Text = """
                :tools:
                    
                **gr invedit |UserTag|ItemName|SetAmount|Description|Emote|ItemType|Level|** 
                *- Edits a users inventory data*
                
                :basketball: 
                    
                **gr dm UserTag MessageCount | MessageText**
                *- DM's a message to a user a set amount of times*
                
                **gr say MessageCount | MessageText**
                *-Spams a message in current channel a set amount of times*
                
                
                
                """
                
                Member = client.get_user(message.author.id)
                await message.channel.send("Those top secret admin commands have been sent to your DM's!")
                
                embed=discord.Embed(title="Admin Commands", url="", description=Text, color=0xccfffe)
                
                await Member.send(embed=embed)
            
            elif Command[1] == "invedit":
                Argument = message.content.split('|')
                print(Argument)
                SetData(GetRawID(Argument[1]), Argument[2], int(Argument[3]), Argument[4], Argument[5], Argument[6], int(Argument[7]))
                await message.channel.send("Edited " + Argument[1] + " " + Argument[2])
                
            elif Command[1] == "say":
                
                CMD = message.content.split('|')
                
                try:
                    
                    if int(Command[2]) > 25:
                       Command[3] = 25
                    
                    for i in range(int(Command[2])):
                        embed=discord.Embed(title="", url="", description=CMD[1], color=GlobalColor)
                        await message.channel.send(embed=embed)
                except Exception as e:
                    print(e)
                    await message.channel.send("Please double check your command for out of place or missing spaces!```py\n"+message.content+"\n```")  
                    
            elif Command[1] == "dm":
               CMD = message.content.split('|')
               member = client.get_user(int(GetRawID(Command[2])))
               
               await message.channel.send("Attempting...")
               
               try:
                   
                   if int(Command[3]) > 25:
                       Command[3] = 25
                       
                   for i in range(int(Command[3])):
                        embed=discord.Embed(title="", url="", description=CMD[1], color=GlobalColor)
                        await member.send(embed=embed)
                        
                   await message.channel.send("Action successful!")
                   
               except Exception as e:
                 print(e)
                 await message.channel.send("Please double check your command for out of place or missing spaces!```py\n"+message.content+"\n```")  

Initialize()
client.run(TOKEN)

