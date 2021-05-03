import pyautogui as pt
from time import sleep
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from emoji import emojize
import pyperclip
import random
import conv
from conv import *


mybot=ChatBot(name="Logan's Chat Assistant",read_only=False,logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.BestMatch'])

#dataset1=open('dialogs.txt').read().strip().split('\n')
#dataset2=open('aboutme.txt').read().strip().split('\n')

list_trainer=ListTrainer(mybot)
for item in (small_talk,google):
    list_trainer.train(item)

#corpus_trainer=ChatterBotCorpusTrainer(mybot)
#corpus_trainer.train('chatterbot.corpus.english')

def get_message():
    global x,y
    position=pt.locateOnScreen("smiley_clip.png",confidence=0.60)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y,duration=.1)
    pt.moveTo(x+82,y-57,duration=.1)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,-120)
    pt.click()
    message=pyperclip.paste()
    print("message received: "+message)

    return message

def post_response(message):
    global x,y
    position=pt.locateOnScreen("smiley_clip.png",confidence=0.60)
    x=position[0]
    y=position[1]
    pt.moveTo(x+200,y+20,duration=.1)
    pt.click()
    pt.typewrite(message,interval=.01)
    pt.typewrite("\n",interval=.01)

def process_response(message):
    msg=mybot.get_response(message)
    sleep(0.5)
    return str(msg.text)

def check_new_msg():
    while True:
        """try:
            position=pt.locateOnScreen("unread.png",confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-30,0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No new msg")"""

        position1=pt.locateOnScreen("smiley_clip.png",confidence=0.60)
        x=position1[0]
        y=position1[1]
        pt.moveTo(x+80,y-53,duration=.1)

        if pt.pixelMatchesColor(int(x+80),int(y-53),(255,255,255),tolerance=10):
            print("is_white")
            processed_msg=process_response(get_message())
            post_response(processed_msg)
        else:
            print("no new msgs yet..")
            sleep(1)

check_new_msg()








