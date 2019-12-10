import pymongo
import csv
connection = pymongo.MongoClient('mongodb://BluebotLog:bluelogic123@18.222.189.3:27017/chatlog')
db = connection['chatlog']
from db_connection import get_fallback_intent
from email_handler import send_mail


def generate_csv_bot(collection):
    try:
        result = get_fallback_intent(collection)
        csv_file = collection+"_default_fallback.csv"
        csv_columns = ['Text', 'Count', 'Intent', 'Entity Value', 'Entity Name']
        with open(csv_file, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
            writer.writeheader()
            for key in result['results']:
                csv_file.write('"%s",%s, %s\n' % (key['_id'], key['value'], 'default_fallback'))

        send_mail('rino@bluelogic.ae', "Attached Report Weekly of "+collection, collection)
        send_mail('anton@bluelogic.ae', "Attached Report Weekly of"+collection, collection)
        return print(result)
    except ValueError as e:
        return print(e)


if __name__ == '__main__':
    register = ['avivo', 'national_bonds', 'healthcare', 'aster']
    for mail in register:
        generate_csv_bot(mail)