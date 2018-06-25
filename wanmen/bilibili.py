import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs
import re
import json
from IPython.display import Image
from IPython.core.display import HTML
import matplotlib.pyplot as plt
#the most important thing is to find this API:
#https://bangumi.bilibili.com/web_api/get_ep_list?season_id=207&season_type=1
season_id = [1177,1178,2655,1180,1179]
all_cid = []
all_avid = []
for st,sid in enumerate(season_id):
	cids = []
	avids = []
	url = 'https://bangumi.bilibili.com/web_api/get_ep_list?season_id='+str(sid)+'&season_type='+str(st)
	response = bs(requests.get(url).text,'lxml')
	response = response.p
	text = json.loads(response.text)
	for item in text['result']:
		cids.append(item['cid'])
		avids.append(item['avid'])
	all_cid.append(cids)
	all_avid.append(avids)
#all_danmu = []
for sid,scid in enumerate(all_cid):#season
	#s_danmu = []
	print(f"season {sid}")
	for eid,ecid in enumerate(scid):#episode
		print(f"episode {eid}")
		e_danmu = []
		url = 'https://comment.bilibili.com/rolldate'+','+str(ecid)
		timestamp = json.loads(requests.get(url).text)#!!!json.load
		for tsid,item in enumerate(timestamp):#timestamp
			print(f"season {sid} episode {eid} timeStamp {tsid}")
			url = f"https://comment.bilibili.com/dmroll,{item['timestamp']},{ecid}"
			danmu = bs(requests.get(url).text,'lxml').find_all('d')
			for ele in danmu:
				temp = ele['p'].split(',')
				temp.append(ele.text)
				e_danmu.append(temp) 
		result = pd.DataFrame(e_danmu,columns = ['time','format','font','color','data_unix','danmuchi','ID	','rowID','danmark'])
		#s_danmu.append(e_danmu)
		filename = f'Season {sid+1} episode {eid+1}.csv'
		result.to_csv(filename,index = False)
	#all_danmu.append(s_danmu)	
			
	
	