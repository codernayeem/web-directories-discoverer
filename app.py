import requests

def get_ans(qs):
    while True:
        ans = input(qs)
        if ans.lower() == 'y':
            return True
        elif ans.lower() == 'n':
            return False

if __name__ == '__main__':
    print('')
    print('\t++++++++++++++++++++++++++++++++++++')
    print('\t|||  Web Directories Discoverer  |||')
    print('\t|||        By @codernayeem       |||')
    print('\t====================================')
