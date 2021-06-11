from utils.colors import *
from urllib.parse import urlparse

DATE_TIME ='%Y-%m-%d %H:%M:%S'
FORMAT = f'{BLUE}%(asctime)s{RESET} - %(color)s%(levelname)s{RESET} - {BLACKB}%(name)s{RESET} - {GREEN}%(method)s{RESET} - %(message)s'

def isValidURL(url):
    try:
        result = urlparse(url)
        _ = all([ result.scheme, result.netloc, result.path ])
    except:
        return False
    return True

def getFolderName(url):
    splitURL = url.split('/')
    fileName = splitURL[-1]
    return fileName