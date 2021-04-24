import os
import urllib.parse as parse
import os.path as path

def getFilename(url):
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol=False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, p):
    return parse.urljoin(url, p)

def q2j(s):
    ps = s.split('&')
    for p in ps:
        pp = p.split('=')
        print("'{}':'{}',".format(pp[0], pp[1]))

if __name__ == '__main__':
    str = "profile=minimalmonthviewgridv2&abvariant=FLUX787_QuoteBlacklist:a|FLUX_GDT2791_SendPriceTraceToMixpanel:b|rts_wta_shadowtraffic:b&apikey=c32d1a225f454c49a44ddec56ddc6910"
    q2j(str)


    # print(os.name)

    # url = "https://blog.naver.com/jeonseongho/1212.jpg"
    # print("filename=", getFilename(url))
    # print("hostname=", getHostname(url))
    # print("URL=", getHostname(url, True))
    # print("QQ>>", urljoin("https://nave.com", "bbb.jpg?aaaa=1"))
