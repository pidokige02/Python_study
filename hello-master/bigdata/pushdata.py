import bigquery 
import sys, os

KeyFile = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
client = bigquery.get_client(json_key_file=KeyFile, readonly=False)

DATABASE = "bqdb"
TABLE = "test1"
# client.delete_table(DATABASE, TABLE)

if not client.check_table(DATABASE, TABLE):
    # client.delete_table(DATABASE, TABLE)
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'songno', 'type': 'numeric', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'albumid', 'type': 'string', 'description': 'album id'},
        {'name': 'rec', 'type': 'record', 'description': 'record',
          'fields': [ {'name': 'sub1', 'type': 'string'}]
          },
    ])

ttt = [
    {'songno': '2.27', 'title': '홍1', 'albumid': '121212121', "rec":  {"sub1": "abc1" } },
    # {'songno': '1.24', 'title': '홍3', 'albumid': '121212121', "rec.sub1": "abc1"},
    # {'songno': '222', 'title': '홍2', 'albumid': '121212121'},
    # {'songno': '30190630', 'title': '홍3', 'albumid': '10029181'},
 ]

try:
    pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
    # client._raise_executing_exception_if_error(pushResult)
    # client._raise_insert_exception_if_error(client.job)
except Exception as err:
    print(pushResult, err)

print("Pushed Result is", pushResult)
