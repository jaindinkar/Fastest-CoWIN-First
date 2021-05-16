# \\********************************************//
#    About Section: Fastest-CoWIN-First
#    Author: Dinkar Jain
#    E-mail: jain.dinkar675@gmail.com
#    Start: 15-05-2021
#    Motto: Notified only when it's time.
# \\********************************************//

import time
import requests
import telegram_send
from datetime import date


class Slot:
    def __init__(self, address, date, minAge, vaccType, feeType, avlCapacity):
        self.address = address
        self.date = date
        self.minAge = minAge
        self.vaccType = vaccType
        self.feeType = feeType
        self.avlCapacity = avlCapacity


# ----------------Filter selection.--------------------
pinCode = '301001'                 # Change to your city's pincode.
# All options below are good as a default. Change according to need.
for18Plus = True                   # Select for slots 18+ citizens only.(Can select both options)
for45Plus = False                  # Select slots for 45+ citizens only.
includePaid = False                # Include slots where vaccination in paid.
vaccineType = ['ALL']              # Default ALL; Slection 'COVISHIELD', 'COVAXIN', 'SPUTNIK-V'
includeOccupiedSlots = True        # Include slots which have no vaccine available(for initial datacheck)
enableNotification = True          # Enable or disable Telegram notifications.(Configure the bot first to avoid unnecessary errors.)
enableErrorNotification = False    # Enable or disable Telegram error notifiactions. (Optional, for debugging only.)
refreshInterval = 5                # in Seconds (minimum = 3, recommended = 10. Below minimum you will be banned from servers)
# -----------------------------------------------------


if for18Plus and for45Plus:
    minAgeLimit = [18, 45]
elif for18Plus:
    minAgeLimit = [18]
elif for45Plus:
    minAgeLimit = [45]
else:
    print('Select at least one age group.')


if includePaid:
    feeType = ['Free', 'Paid']
else:
    feeType = ['Free']


if vaccineType[0] == 'ALL':
    vaccine = ['COVISHIELD', 'COVAXIN', 'SPUTNIK-V']
else:
    vaccine = vaccineType


if includeOccupiedSlots:
    min_cap = 0
else:
    min_cap = 1


url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"
headers = {'user-agent': 'my-app/0.0.1'}

request_num = 0

last_text = ''

while True:

    print(f'----------------- num_req: {request_num} ------------------')

    date_today = date.today().strftime("%d-%m-%Y")
    payload = {'pincode': pinCode, 'date': date_today}

    r = requests.get(url, params=payload, headers=headers)

    avl_slot_list = []


    if r.status_code == requests.codes.ok :

        response = r.json()
        
        center_details_list = (response["centers"])
        
        for obj in center_details_list:
            for session in obj['sessions']:
                if session['available_capacity'] >= min_cap:
                    if session['min_age_limit'] in minAgeLimit:
                        if obj['fee_type'] in feeType:
                            if session['vaccine'] in vaccine:
                                add_str = obj['name'] + ", " + obj['address']
                                avl_slot_list.append(Slot(
                                    address=add_str, 
                                    date=session['date'], 
                                    minAge=session['min_age_limit'], 
                                    vaccType=session['vaccine'], 
                                    feeType=obj['fee_type'], 
                                    avlCapacity=session['available_capacity']
                                ))

        message_text = ''
        for i in range(len(avl_slot_list)):
            print(
                
                f'{i+1}) {avl_slot_list[i].address}\n'\
                f'Date: {avl_slot_list[i].date}\n' \
                f'Available Capacity: {avl_slot_list[i].avlCapacity}\n'\
                f'Fee Type: {avl_slot_list[i].feeType}\n'\
                f'Age Group: {avl_slot_list[i].minAge}+\n\n'
            )
            message_text += f'{i+1}) {avl_slot_list[i].address}\n'\
                            f'Date: {avl_slot_list[i].date}\n' \
                            f'Available Capacity: {avl_slot_list[i].avlCapacity}\n'\
                            f'Fee Type: {avl_slot_list[i].feeType}\n'\
                            f'Age Group: {avl_slot_list[i].minAge}+\n\n'
        
        if avl_slot_list:
            if enableNotification:
                if last_text != message_text:
                    telegram_send.send(messages=[message_text])
                    last_text = message_text
        else:
            print("No open slots for given filter. Wait untill notification arrives.")

    else:
        print("Request Failed!!")
        print(r.status_code)
        if enableErrorNotification:
            telegram_send.send(messages=[r.status_code, r.text])

    time.sleep(refreshInterval)
    request_num += 1
