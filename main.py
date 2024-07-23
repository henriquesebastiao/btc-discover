import sys
from time import time

from random import SystemRandom
from cryptos import Bitcoin

def format_time(time_run):
    if time_run < 60:
        return f'{time_run:.4f} seconds'
    elif time_run < 3600:
        minutes = time_run // 60
        seconds = time_run % 60
        return f'{minutes:.0f} minutes {seconds:.2f} seconds'
    else:
        hours = time_run // 3600
        minutes = (time_run % 3600) // 60
        seconds = time_run % 60
        return f'{hours:.0f} hours {minutes:.0f} minutes {seconds:.2f} seconds'

start_time  = time()

MIN = 0x2126875fd00000000
MAX = 0x1fffffffffffffffff

WALLETS = [
    '13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so',
    '1BY8GQbnueYofwSuFAT3USAhGjPrkxDdW9',
    '1MVDYgVaSN6iKKEsbzRUAYFrYJadLYZvvZ',
    '19vkiEajfhuZ8bs8Zu2jgmC6oqZbWqhxhG',
]

coin = Bitcoin()
stop = False

srandom = SystemRandom()

while not stop:
    private = hex(srandom.randint(MIN, MAX + 1))[2:]

    while len(private) < 64:
        private = '0' + private

    public = coin.privtopub(private)
    private_encoded = coin.encode_privkey(private, 'hex_compressed')
    address_compressed = coin.privtoaddr(private_encoded)

    print(f'{private}:{public}')

    for wallet in WALLETS:
        if address_compressed == wallet:
            execution_time = time() - start_time
            stop = True

            with open('found.txt', 'w', encoding='utf-8') as result:
                result.write('Private Key FOUND!\n')
                result.write(f'Address: {address_compressed}\n')
                result.write(f'PUBLIC:  {public}\n')
                result.write(f'PRIVATE: {private.strip('0')}')

            print('\n\033[1;32mFOUND!\033[m ✨')
            print(f'TIME: {format_time(execution_time)}')
            print(f'Address: \033[0;33m{address_compressed}\033[m')
            print(f'PUBLIC:  {public}')
            print(f'PRIVATE: \033[0;33m{private.strip('0')}\033[m\n')
            sys.exit(0)
