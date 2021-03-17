# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from kafka import KafkaProducer
from json import dumps
import time

class NaverscraperPipeline(object):
    def __init__(self):
        self.producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=[127.0.0.1:9092], value_serializer=lambda x :dumps(x).encode('utf-8'))

    def process_item(self, item, spider):
        item = dict(item)

        self.producer.send('my_topic_2stock', value = data)
        time.sleep(10)
        self.producer.flush()
        print('Done:')

        print('*********************',item,'*********************')
