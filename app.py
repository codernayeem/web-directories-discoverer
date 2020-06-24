import requests
from os.path import join

file_type_dict = {
    '1': 'dir_', 
    '2': 'file_', 
    '3': 'file_php_', 
    '4': '(dir-file) '
    }

word_type_dict = {
    '1': 'all',
    '2': 'common',
    '3': 'crazy',
    '4': 'extra'
    }

def get_ans(qs):
    while True:
        ans = input(qs)
        if ans.lower() == 'y':
            return True
        elif ans.lower() == 'n':
            return False

def request(url):
    try:
        r = requests.get(url)
        if r.status_code == 404:
            return False
        else:
            return r.status_code
    except Exception as e:
        print('\n[!] - OOps. Got error.\n')
        print(e, '\n')
        return None

if __name__ == '__main__':
    print('')
    print('\t++++++++++++++++++++++++++++++++++++')
    print('\t|||  Web Directories Discoverer  |||')
    print('\t|||        By @codernayeem       |||')
    print('\t====================================')

    while True:
        count = 0
        save = ''

        print('\n[+] - Enter Target link')
        target = input('[?] --> ')

        if target == '':
            continue

        if not (target.startswith('http://') or target.startswith('https://')):
            target = 'http://' + target

        if not target.endswith('/'):
            target += '/'
        
        print('\n---> Let\'s use buitin dictionaries! ')
        while True:
            print('\n--> Choose dictionary type? ')
            print('  1. Only Directory')
            print('  2. Only Files')
            print('  3. Only Files (PHP)')
            print('  4. Directory & Files')
            ans = input('[>] ')
            if ans in ['1', '2', '3', '4']:
                file_type = ans
                break
        while True:
            print('\n--> Choose words type? ')
            print('  1. All')
            print('  2. Common')
            print('  3. Crazy')
            print('  4. Extra')
            ans = input('[>] ')
            if ans in ['1', '2', '3', '4']:
                word_type = ans
                break
        file_path = join('wordlist', file_type_dict[file_type] + word_type_dict[word_type] + '.wordlist')
            
        try:
            fl = open(file_path, 'r')
        except:
            print(f'[+] - Failed to open "{file_path}". Make sure that file exists.\n')
            continue
        directory_list = fl.read().strip().splitlines()
        fl.close()

        print('[+] - Searching started ...\n')

        for a_item in directory_list:
            a_item = a_item.strip()
            if a_item != '':
                link = target + a_item
                response = request(link)
                if response is None:
                    print('[+] - Got error. So we sttoped.')
                    break
                elif response:
                    print(f'\n[+] - Got at - {link} - [{response}]')
                    count += 1
                    
        print(f'\n[!] - All done ({count})')

        if not get_ans('\n[?] - Wanna try again? '):
            exit(0)
            