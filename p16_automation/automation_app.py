from credentials import mobile_number
import requests # to send data to text build
import schedule
import time

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone': mobile_number,
        'message': "Hey, salam",
        'key': "textbelt" 
    })
    print(resp.json())
    
    
schedule.every().day.at('21:00').do(send_message)

#for testing
# schedule.every(10).seconds.do(send_message)

# while True:
#     schedle.run_pending()
#     time.sleep(1)

send_message()