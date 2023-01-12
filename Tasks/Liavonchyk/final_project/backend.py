import os
import sqlite3
from sqlite3 import Error
from consts import *

def populate_default_records(): #in order not to commit test DB here is a function that populates some dafault records
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        cur = conn.cursor()
        cur.execute("insert into materials (type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, update_timestamp, comment)\
            values ('polymer clay','staedtler','fimo','soft','tangerine','',57,57,'gram',6.5,2.1,date('2022-12-12'),'art territory',datetime('now'),'test1')")
        cur.execute("insert into materials (type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD, purchase_date, purchase_place, update_timestamp, comment)\
        values ('polymer clay','staedtler','fimo','soft','black','',57,56,'gram', 6.5, 2,  date('2022-12-01'), 'art territory', datetime('now'),'test2')")
        cur.execute("insert into materials (type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, update_timestamp, comment)\
        values ('polymer clay','the clay and paint factory','cernit','number one','brown','opaque',56,56,'gram', 5, 1.5,  date('2022-12-01'), 'leonardo',datetime('now'),'test3')")
        cur.execute("insert into accessories (type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, update_timestamp, comment)\
        values ('scissors','uncle feng','cheap chinese scissors',1, 0.5, date('2022-12-01'), 'art territory', datetime('now'),'test 5')")
        cur.execute("insert into production (type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, update_timestamp, comment)\
                values('cup','to sell', '{fimo soft black:5,fimo soft tangerine:1.5}', 35, 15, 13, 4, 'photoes/photo1.jpg', date('2022-12-12'), '{Maria Ivanova:375291111111}', datetime('now'),'cup with a dead unicorn')")
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
#        print('DB created')
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS materials (id  integer not null primary key, type text, article text, manufacturer text, trade_mark text, series text, color text, effects text, nominal_amount real, real_amount real, measure_units text, unit_price_BYN real, unit_price_USD real, purchase_date integer, purchase_place text, update_timestamp integer, comment text)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS accessories (id integer not null primary key, type text, article text, manufacturer text, description text, unit_price_BYN real, unit_price_USD real, purchase_date integer, purchase_place text, update_timestamp integer, comment text)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS production (id integer not null primary key, type text, for_whom text, used_materials text, price_BYN real, price_USD real, materials_price_BYN real, materials_price_USD real, photo_link text, sell_date integer, to_whom_was_given text, update_timestamp integer, comment text)")
        cur.execute(
            "CREATE TABLE IF NOT EXISTS rests (id  integer not null primary key, type text, article text, manufacturer text, trade_mark text, series text, color text, effects text, rest_amount real,  measure_units text, total_price_BYN real, total_price_USD real, update_timestamp integer, comment text)")
        conn.commit()
        if view_materials(): #if the db is empty, we will add some records. Test stuff
            pass
        else:
            populate_default_records()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def view_materials():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM materials")
    rows = cur.fetchall()
    conn.close()
    return rows

def view_accessories():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM accessories")
    rows = cur.fetchall()
    conn.close()
    return rows


def view_production():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM production")
    rows = cur.fetchall()
    conn.close()
    return rows

def add_material(type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    if purchase_date == 'now':
        pd = "date('now')"
    else:
        pd = "date('" + purchase_date + "')"
    coocoo = cur.execute(f"INSERT INTO materials (type, manufacturer, trade_mark, series, color, effects, nominal_amount, real_amount, measure_units, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, update_timestamp, comment) VALUES\
     ('{type}', '{manufacturer}', '{trade_mark}', '{series}', '{color}', '{effects}', '{nominal_amount}', '{real_amount}', '{measure_units}', '{unit_price_BYN}', '{unit_price_USD}', {pd}, '{purchase_place}', datetime('now'), '{comment}')")
    conn.commit()
    conn.close()
    return coocoo

def add_accessory(type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place, comment):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    if purchase_date == 'now':
        pd = "date('now')"
    else:
        pd = "date('" + purchase_date + "')"
    coocoo = cur.execute(f"INSERT INTO accessories (type, manufacturer, description, unit_price_BYN, unit_price_USD,  purchase_date, purchase_place,update_timestamp, comment) VALUES\
     ('{type}', '{manufacturer}', '{description}', '{unit_price_BYN}', '{unit_price_USD}', {pd}, '{purchase_place}', datetime('now'), '{comment}')")
    conn.commit()
    conn.close()
    return coocoo

def add_product(type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, comment):
    conn = sqlite3.connect(db_name)
    if sell_date == 'now':
        sd = "date('now')"
    else:
        sd = "date('" + sell_date + "')"
    cur = conn.cursor()
    coocoo = cur.execute(f"INSERT INTO production (type, for_whom, used_materials, price_BYN, price_USD, materials_price_BYN, materials_price_USD, photo_link, sell_date, to_whom_was_given, update_timestamp, comment) VALUES\
     ('{type}', '{for_whom}', '{used_materials}', '{price_BYN}', '{price_USD}', '{materials_price_BYN}', '{materials_price_USD}', '{photo_link}', {sd}, '{to_whom_was_given}', datetime('now'), '{comment}')")
    conn.commit()
    conn.close()
    return coocoo


# if __name__ == '__main__':
#     create_connection(db_name)

# print(view_materials())
# print(view_accessories())
# print(view_production())