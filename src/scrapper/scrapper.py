import os
import time
import requests
import urllib.request

from re import match
from utils.tools import *
from bs4 import BeautifulSoup
from utils.logger import parseLevel
from utils.logger import LoggerFactory as Logger

log = Logger(name='Scrapper')
log.setLevel('DEBUG')

class Scrapper:

    def __init__(self, url:str):
        if isValidURL(url):
            self.url = url
        else:
            log.error('Invalid URL', '__init__')

    def getHTML(self, url:str):
        wait = 0
        while True:
            try:
                log.info(f'GET {url}', 'getHTML')
                with requests.get(self.url) as response:
                    html = response.text
                break
            except Exception:
                log.error(f'An error ocurred when try to get {url}', 'getHTML')

                if wait == 2:
                    log.error(f'Download failed: {url}', 'getHTML')
                    return

                log.info(f'Trying again in {2 ** wait} seconds', 'getHTML')
                time.sleep(2 ** wait)
                wait = wait + 1
        return html

    def getLink(self, link:str):
        wait = 0
        while True:
            try:
                log.info(f'GET {link}', 'getLink')
                with urllib.request.urlopen(link) as response:
                    html = response.read()
                break
            except Exception:
                log.error(f'An error ocurred when try to get {link}', 'getLink')

                if wait == 2:
                    log.error(f'Download failed: {link}', 'getLink')
                    return

                log.info(f'Trying again in {2 ** wait} seconds', 'getLink')
                time.sleep(2 ** wait)
                wait = wait + 1
        return html

    def startRequests(self):

        html = self.getHTML(self.url)
        if html == None:
            return

        baseURL = self.formURL(self.url)
        links = []
        soup = BeautifulSoup(html, 'lxml')
        soupTag = soup.find_all(self.extractTags)

        for idx in range(len(soupTag)):
            if soupTag[idx].has_attr('href'):
                name = self.putName(soupTag[idx]['href'])
                links.append((urllib.parse.urljoin(baseURL, soupTag[idx]['href']), name))
                soupTag[idx]['href'] = name

            if soupTag[idx].has_attr('src'):
                name = self.putName(soupTag[idx]['src'])
                links.append((urllib.parse.urljoin(baseURL, soupTag[idx]['src']), name))
                soupTag[idx]['src'] = name

        folderName = getFolderName(self.url)
        path = os.path.join('downloads', folderName)
        page = 'index.html'
        if not os.path.isdir(path):
            os.makedirs(path)

        with open(os.path.join(path, page), 'wb') as fileHTML:
            fileHTML.write(soup.prettify(formatter='html').encode('utf-8'))

        for (tag_url, name_url) in links:
            scheme, netloc, path, query, fragment = urllib.parse.urlsplit(tag_url)
            path = urllib.parse.unquote(path)
            link = urllib.parse.urlunsplit((scheme, netloc, path, query, fragment))
            if not link.endswith('.ico'):
                html = self.getLink(link)

                with open(os.path.join('downloads', folderName, name_url), 'wb') as fileHTML:
                    fileHTML.write(html)

    def extractTags(self, tag:str):
        return (tag.has_attr('href') and (match(r'.*\.php', tag['href']) 
            or match(r'.*\.css', tag['href']) or match(r'.*\.js', tag['href']) 
              or match(r'.*\.jpg', tag['href']) or match(r'.*\.png', tag['href']) 
                or match(r'.*\.ico', tag['href']))) or (tag.has_attr('src') 
                  and (match(r'.*\.php', tag['src']) or match(r'.*\.css', tag['src']) 
                    or match(r'.*\.js', tag['src']) or match(r'.*\.jpg', tag['src']) 
                      or match(r'.*\.png', tag['src']) or match(r'.*\.ico', tag['src'])))

    def putName(self, name):
        splitName = name.replace('?', '').replace('=', '').split('/')
        splitName = splitName[max(0, len(splitName) - 4):]
        return '-'.join(splitName)

    def formURL(self, url:str):
        splitURL = url.split('/')
        if splitURL[0] == 'file:':
            return '/'.join(splitURL[0:])
        else:
            return '/'.join(splitURL[0:3])
