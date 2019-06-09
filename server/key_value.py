import socket

def main():

    if command == 'EXIT':
        response = HANDLERS[command]
    elif command == 'STORE':
        response = HANDLERS[command]
    elif command in (
        'GET',
        'DEL'
            ):
        response = HANDLERS[command](key)
    elif command == 'PUT':
        response = HANDLERS[command](key, value)
    else:
        response (False, 'Unknown command type[{}]'.format(command))

#    connection.sendall('{};{}'.format(response[0], response[1]))
#    connection.close()

# returns tumple containing command, key, optional value, optional value type
def parse_message(data):
    command, key, value, value_type = data.strip().split(';')
    if value_type:
#        if value_type == 'LIST':
#            value = value.split(',')
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

# return tuple containing true if key exists, and msg to send to client
def handle_get(key):
    if key not in DICT:
        return(False, 'ERROR: Key [{}] not found'.format(key))
    else:
        return(True, DICT[key])

# return tumple containing true of key could be deleted, and msg
def handle_del(key):
   if key not in DICT:
       return (False, 'ERROR: Key [{}] not found, not deleted'.format(key))
   else:
       del DICT[key]

# return tuple containing true, and msg to client containing all key-value pairs in data
# TRUNCATE?
def handle_store():
    print("Your stored data: ")
    return(True, DICT)

# returns tuple containing true, and msg to client stating connection to server shutting down
#def handle_exit():
#    return(True, '...EXITING SERVER')

key = value = 0

# Initialize Dictionary (key value store)
DICT = {}

# OPERATION LOOKUP
HANDLERS = {
    'PUT': handle_put(key, value),
    'GET': handle_get(key),
    'DEL': handle_del(key),
    'STORE': handle_store(),
#    'EXIT': handle_exit(),
    }

if __name__ == '__main__':
    main()
