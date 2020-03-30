# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class AdcoilPipeline(object):


    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = sqlite3.connect('myadcos')
        self.curr = self.con.cursor()

    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS adco_tb""")
        self.curr.execute(""" create table adco_tb(
        car_name text,
        car_model text,
        car_km integer,
        car_price integer,
        car_like integer)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute(
            """ insert into adco_tb values (?,?,?,?,?)""",(
                item['car_name'][0],
                item['car_model'][0],
                item['car_km'][0],
                item['car_price'][0],
                item['car_like'][0]
            ))
        self.con.commit()