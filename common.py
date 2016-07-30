
import cookielib
import urllib
from StringIO import StringIO
import urllib2
import gzip

import time
import random


def prepare(proxy=None):  # example: http://127.0.0.1:8087/
    ckp = urllib2.HTTPCookieProcessor(cookielib.CookieJar())

    if use_proxy:
        proxy_handler = urllib2.ProxyHandler({"http": proxy})
        opener = urllib2.build_opener(proxy_handler, ckp)
    else:
        null_proxy_handler = urllib2.ProxyHandler({})
        opener = urllib2.build_opener(null_proxy_handler, ckp)

    urllib2.install_opener(opener)


_std_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip",
    "Cache-Control": "no-cache",
}


def get_std_headers():
    return _std_headers


def open_request_and_read(request):
    response = urllib2.urlopen(request)
    if response.info().get("Content-Encoding") == "gzip":
        buf = StringIO(response.read())
        f = gzip.GzipFile(fileobj=buf)

        return f.read()
    else:
        return response.read()


def guarded_read(url, data=None):
    assert data is None or isinstance(data, dict)
    if data:
        data = urllib.urlencode(data)

    max_tries = 5
    num_tries = 0

    while True:
        num_tries += 1

        try:
            req = urllib2.Request(url, data=data, headers=_std_headers)
            return open_request_and_read(req)
        except urllib2.HTTPError, e:
            print "HTTP Error", e.code, e.msg
            print e.geturl()
            print e.fp.read()
        except Exception, e:
            print e
        finally:
            if num_tries == max_tries:
                return None

        random_sleep(20)


def simple_read(url):
    return open_request_and_read(urllib2.Request(url, headers=_std_headers))


def random_sleep(base=2):
    time.sleep(base + random.random())
