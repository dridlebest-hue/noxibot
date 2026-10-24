import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import json
from typing import Optional
from discord import app_commands
from discord.ui import Button, View
from keep_alive import keep_alive




load_dotenv()



bot = commands.Bot(command_prefix="/",intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("hello world :DDDDDDDD")
      
    try:
       
       synced = await bot.tree.sync()
       print(f"syncro: {len(synced)}")

    except Exception as e :
         print("e")
@bot.tree.command(name="init-recrutements", description="none")
async def info(interaction:discord.interactions):
    class alliés(discord.ui.Modal, title="faction alliée"):
            age= discord.ui.TextInput(
            label="de quelle faction vient tu ?",
            placeholder="ex:noxira"
        )
            async def on_submit(self, interaction: discord.Interaction):
                         buttonalliesyes=Button(label='accepter en tant que diplomate ', style=discord.ButtonStyle.green)
                         buttonalliesno=Button(label='refusé car faction non alliée', style=discord.ButtonStyle.red)
                        
                         
                         fac=self.age
                         member= interaction.user
                         logs_channel=bot.get_channel(1561425314784088124)
                         embed_logs= discord.Embed(
                                 title= "un membre a demander a s'enregistrer en tan qui diplomate",
                                 description= f"le membre {interaction.user.display_name} souhaite devenir un diplomate pour la faction {fac}",
                                 color= discord.Color.dark_blue())
                         
                         await interaction.response.send_message("ta demande de devenir diplomate été envoyée",ephemeral=True)
                         async def buttonalliesyes_callback(interaction):
                               diplo_id=1553801244026343505
                               role= interaction.user.guild.get_role(diplo_id)
                               await member.send("ta demande de devenir diplomate été acceptée" )
                               await interaction.response.send_message("accepté",ephemeral=True)
                               await member.add_roles(role)
                         async def buttonalliesno_callback(interaction):
                                    ob_id= 1563201611319353384
                                    role= interaction.user.guild.get_role(ob_id)                    
                                    await member.send("ta demande de devenir diplomate été refusée ta faction n'est notre alliée")
                                    await interaction.response.send_message("refusé",ephemeral=True)
                                    await member.add_roles(role)
                                                        
                         buttonalliesyes.callback= buttonalliesyes_callback
                         buttonalliesno.callback= buttonalliesno_callback
                         view2=View()
                         view2.add_item(buttonalliesyes)
                         view2.add_item(buttonalliesno)
                         
                         await logs_channel.send(embed=embed_logs,view=view2)
    
    class Recrutement(discord.ui.Modal, title="Recrutement"):
        age= discord.ui.TextInput(
        label=" ton age",
        placeholder="ex:16ans"
    )
        qualités= discord.ui.TextInput(
                label=" quelles sont tes qualités",
                placeholder="ex:gentil"
            )
        defauts= discord.ui.TextInput(
                        label=" quelles sont tes défauts",
                        placeholder="ex:méchant"
                    )
        pseudo = discord.ui.TextInput(
        label='pseudo minecraft',
        placeholder='ex:stevedu411',
    )
       
                    
        roles= discord.ui.TextInput(
                                        label="quel role veut tu avoir dans la fac",
                                        placeholder="ex:builder"
                                    )
                
        
        async def on_submit(self, interaction: discord.Interaction):
                 buttonaccept=Button(label='accepté', style=discord.ButtonStyle.green)
                 buttonticket=Button(label='ouvrir un ticket', style=discord.ButtonStyle.gray)
                 buttonrefuse=Button(label='refusé', style=discord.ButtonStyle.red)

                 qua = self.qualités
                 old=self.age
                 defau=self.defauts
                 
                 rol=self.roles
                 
                 psu=self.pseudo
                 member=interaction.user.display_name
                 member_mention=interaction.user.id
                 logs_channel=bot.get_channel(1561425314784088124)
                 embed_logs= discord.Embed(
                         title= 'un membre veut se faire recruter',
                         description= f"le membre {member }souhaite se faire recruter",
                         color= discord.Color.dark_blue())
                 embed_logs.add_field(name="qualités",value=qua)
                 embed_logs.add_field(name="défauts",value=defau)
                 embed_logs.add_field(name="age",value=old)
                 
                 embed_logs.add_field(name="pseudo ig",value=psu)
                 embed_logs.add_field(name="roles que le membre veut avoir",value=rol)
                 await interaction.response.send_message("ta candidature a été déposée un staff est suceptible d'ouvrir un salon avec toi pour avoir plus d'information",ephemeral=True)
                 async def ticket_callback(interaction):
                    GUILD = bot.get_guild(1553096848179470518)
                    mm=bot.get_user(member_mention)
                    await interaction.response.send_message('ticket ouvert',ephemeral=True)
                    
                    overwrites = { GUILD.default_role: discord.PermissionOverwrite(view_channel=False)}

                    channel =  await GUILD.create_text_channel(f'recrutement de {member}',overwrites=overwrites)
                    await channel.send(f"ouverture du salon de recrutement <@{interaction.user.id}> <@{member_mention}>")
                    perms = channel.overwrites_for(mm)
                    perms.send_messages = True
                    perms.view_channel =True
                    await channel.set_permissions(mm, overwrite=perms)


                 buttonticket.callback=ticket_callback
                 async def refuse_callback(interaction):
                       
                       mm=bot.get_user(member_mention)
                                         
                       await mm.send("ta demande d'etre un de nos membres a été refusée")
                       await interaction.response.send_message("refusé",ephemeral=True)
                       
                 async def accept_callback(interaction):
                                        
                                        mm=bot.get_user(member_mention)
                                                          
                                        await mm.send("ta demande de devenir un de nos membres a été acceptée")
                                        await interaction.response.send_message("accepté",ephemeral=True)
                                        
                       
                 buttonaccept.callback= accept_callback
                 buttonrefuse.callback=refuse_callback
                 view3=View()
                 view3.add_item(buttonaccept)
                 view3.add_item(buttonrefuse)
                 view3.add_item(buttonticket)
                 await logs_channel.send(embed=embed_logs,view=view3)
                 
        

    buttonjoin = Button(label='recrutement', style=discord.ButtonStyle.primary)
    buttonallies = Button(label='allié', style=discord.ButtonStyle.green)
    buttonnormal = Button(label='observateur ', style=discord.ButtonStyle.gray)
    embed= discord.Embed(
        title= 'pourquoi est tu venu ici ?',
        description= "si tu es venu faire partie de la fac cliques sur le bouton bleu,si tu viens d'une autre faction cliques sur le bouton vert,si tu es juste venu ici pour regarder l'évolution de la fac cliques sur le bouton gris",
        color= discord.Color.dark_blue())
    view=View()
    view.add_item(buttonjoin)
    view.add_item(buttonallies)
    view.add_item(buttonnormal)
    async def buttonjoin_callback(interaction):
        await interaction.response.send_modal(Recrutement())
        
    async def buttonallies_callback(interaction):
        await interaction.response.send_modal(alliés())
        
           
        
    async def buttonnormal_callback(interaction):
            user=interaction.user
            
            ob_id= 1563201611319353384
            role = user.guild.get_role(ob_id)
            await user.add_roles(role)
            await interaction.response.send_message("tu as bien été enregistré en tant que visiteur",ephemeral=True)
            
    buttonnormal.callback = buttonnormal_callback
    buttonallies.callback =buttonallies_callback
    buttonjoin.callback = buttonjoin_callback

    await interaction.response.send_message(embed=embed,view=view)
keep_alive()
bot.run(os.getenv('DISCORD_TOKEN'))