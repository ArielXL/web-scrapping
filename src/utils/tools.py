from utils.colors import *
from urllib.parse import urlparse

DATE_TIME ='%Y-%m-%d %H:%M:%S'
FORMAT = f'{BLUE}%(asctime)s{RESET} - %(color)s%(levelname)s{RESET} - {BLACKB}%(name)s{RESET} - {GREEN}%(method)s{RESET} - %(message)s'

def isValidURL(url:str) -> bool:
    try:
        result = urlparse(url)
        _ = all([ result.scheme, result.netloc, result.path ])
    except:
        return False
    return True

def getDomain(url:str) -> str:
    splitURL = url.split('/')
    fileName = splitURL[-1]
    splitFileName = fileName.split('.')
    if splitFileName[0] == 'www':
        domain = '.'.join(splitFileName[1:])
        return domain
    return fileName

def prefixFuntion(patron:str) -> list:
    pi, k = [ 0 for _ in patron ], 0
    for i in range(2, len(patron)):
        while k>0 and patron[k+1] != patron[i]:
            k = pi[k]
        if patron[k+1] == patron[i]:
            k += 1
        pi[i] = k
    return pi

def kmp(text:str, patron:str) -> list:
    ocurrencies, k = [], 0
    pi = prefixFuntion(patron)

    for i in range(1, len(text)):
        while k>0 and text[i] != patron[k+1]:
            k = pi[k]
        if text[i] == patron[k+1]:
            k += 1
        if k == len(patron) - 1:
            k = pi[k]
            ocurrencies.append(i - len(patron) + 1)

    return ocurrencies
