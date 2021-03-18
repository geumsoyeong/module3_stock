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
        self.producer = KafkaProducer(acks=0, compression_type='gzip', bootstrap_servers=['52.88.172.54:9092'], value_serializer=lambda x :dumps(x).encode('utf-8'))

    def process_item(self, item, spider):
        item = dict(item)

        data = {"schema":{"type":"struct","fields":[{"type":"int32","optional":False,"field":"id"},{"type":"string","optional":False,"field":"stock_rank"},{"type":"string","optional":False,"field":"title"},{"type":"int32","optional":False,"field":"price"},{"type":"string","optional":False,"field":"low"},{"type":"int32","optional":False,"field":"volume"},{"type":"int32","optional":False,"field":"payment"},{"type":"int32","optional":False,"field":"buy"},{"type":"int32","optional":False,"field":"sell"},{"type":"string","optional":False,"field":"capitalization"},{"type":"string","optional":False,"field":"per"},{"type":"string","optional":False,"field":"roe"},{"type":"int64","optional":True,"name":"org.apache.kafka.connect.data.Timestamp","version":1,"field":"created_at"}],"optional":False,"name":"stock"},"payload":{"id":1,"stock_rank":item['stock_rank'],"title":item['title'],"price":item['price'],"low":item['low'],"volume":item['volume'],"payment":item['payment'],"buy":item['buy'],"sell":item['sell'],"capitalization":item['capitalization'],"per":item['per'],"roe":item['roe'],"created_at":int(time.time()*1000)}}


        self.producer.send('my_topic_stock', value = data)
        time.sleep(10)
        self.producer.flush()
        print('Done:')

        print('*********************',item,'*********************')
