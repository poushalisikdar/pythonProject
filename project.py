

import tkinter as tk
from tkinter import messagebox
import time
import datetime
import random
list1=["If people knew how hard I worked to get my mastery, it wouldn't seem so wonderful after all. — Michelangelo",
"Do the best you can until you know better. Then when you know better, do better. — Maya Angelou",
"Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do. — Pele",
"I do not know anyone who has got to the top without hard work. That is the recipe. It will not always get you to the top, but should get you pretty near. — Margaret Thatcher",
"Hard work spotlights the character of people: some turn up their sleeves, some turn up their noses, and some don’t turn up at all.— Sam Ewing",
"The only thing standing between you and outrageous success is continuous progress you need discipline. — Dan Waldschmidt",
"Talent is cheaper than table salt. What separates the talented individual from the successful one is a lot of hard work.— Stephen King",
"Hard work is a prison sentence only if it does not have meaning. Once it does, it becomes the kind of thing that makes you grab your wife around the waist and dance a jig. — Malcolm Gladwell",
"The fight is won or lost far away from witnesses — behind the lines, in the gym, and out there on the road, long before I dance under those lights. — Muhammad Ali",
"Most of the important things in the world have been accomplished by people who have kept on trying when there seemed to be no hope at all. — Dale Carnegie",
"The only place where success comes before work is in the dictionary. — Vince Lombardi",
"There are no secrets to success. It is the result of preparation, hard work, and learning from failure. — Colin Powell",
"Strive not to be a success, but rather to be of value. — Albert Einstein",
"Try not to become a man of success. Rather become a man of value. ― Albert instein",
"Success is stumbling from failure to failure with no loss of enthusiasm. ― Winston S. Churchill",
"Don't spend time beating on a wall, hoping to transform it into a door.  ― Coco Chanel",
"If A is a success in life, then A equals x plus y plus z. Work is x; y is play; and z is keeping your mouth shut ― Albert Einstein",
"It is hard to fail, but it is worse never to have tried to succeed. ― Theodore Roosevelt",
"If you want to live a happy life, tie it to a goal, not to people or things.― Albert Einstein",
"It is our attitude at the beginning of a difficult task which, more than anything else, will affect its successful outcome. – William James",
"Success depends upon previous preparation, and without such preparation, there is sure to be failure. — Confucius",
"Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. – Thomas A. Edison",
"It is better to fail in originality than to succeed in imitation.  Herman Melville",
"In most things success depends on knowing how long it takes to succeed.  Montesquieu",
"I don’t believe in failure. It’s not failure if you enjoyed the process. Oprah Winfrey",
"Success is not how high you have climbed, but how you make a positive difference to the world. ― Roy T. Bennett, The Light in the Heart",
"The worst part of success is trying to find someone who is happy for you. ― Bette Midler",
"I'm a success today because I had a friend who believed in me and I didn't have the heart to let him down. ― Abraham Lincoln",
"However difficult life may seem, there is always something you can do and succeed at. — Stephen Hawking",
"Today a reader. Tomorrow a leader. – Anonymous",
"He who asks a question is a fool for five minutes; he who does not ask a question remains a fool forever. — Chinese Proverb"]


try:

    def send_notification(title):
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        message=random.choice(list1)

        messagebox.showinfo(title, message)
        

        root.destroy()  # Destroy the root window after displaying the notification

except Exception as e:
    print("Error",e)       


if __name__ == "__main__":
    while True:
        t = datetime.datetime.now()
        current_time = t.hour

        if 4 <= current_time < 12:
            send_notification("🌷🌷Good Morning POUSHALI !!🌷🌷")

        elif 12 <= current_time < 17:
            send_notification("💕Good Afternoon POUSHALI !!💕")

        elif 17 <= current_time < 21:
            send_notification("💫💫Good Evening POUSHALI !!💫💫" )

        else:
            send_notification("🍁🌚Good Night POUSHALI !!🌚🍁")

        # Calculate remaining time until the next hour
        remaining_seconds = 3600 - (t.minute * 60 + t.second)
        time.sleep(remaining_seconds )





       