import socket

# initialize Dictionary (key value store)
DICT = {}
key = value = None

def main(data):

    print('...inside kvtest.main(), data is [{}]'.format(data))
    print('inside kvtest.main()... dictionary is [{}]'.format(DICT))

    if data.lower() == 'exit':
        response = handle_exit()

    elif data.lower() == 'store':
        response = handle_store()

    else:
        try:
            command, key = data.split(' ',1)
        except ValueError:
            return(True, 'invalid input, try again.')

        print('... key is [{}]'.format(key))
        if command.lower() == 'del':
            response = handle_del(key)
        elif command.lower() == 'get':
            response = handle_get(key)
        else:
            try:
                key, value = key.split()
            except ValueError:
                return(True, 'invalid input, try again.')

            print('... value is [{}]'.format(value))

            if command.lower() == 'put':
                response = handle_put(key, value)

            else:
                response = (True, 'invalid input, try again')

    return(response)

# OPERATION HANDLERS
# return tuple containing true and msg to send to client
def handle_store():
    print('...inside handle_store')
    print('inside kvtest.main().handle_store()... dictionary is [{}]'.format(DICT))

    return(True, 'contents of key-velue store is [{}]'.format(DICT))

def handle_put(key, value):

    DICT[key] = value
    print('...inside handle_put, DICT is [{}]'.format(DICT))

    return (True, 'Key [{}] set to [{}]'.format(key, value))

def handle_get(key):
    print('...inside handle_get, key is [{}]'.format(key))
    if key not in DICT:
        return (False, 'ERROR: key [{}] not found'.format(key))

    else:
        return(True, 'value is [{}]'.format(DICT[key]))



def handle_del(key):

   print('...inside handle_del, key is [{}]'.format(key))
   if key not in DICT:
       return (False, 'ERROR: key [{}] not found, no deletion'.format(key))

   else:
       del DICT[key]
       return(True, 'Key [{}] deleted'.format(key))

def handle_exit():
    return (None, 'Exiting key value store')

if __name__ == '__main__':
    main(data)
