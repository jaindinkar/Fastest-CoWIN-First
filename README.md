# Fastest-CoWIN-First
This python script will help you book the slots for the vaccines on CoWIN portal very fast. It notifies the user as soon as the slots are available for booking.

## Problem Statement:
While India is working very hard to provide every means to vaccinate everyone, still there is a big shortage of doses available to people. Due to high demand and low supplies vaccination slots are filled in a very short time. It's very tiring, frustrating and time consuming to sit in front of your phone or desktop and refresh every now and then to look for the open spots and still we can miss them. It's better to automate this job and let software handle this task.

## How this script helps:
Script uses a telegram bot to notify you as soon as a slot is available for booking. As soon as you get the notification you can easily login to CoWIN portal and book your slots. Thus saving a lot of time spent on clicking/refreshing the page for the repetitive job.


## Salient Features:
- A good selection of filters, notified only when it's time.
- Takes very less resources in the background, no CPU loading at all.
- Minimal approach, easy to understand, low latency.
- Can be modified to integrate with multiple broadcasting channels.(Bots, messaging queues, email-reminders)
- Selectable refresh frequecy, upto 100 API calls in 5 min.
- Beautifully formatted data, easy to read.


## How to Use:

-> Download and Install Telegram on your phone/desktop.
-> Install BotFather and create a new bot. (Follow the article.)
-> Create a Python virtual environment in a separate directory.
-> Clone the repo, install all the requirements from requirements.txt
-> Configure your bot on desktop using telegram-send --configure.
-> Set the Appropriate filters in the script.
-> Run the script in the background.



##FAQ:

Q: Why can't we book slots using the script?
This script only notifies you when there is an empty slot. It does not book slots for you. For booking you have to manually login and select the slot. The booking API is restricted by the government for the official use only. So, it's not possible now to do so.

Q: How do we use filters properly?
Filters are very easy to understand by reading comments in code. A proper list of usecase will be available soon.

Q: How should I set up the bot?
You can follow this article for that. It's very easy, given you have a phone or desktop. :smile:

## References:

-> Medium Article on how to configure BotFather.
-> Requests module docs.
-> telegram-send module docs.
-> CoWin API support.
