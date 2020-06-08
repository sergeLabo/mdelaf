#! /usr/bin/env python3


from time import sleep
import threading
from mdelaf_irc import MDeLafIrcBot
from mdelaf_gen import generate
from textgenrnn import textgenrnn

# Serveur IRC
SERVER = "irc.freenode.net"
PORT = 6667
CHANNEL = "#labomedia"
NICKNAME = "MDeLaf"
REALNAME = "Monsieur Jean De La Fontaine"


def run():

    bot = MDeLafIrcBot(CHANNEL, NICKNAME, REALNAME, SERVER, PORT)
    thread_dialog = threading.Thread(target=bot.start)
    thread_dialog.setDaemon(True)
    thread_dialog.start()

    textgen = textgenrnn('textgenrnn_weights.hdf5')

    sleep(1)
    while bot.alive:
        a = 0
        num = bot.num
        if bot.quest_rep:
            if len(bot.quest_rep) == num + 1:
                if len(bot.quest_rep[num]) == 1:
                    a = 1
                    question = bot.quest_rep[num][0]

        if a == 1:
            try:
                text = generate(textgen)
            except:
                text = "Je ne comprends pas la question!"

            # Envoi de la réponse
            print("\nQuestion n°:", num)
            print("Question:", bot.quest_rep[num])
            print("Response:", text)
            bot.quest_rep[num].append(text)


if __name__ == '__main__':

    run()
