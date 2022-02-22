import time
import pychromecast

services, browser = pychromecast.discovery.discover_chromecasts()
print(services)
# print(browser)
