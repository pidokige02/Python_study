import urllib.parse as parse
import os.path as path
import ssl

def getFilename(url):
    return path.basename(parse.urlparse(url).path)

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urlencode(p):
    return parse.urlencode(p)

def urljoin(url, path):
    return path.urljoin(url, path)

def sslContext():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx

if __name__ == '__main__':
    URL = "https://postfiles.pstatic.net/MjAxOTAxMDNfMjYw/MDAxNTQ2NTA4NzYwNjQ3.fVyIE3nPM6zmvVZuaJG9tSAqzopYNzUGUpPHR9v86hMg.Hyq_lVTVWz-pnaSC3TZ8ue4iJOfJMgkOFVSQozQdYqUg.PNG.korea_diary/천안_호두과자.png?type=w966"
    print("URL>>", URL)
    print("fileName>>", getFilename(URL))
    print("hostName>>", getHostname(URL))
    print("hostName>>", getHostname(URL, True))
