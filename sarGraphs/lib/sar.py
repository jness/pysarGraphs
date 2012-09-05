from pySar.lib import sar
import os

def get_cpu(key):
    'Get usage for a specific key in cpu report'
    results = sar(sarbin='sar')
    items = [ float(i[key]) for i in results ]
    times = shorttimes(results)
    return zip(times, items)

def get_swap(key):
    'Get usage for a specific key in swap report'
    results = sar(sarbin='sar', saroptions='-S')
    items = [ float(i[key]) for i in results ]
    times = shorttimes(results)
    return zip(times, items)

def get_memory():
    'Get usage for a specific key in memory report'
    results = sar(sarbin='sar', saroptions='-S')
    items1 = [ float(i['kbmemused']) for i in results ]
    items2 = [ float(i['kbbuffers']) for i in results ]
    items3 = [ float(i['kbcached']) for i in results ]
    times = shorttimes(results)
    return zip(times, items1, items2, items3)

def get_load():
    'Get usage for a specific key in load report'
    results = sar(sarbin='sar', saroptions='-q')
    items1 = [ float(i['ldavg-1']) for i in results ]
    items2 = [ float(i['ldavg-5']) for i in results ]
    items3 = [ float(i['ldavg-15']) for i in results ]
    times = shorttimes(results)
    return zip(times, items1, items2, items3)
    
def shorttimes(results):
    longtimes = [ i['timestamp'] for i in results ]
    shorttimes = []
    for time in longtimes:
        t = '%s:%s' % (time.split(':')[0], time.split(':')[1])
        shorttimes.append(t)
    return shorttimes
