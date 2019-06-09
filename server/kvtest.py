import socket

def main(data):
    if data.lower() == 'exit':
        response = HANDLERS[data.lower()]

    elif not data.split():
        return(True, 'invalid input, try again.')

    else:
        command, key = data.split(' ',1)

        if command.lower() == 'del':
            response = handle_del(key)

        elif command.lower() == 'put':
            key, value = key.split()
            response = handle_put(key, value)
        else:
            response = (False, 'Unknown command type [{}]'.format(command))
    return(response)

# initialize Dictionary (key value store)
DICT = {}
key = value = None

# OPERATION HANDLERS
# return tuple containing true and msg to send to client
def handle_put(key, value):

    DICT[key] = value
    print('...inside handle_put, DICT is [{}]'.format(DICT))

    return (True, 'Key [{}] set to [{}]'.format(key, value))

def handle_del(key):
   if key not in DICT:
       return (False, 'ERROR: key [{}] not found, no deletion'.format(key))
   else:
       del DICT[key]

def handle_exit():
    return (None, b'')


# OPERATION LOOKUP
HANDLERS = {
    'del': handle_del(key),
    'put': handle_put(key, value),
    'exit': handle_exit()
    }


if __name__ == '__main__':
    main(data)
