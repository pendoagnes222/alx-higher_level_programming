urllib.request is a Python module for fetching URLs (Uniform Resource Locators). It offers a very simple interface, in the form of the urlopen function.
This is capable of fetching URLs using a variety of different protocols. It also offers a slightly more complex interface for handling common 
situations - like basic authentication, cookies, proxies and so oThese are provided by objects called handlersand openers


       FETCHING URLS
       
The simplest way to use urllib.request is as follows:

import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

If you wish to retrieve a resource via URL and store it in a temporary location, you can do so via the shutil.copyfileobj() and tempfile.NamedTemporaryFile() functions:

import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    pass



