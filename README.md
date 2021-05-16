# Fastest-CoWIN-First :syringe: :rocket:
This python script will help you book the slots for the vaccines on CoWIN portal very fast :zap:. It notifies the user as soon as the slots are available for booking.

## Problem Statement:
While India is working very hard to provide every means to vaccinate everyone, still there is a big shortage of doses available to people. Due to high demand and low supplies vaccination slots are filled in a very short time. It's very tiring, frustrating and time consuming to sit in front of your phone or desktop and refresh every now and then to look for the open spots and still we can miss them. It's better to automate this job and let software handle this task. Also, most of the available options for tracking either notify very late or have bugs in them.

## How this script helps:
Script uses a telegram bot to notify you as soon as a slot is available for booking. As you get the notification you can easily login to CoWIN portal and book your slots. Thus saving a lot of time spent on clicking/refreshing the page for the repetitive job. Also, because it's a raw python script, it has the room for modifications.


## Salient Features:
- A good selection of filters, notified only when it's time. :vibration_mode: :heavy_check_mark:
- Takes very less resources in the background, no CPU loading at all. :battery:
- Minimal approach, easy to understand, low latency. :stopwatch:
- Can be modified to integrate with multiple broadcasting channels.(Bots, email, SMS, etc.) :speech_balloon:
- Selectable refresh frequecy, upto 100 API calls in 5 min. (1 in every 3 sec) :repeat:
- Properly formatted data, easy to read. :page_with_curl:
- No repetitive notifications, notifies only on change. :calling:
- Automatic date capture, no need to change dates at midnight, sleep well Tommy. :relieved:


## How to Use:

1. Create a Python virtual environment in a separate directory and activate it.
	* <kbd>python -m venv venv</kbd>
	* <kbd>source venv/bin/activate</kbd>
2. Clone the repo, install all the requirements from requirements.txt
	* <kbd>git clone 'repo-address'</kbd>
	* <kbd>cd Fastest-CoWin-First</kbd> 
	* <kbd>pip install -r requirements.txt</kbd>
3. Download and Install Telegram on your phone/desktop form [here](https://telegram.org/).
4. Create a Telegram bot using BotFather. (Follow the article from references.)
5. Configure your bot on desktop using - 
	* <kbd>telegram-send --configure</kbd>
6. Set the pin-code and filters in the script.
7. Run the script in the background.
	* <kbd>python fastest-covin-first.py</kbd>

## Important Notes:

* In case if error notifications are enabled, the script would notify you only once. Make sure to debug the connection.
* The design of script is such that it notifies/logs only if there is a change compared to previous responses.
* You can switch the Telegram notifications on/off, but terminal logs are always enabled.
* On terminal a num_req variable shows the number of times script tried to hit the API.

## FAQ:

#### Q: Why can't we book slots using the script?
This script only notifies you when there is an empty slot. It does not book slots for you. For booking you have to manually login and select the slot. The booking API is restricted by the government for the official use only. So, it's not possible todo so.

#### Q: How do we use filters properly?
Filters are very easy to understand by reading comments in code. A proper list of usecase will be available soon.

#### Q: How should I set up the bot?
You can follow [this](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580) article for that. It's very easy, given you have a phone and a desktop with a working internet connection.

## References:

- [Medium Article: Configure a Telegram bot using python](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580)
- [Requests module docs](https://pypi.org/project/requests/)
- [telegram-send module docs](https://pypi.org/project/telegram-send/)
- [CoWin API support](https://apisetu.gov.in/public/marketplace/api/cowin)
