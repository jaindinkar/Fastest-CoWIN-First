import time
import requests
import telegram_send
from pprint import pprint

class Slot:
    def __init__(self, address, date, minAge, vaccType, feeType, avlCapacity):
        self.address = address
        self.date = date
        self.minAge = minAge
        self.vaccType = vaccType
        self.feeType = feeType
        self.avlCapacity = avlCapacity



# ----------------Filter selection.--------------------
for18Plus = True
for45Plus = False
includePaid = False
vaccineType = ['ALL'] # Add 'COVISHIELD', 'COVAXIN', 'SPUTNIK-V'
# -----------------------------------------------------


if for18Plus && for45Plus:
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


if vaccineType[0] = 'ALL':
    vaccine = ['COVISHIELD', 'COVAXIN', 'SPUTNIK-V']
else:
    vaccine = vaccineType



url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin"

headers = {'user-agent': 'my-app/0.0.1'}

payload = {'pincode': '301001', 'date': '15-05-2021'}

request_num = 0


while True:

    r = requests.get(url, params=payload, headers=headers)

    # print(r.url)
    print(request_num)

    center_addr_list = []
    center_stock_list = []

    avl_slot_list = []

    isVaccAvailable = False

    if r.status_code == requests.codes.ok :

        print('request successful')

        response = r.json()

        # print(type(response))
        
        center_details_list = (response["centers"])
        
        # print(type(center_details_list))
        
        for obj in center_details_list:
            for session in obj['sessions']:
                if session.available_capacity > 0:
                    if session.min_age_limit in minAgeLimit:
                        if obj.fee_type in feeType:
                            if session.vaccine in vaccine:
                                add_str = obj['name'] + ", " + obj['address']
                                avl_slot_list.append(Slot(
                                    address=add_str, 
                                    date=session.date, 
                                    minAge=session.min_age_limit, 
                                    vaccType=session.vaccine, 
                                    feeType=obj.fee_type, 
                                    avlCapacity=session.available_capacity
                                ))






            center_addr_list.append(obj['name'] + ", " + obj['address'])
            sum_vacc = 0
            for session in obj['sessions']:
                sum_vacc += session['available_capacity']
                if sum_vacc > 0:
                    isVaccAvailable = True
            center_stock_list.append(sum_vacc)
        
        
        # message_text = '\n'.join(zip(center_addr_list,center_stock_list))
        # message_text = ''
        for i in range(len(center_addr_list)):
            print(f'{i+1}) {center_addr_list[i]} Dose Available: {center_stock_list[i]}')
            # message_text += f'{i+1}) {center_addr_list[i]} Dose Available: {center_stock_list[i]}\n'
        # print(message_text)
        # telegram_send.send(messages=[message_text])
        
        if isVaccAvailable:
            telegram_send.send(messages=['Vaccine available at a center: check your dashboard.'])

    else:
        print(r.status_code)
        #telegram_send.send(messages=[r.text])

    time.sleep(10)
    request_num += 1




