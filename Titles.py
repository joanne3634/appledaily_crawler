#coding: utf-8
import pandas as pd
import sys
import traceback
import operator
import json

from pprint import pprint

def ex():
	sys.exit()

def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')
	
	myData = pd.DataFrame()
	list_ = []
	list_.append(pd.read_csv ('appledaily/profiles/overall.csv', sep=',', dtype='unicode', encoding='utf-8', header=None));
	list_.append(pd.read_csv ('appledaily/profiles/未結案/overall.csv', sep=',', dtype='unicode', encoding='utf-8', header=None));
	myData = pd.concat(list_)

	myObjs = {}

	for idx, row in myData.iterrows():
		aid = row[0]
		title = row[5]
		url = row[7]
		# cover = 'db_covers/' + aid + '.jpg'
		article = 'db_articles/' + aid + '.htm'
		myObj = {}
		myObj['aid'] = aid
		myObj['title'] = title
		# myObj['cover'] = cover
		myObj['article'] = article
		myObj['url'] = url
		if aid not in myObjs:
			myObjs[aid] = myObj
		else:
			print('something wrong ...')
			ex()		

	myJSON = json.dumps (myObjs, ensure_ascii=False, indent=2, sort_keys=True).encode ('utf-8')
	ofn = './db_lists/titles.json'
	with open(ofn, 'w') as fw:
		fw.write (myJSON)

if __name__ == '__main__':
	try:
		main ()
	except:
		traceback.print_exc(file=sys.stdout)