import sys
from urllib.request import Request, urlopen
from datetime import datetime


def crawling(
        url='',
        encoding='utf-8',
        proc=lambda html:html,
        store=lambda html:html,
        # proc=None,
        err=lambda e: print('%s : %s' % (e, datetime.now()), file=sys.stderr)):
    try:
        request = Request(url)
        resp = urlopen(request)

        try:
            receive = resp.read()
            # result = receive.decode(encoding)
            # result = proc(result)
            result = store(proc(receive.decode(encoding)))
            # if proc is not None:
            #     result = proc(result)
            # if store is not None:
            #     result = store(result)
        except UnicodeDecodeError:
            result = receive.decode(encoding, 'replace')

        return result

    except Exception as e:
        err(e)
