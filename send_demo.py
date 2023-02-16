import boto3
import logging
import time
from SnsWrapper import SnsWrapper

def send_demo(phone_num, t):
    
    print('-'*88)
    print("Starting the test run!")
    print('-'*88)
    
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    sns_wrapper = SnsWrapper(boto3.resource('sns', 
                                            region_name = 'us-east-1',
                                            aws_access_key_id = "AWS ACCESS KEY ID", 
                                            aws_secret_access_key = "AWS SECRET ACCESS KEY"))
    topic_name = f'test-1-{time.time_ns()}'
    
    print(f"Creating topic {topic_name}.")
    topic = sns_wrapper.create_topic(topic_name)
    
    phone_number = '+' + str(phone_num)
    if phone_number != '':
        print(f"Sending an SMS message directly from SNS to {phone_number}.")
        sns_wrapper.publish_text_message(phone_number, "Hi this is the Phendo Voice project! This is your daily text notification and reminder to please submit your daily log (if you haven't done so already) with voice recording and symptom report. Remember to use your personalized link! Thank you")
    
    print(f"Getting subscriptions to {topic_name}.")
    topic_subs = sns_wrapper.list_subscriptions(topic)
    for sub in topic_subs:
        print(f"{sub.arn}")
    
    print(f"Deleting subscriptions and {topic_name}.")
    for sub in topic_subs:
        if sub.arn != 'PendingConfirmation':
            sns_wrapper.delete_subscription(sub)
    sns_wrapper.delete_topic(topic)
    
    print("SUCCESS!")
    print('-'*88)

