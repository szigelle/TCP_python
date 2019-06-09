import socket

def main(command):

    if command == 'EXIT':
        response = HANDLERS[command]
    elif command in (
        'DEL'
            ):
        response = HANDLERS[command](key)
    elif command == 'PUT':
        response = HANDLERS[command](key, value)
    else:
        response (False, 'Unknown command type[{}]'.format(command))

# returns tuple containing command, key, optional value, optional value type
def parse_message(data):
    command, key, value, value_type = data.strip().split(';')
    if value_type:
        if value_type == 'INT':
            value = int(value)
        else:
            value = str(value)
    else:
        value = None
    return (command, key, value)

# OPERATION HANDLERS
# return tuple containing true and msg to send to client
def handle_put(key, value):
    DICT[key] = value
    return (True, 'Key [{}] set to [{}]'.format(key, value))

    if key not in DICT:
        return(False, 'ERROR: Key [{}] not found'.format(key))
    else:
        return(True, DICT[key])

def handle_del(key):
   if key not in DICT:
       return (False, 'ERROR: Key [{}] not found, not deleted'.format(key))
   else:
       del DICT[key]

def handle_exit():
    return

# initialize key and value
key = value = 0

# initialize Dictionary (key value store)
DICT = {}

# OPERATION LOOKUP
HANDLERS = {
    'PUT': handle_put(key, value),
    'DEL': handle_del(key),
    'EXIT': handle_exit(),
    }

if __name__ == '__main__':
    main(command)
