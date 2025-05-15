import time
import random
import string
from typing import Optional

class URLShortener:
    def __init__(self):
        self.shortToLong = {}
        self.longToShort = {}
        self.baseURL = "http://short.ly/"   #Can't really use bit.ly since that's a real thing so I'm making a knockoff version
        self.charLimit = 7               #Limits characters after link

    def shortAlias(self) -> str:
        chars = string.ascii_letters + string.digits #This just adds random letters/numbers to the end of the shortened link
        return ''.join(random.choices(chars, k=self.charLimit))

    def shorten_url(self, originalURL: str, expireSeconds: Optional[int] = None) -> str:
        if originalURL in self.longToShort:
            short = self.longToShort[originalURL]
            return self.baseURL + short
        short = self.shortAlias()
        
        while short in self.shortToLong:    #Ensures unique characters for link generation
            short = self.shortAlias()

        expireTimer = time.time() + expireSeconds if expireSeconds else None

        self.shortToLong[short] = (originalURL, expireTimer)
        self.longToShort[originalURL] = short

        return self.baseURL + short

    def changedURL(self, shortURL: str) -> Optional[str]:
        if not shortURL.startswith(self.baseURL):
            return None

        alias = shortURL.replace(self.baseURL, "")
        if alias not in self.shortToLong:
            return None

        originalURL, expiration = self.shortToLong[alias]

        #Way to delete link after expiration
        if expiration and time.time() > expiration:
            del self.shortToLong[alias]
            del self.longToShort[originalURL]
            return None

        return originalURL

def main():
    shortener = URLShortener()

    original = "https://www.google.com/"
    short = shortener.shorten_url(original)
    print(f"Shortened: {short}")
    resolved = shortener.changedURL(short)
    print(f"Resolved: {resolved}")
    assert resolved == original

    shortExpirationTimer = shortener.shorten_url("https://temporary.com", expireSeconds=2) #Timer on shortened URL expires in 2 seconds as an example
    print(f"Shortened (expiring): {shortExpirationTimer}")
    time.sleep(3)
    resolvedExpiration = shortener.changedURL(shortExpirationTimer)
    print(f"Resolved after expiration: {resolvedExpiration}") #Message plays when link duration expires
    assert resolvedExpiration is None

main()
