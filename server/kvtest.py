import socket

def main(data):
    if data.lower() == 'exit':
        response = HANDLERS[data.lower()]
 
    else:
        try:
            command, key = data.split(' ',1)
        except ValueError:
            return(True, 'invalid input, try again.')

        if command.lower() == 'del':
            response = handle_del(key)

        else:
            try:
                key, value = key.split()
                response = handle_put(key, value)
            except ValueError:
                return(True, 'invalid input, try again.')
            if command.lower() == 'put':
                response = handle_put(key, value)
            else:
                return(True, 'invalid input, try again.')
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
