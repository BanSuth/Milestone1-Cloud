import os
from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError 

credentials_path = 'privateKey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/kafka-clusters-411917/subscriptions/smartmeter-sub'


#READY TO SUBSCRIBE NOW

def callback(message):
    print(f'Recieved message: {message}')
    print(f'data: {message.data}')
    
    if message.attributes:
        print("Attributes")
        for key in message.attributes:
            value - message.attributes.get(key)
            print(f"{key}: {value}")
    
    message.ack()

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f'Listening for messages on {subscription_path}')

with subscriber:
    try:
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()
        streaming_pull_future.result()


