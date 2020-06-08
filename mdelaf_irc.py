
#! /usr/bin/env python3


"""
It also responds to DCC CHAT invitations and echos data sent in such
sessions.
    dcc -- Let the bot invite you to a DCC CHAT connection.
"""

from time import time, sleep

import irc.bot
import irc.strings

from some_response import i_am


class MDeLafIrcBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, realname, server, port=6667):
        super().__init__([(server, port)], nickname, realname)
        self.channel = channel
        self.question = ""
        self.response = "I'm stupid"
        # #self.response_old = "Je suis un bug à la 1ère question"
        # #self.t_block = time()
        self.num = 0
        self.quest_rep = {}
        self.alive = 1

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")
        print("on_nicknameinuse")

    def on_welcome(self, c, e):
        c.join(self.channel)
        print("Welcome on #labomedia IRC")

    def on_pubmsg(self, c, e):

        # a est le messge reçu
        msg = e.arguments[0].split(":", 1)

        i_am = irc.strings.lower(self.connection.get_nickname())
        # Si le message commence par "TheGeneral: "
        if len(msg) > 1 and irc.strings.lower(msg[0]) == i_am:
            # La commande est la suite de "TheGeneral: texte_du_message
            self.do_command(e, msg[1].strip())

    def do_command(self, e, cmd):

        if "die" in cmd:
            self.alive = 0
            sleep(1)
            self.die()
        elif "qui es tu" in cmd or "qui es-tu" in cmd:
            self.send_pubmsg(["Qui suis-je ?", i_am])
        else:
            self.question = cmd.lower()
            self.quest_rep[self.num] = [self.question]
            while len(self.quest_rep[self.num]) == 1:
                sleep(0.01)
            if len(self.quest_rep[self.num]) == 2:
                msg = [self.quest_rep[self.num][0],
                        self.quest_rep[self.num][1]]
                self.send_pubmsg(msg)
                self.num += 1

    def send_pubmsg(self, msg):
        if msg[1] == "i_am":
            self.connection.privmsg("#labomedia", i_am_1)
            sleep(0.3)
            self.connection.privmsg("#labomedia", i_am_2)
            sleep(0.3)
            self.connection.privmsg("#labomedia", i_am_3)
        else:
            self.connection.privmsg("#labomedia", "Q: " + msg[0])
            sleep(0.1)
            self.connection.privmsg("#labomedia", "R: " + msg[1])


def mdelaf_irc_bot_main():

    server = "irc.freenode.net"
    port = 6667
    channel = "#labomedia"
    nickname = "MDeLaf"
    realname = "Monsieur Jean De La Fontaine"

    bot = MDeLafIrcBot(channel, nickname, realname, server, port)
    bot.start()




if __name__ == "__main__":
    mdelaf_irc_bot_main()
