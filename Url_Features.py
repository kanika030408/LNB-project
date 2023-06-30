import re
from urllib.parse import urlparse

#make function to extend feature
# First Directory Length
def fd_length(url):
    urlpath = urlparse(url).path
    try:
        return len(urlpath.split('/')[1])
    except:
        return 0

#to count digit
def digit_count(url):
    digits = 0
    for i in url:
        if i.isnumeric():
            digits = digits + 1
    return digits

#to count letter in url
def letter_count(url):
    letters = 0
    for i in url:
        if i.isalpha():
            letters = letters + 1
    return letters

#find number of directory
def no_of_dir(url):
    urldir = urlparse(url).path
    return urldir.count('/')

#find IP is use in domain or not
def having_ip_address(url):
    match = re.search(
        # IPv4 in hexadecimal
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)'
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
    if match:
        return -1
    else:
        return 1
#find hostname
def hostname_length(url):
    return len(urlparse(url).netloc)

#find length of url
def url_length(url):
    return len(urlparse(url).path)

#all count features
def get_counts(url):
    count_features = []
    sym=['-','@','?','%','.','=','http','https','www']
    for i in sym:
        j=url.count(i)
        count_features.append(j)
    return count_features
