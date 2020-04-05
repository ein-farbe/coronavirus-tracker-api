#
# before run this script, execute below command to get raw data.
# $ curl https://coronavirus-tracker-api.herokuapp.com/v2/locations/139 | json_pp > covid_jp.txt
#

import json
from collections import OrderedDict
import pprint
import matplotlib.pyplot as plt
import math

filename = ['covid_jp.txt', 'covid_us.txt', 'covid_it.txt', 'covid_de.txt', 'covid_es.txt', 'covid_cn_hubei.txt']
dataname = ['Japan',        'US',           'Italy',        'Germany',      'Spain',        'China_Hubei']
linecolor = ['b',           'm',            'g',            'k',            'c',            'r']

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

for i in range(len(filename)):
    print(filename[i])
    with open(filename[i]) as f:
        raw = f.read()
    
    json_data = json.loads(raw, object_pairs_hook=OrderedDict)
    dic_conf = json_data['location']['timelines']['confirmed']['timeline']
    dic_deat = json_data['location']['timelines']['deaths']['timeline']
    
    key = []
    conf = []
    deat = []
    
    for k,v in sorted(dic_conf.items(), key=lambda x: x[0]):
        key.append(k[5:10])
        conf.append(v)
    
    for k,v in sorted(dic_deat.items(), key=lambda x: x[0]):
        deat.append(v)
    
    key = key[35:]
    conf = conf[35:]
    deat = deat[35:]
    idx = range(len(key))
    
    ax.plot(conf, linecolor[i], label=dataname[i])
    #ax.plot(deat, 'r', label='death')
    ax.set_xticks(idx)
    ax.set_xticklabels(key, rotation=90, fontsize='small')
    ax.set_title('Covid19')
    ax.set_xlabel('Date')
    ax.set_ylabel('Confirmed')

ax.legend(loc='best')
plt.show()

print('finish.')

