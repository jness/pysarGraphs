from pySar.lib import sar
import os

def get_cpu(key):
    'Get usage for a specific key in cpu report'
    results = sar(sarbin='sar')
    items = [ float(i[key]) for i in results ]
    times = shorttimes(results)
    return zip(times, items)
    
def get_load(key):
    'Get usage for a specific key in cpu report'
    results = sar(sarbin='sar', saroptions='-q')
    items = [ float(i[key]) for i in results ]
    times = shorttimes(results)
    return zip(times, items)
    
def shorttimes(results):
    longtimes = [ i['timestamp'] for i in results ]
    shorttimes = []
    for time in longtimes:
        t = '%s:%s' % (time.split(':')[0], time.split(':')[1])
        shorttimes.append(t)
    return shorttimes
