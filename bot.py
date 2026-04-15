import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Реакции на "нет"
DISLIKE_EMOJI = "<:Cat_Pain:1486024964359459089>"

# Короткие советы
advice_list = [
    "Иди пить пиво, заслужил",
    "Посмотри аниме, отвлекись",
    "Поспи хотя бы 4 часа",
    "Забей на работу, поиграй в игры",
    "Выйди на улицу, вспомни как ходить",
    "Почитай книгу, если умеешь",
    "Посмотри видео с котиками",
]

# Магический шар
magic_ball = [
    "Да! Без вариантов!",
    "Нет, и не надейся",
    "Возможно... если погода будет хорошая",
    "Определённо да! Спроси завтра",
    "Понятия не имею, но звучит круто",
    "Шансы есть, но маленькие",
    "Спроси после обеда, я устал",
    "100% ДА! Делай немедленно!"
]

@client.event
async def on_ready():
    print(f"✅ miniPomadka23 запущен!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot:
        return
    
    content = message.content.lower()
    
    # Реакции на чужие "нет"
    if content in ["нет", "no", "не", "неа", "нетушки"]:
        await message.add_reaction(DISLIKE_EMOJI)
        return

   if "пластиковые трусы" in content:
        await message.reply("ДА! <:BOSS:1486025422859665510>")
        return
    
    # Команды
    if content.startswith("/dice") or content.startswith("!dice"):
        result = random.randint(1, 20)
        await message.reply(f"Бросаю кубик... {result} из 20!")
        return
    
    if content.startswith("/d6") or content.startswith("!d6"):
        result = random.randint(1, 6)
        await message.reply(f"У тебя выпало - {result}!")
        return
    
    if content.startswith("/coin") or content.startswith("!coin"):
        result = random.choice(["Да!", "Нет!"])
        await message.reply(result)
        return
    
    if content.startswith("/8ball") or content.startswith("!8ball"):
        question = content[6:].strip()
        if not question:
            await message.reply("Напиши вопрос после /8ball, например: /8ball Уволят меня?")
            return
        answer = random.choice(magic_ball)
        await message.reply(f" {answer}")
        return
    
    if content.startswith("/advice") or content.startswith("!advice"):
        advice = random.choice(advice_list)
        await message.reply(f" {advice}")
        return
    
    if content.startswith("/help") or content.startswith("!help") or content.startswith("/?"):
        help_text = """
        **miniPomadka23** - мини помощник и советчик:

        **Важные вопросы**
        `/dice` или `!dice` - Кинуть d20
        `/d6` или `!d6` - Кинуть обычный кубик
        `/coin` или `!coin` - Монетка (да/нет)
        `/advice` или `!advice` - Случайный совет
        
        **Магический шар:**
        `/8ball [вопрос]` или `!8ball` - задай вопрос и получи ответ

     
        """
        await message.reply(help_text)
        return

# МЕСТО ДЛЯ ТОКЕНА, НА ГИТХАБЕ ОСТАВИТЬ ПУСТЫМ, ПОТОМ ЗАМЕНЮ НА СЕРВЕРЕ (в кавычках)
TOKEN = "DISCORD_TOKEN"
client.run(TOKEN)