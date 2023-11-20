import getpass
import hashlib
import logging
import re
import time

logger = logging.getLogger('password_checker')


def input_and_check_password():
    password:str=getpass.getpass()
    passw = re.findall(r'/(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{8,}/g',password)
    if not passw:
        logger.warning('плохой пароль',time.time())
    elif not password:
        logger.warning('пустой пароль',time.time())
        return False
    try:
        hasher = hashlib.md5()
        hasher.update(password.encode('latin-1'))
        if hasher.hexdigest() == '098f6bcd4621d373caded4e832627b4f6':
            return True
    except ValueError:
        pass

def is_strong_password():
    password:str=getpass.getpass()
    passw = re.findall(r'/(?=.*[0-9])(?=.*[!@#$%^&*]){8,}/g',password.lower())
    if passw:
        return 0
    else:
        return 1


if __name__ == '__main__':
    logging.basicConfig(filename='stderr.txt',level=logging.DEBUG)
    count: int = int(input('сколько попыток будет'))
    while count > 0:
        if input_and_check_password():
            exit(0)
        count -=1
    exit(1)