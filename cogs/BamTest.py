# The invisible bot's emotion.

# 0.3. Too messy. Will use double array next time. Still running 0.2.

# Author: James Emerson (An Vo)

import discord  # import discord files?
import random  # to generate random numbers
from discord.ext import commands  # import commands from it?

# from redis import Redis, RedisError # maybe not

# =============================================================================
# Base decision tree
# =============================================================================


class BamboozledTest:
    """ 0.3 Expand the emotional spectrum (maybe will use union)
        -   1 - 10 = ANGER
            + 1. HURT
            + 2. THREATENED
            + 3. HATEFUL
            + 4. MAD
            + 5. AGGRESSIVE
            + 6. FRUSTRATED
            + 7. DISTANT
            + 8. CRITICAL        
        -   11 - 20 = FEAR
        -   21 - 30 = HAPPY         JOYFUL + POWERFUL + PEACEFUL
        -   31 - 40 = SURPRISE
        -   41 - 50 = DISGUST
        -   51 - 60 = SAD       


        Avoid using: N/A
        Arguments: N/A
        
        0.2 Greeting accordance to 6 basic moods
        -   1 = MAD
        -   2 = SCARED
        -   3 = JOYFUL
        -   4 = POWERFUL
        -   5 = PEACEFUL
        -   6 = SAD
        0.1. class Lamb will now prompt a user greeting for now        
    """

    def __init__(self,
                 bot):  # view:python3 is good, view: python is bad for sublime
        self.bot = bot

    # =============================================================================
    # Types and constants
    # =============================================================================

    """
    # 0.3.
    greeting = [
                    "(╯°□°)╯︵ ┻━┻ GTFO",                                                # 1
                    "༼;´༎ຶ ۝ ༎ຶ༽ *gasp",                                                 # 2
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ OH YEAH, MY DUDE!!!!!",          # 3
                    "<:pikachu:512132390920126474> （・□・；）(」゜ロ゜)」 Σ(゜ロ゜;)"             # 4
                    " щ(゜ロ゜щ) ┌╏ º □ º ╏┐ NAN-TAH-NOH?（○□○）∴(O艸O★)", 
                    "uhhhhhhh -(≖д≖﹆)"                                ,                # 5
                    "\"( _ _ \")\" oh....kay"                                             # 6
                ]
    old greeting

    """
    # 0.2.
    uwu_greeting = [
                    "(╯°□°)╯︵ ┻━┻ WHO WOKE ME UP!!!???", 
                    "༼;´༎ຶ ۝ ༎ຶ༽ I WUV YOU WHOA~~~~~~~",
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ HOWDY, MY DUDE!!!!!",
                    "( ︶︿︶)_╭∩╮", 
                    "| (• ◡•)| (❍ᴥ❍ʋ ) what's up, mah homie!!??",
                    "\"( Ó_Ò \")\" h...hi......."
                ]

    uwu_mood = [
                    "(╯°□°)╯︵ ┻━┻ GTFO", 
                    "༼;´༎ຶ ۝ ༎ຶ༽ *gasp",
                    "\m/...(>.<)…\m/ └[∵┌]└[ ∵ ]┘[┐∵]┘ OH YEAH, MY DUDE!!!!!",
                    "( ︶︿︶)_╭∩╮ <:pikachu:512132390920126474>", 
                    "| (• ◡•)| (❍ᴥ❍ʋ ) darn right, mah homie!",
                    "\"( Ó_Ò \")\" oh....kay"
                ]
    # =============================================================================

    # =============================================================================
    # Trigger commands
    # =============================================================================    
    bot = commands.bot(command_prefix="sure ")
    # =============================================================================    


    async def on_message(self, message):
        """Defines bot behavior when a message is posted to channel"""

        activate_emoji = "<:thonking:455992031752355870> "
        if message.content.startswith(activate_emoji):
            # convert the result to bot class => ctx = bot.context
            ctx = await self.bot.get_context(message)

            # make sure others can use more than 1 emoji without triggering uwu
            #   repeat_count = 0
            #for index in xrange(1,10):
            #    if ctx[index] == <:thonking:455992031752355870>:
            #        repeat_count++; 
            
            mood = random.randint(1, 6)               # generate a random mood like
                                                      # my cousin's wife
            await ctx.send(self.uwu_mood[mood-1])     # we can use ctx.send

    @commands.command()
    async def ciao(self, ctx):
        """ 0.2. Greeting accordance to mood
            0.1. Saying "hello"
        """


        mood = random.randint(1, 6)
        await ctx.send(self.uwu_greeting[mood - 1])  # array max index is n -1

    @commands.command()
    async def sure(self, ctx, *args):
        """ 0.1. Spongebod Bob mocking tone

            Argument: message
        """
        """
        mocking = message
        mocking = mocking.lower()
        for index in mocking:
            mocking[index] = mocking[index].upper()
        """
        """
        activate_line = "sure "
        mocking = message
        if message.content.startswith(activate_line):
            ctx = await self.bot.get_context(message)
            await ctx.send(mocking)
        """
        await ctx.send(args)

# Sets up the cog
def setup(bot):
    bot.add_cog(BamboozledTest(bot))
