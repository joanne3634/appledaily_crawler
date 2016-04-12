#coding: utf-8
import pandas as pd
import sys
import traceback
import shutil
import os

from pprint import pprint

def ex():
	sys.exit()

def main():
	reload(sys)
	sys.setdefaultencoding('utf-8')

	dirArticles = 'db_articles/'
	shutil.rmtree(dirArticles, ignore_errors=True)
	if not os.path.isdir(dirArticles):
		os.makedirs(dirArticles)

	dirDoneCase = 'db_articles_txt/done_case'
	shutil.rmtree(dirDoneCase, ignore_errors=True)
	if not os.path.isdir(dirDoneCase):
		os.makedirs(dirDoneCase)

	dirPendingCase = 'db_articles_txt/pending_case'
	shutil.rmtree(dirPendingCase, ignore_errors=True)
	if not os.path.isdir(dirPendingCase):
		os.makedirs(dirPendingCase)

	overallDoneCase = pd.read_csv ('appledaily/profiles/overall.csv', sep=',', dtype='unicode', encoding='utf-8', header=None)
	aidsDoneCase = overallDoneCase[0].values

	myFile = open(u'appledaily/profiles/未結案/overall.csv')
	overallPendingCase = pd.read_csv (myFile, sep=',', dtype='unicode', encoding='utf-8', header=None)
	aidsPendingCase = overallPendingCase[0].values

	for aid in aidsDoneCase:
		shutil.copy2('appledaily/profiles/' + aid[-1:] + '/' + aid + '/'+aid+'.htm',dirArticles+ '/' + aid + '.htm')

		txtPath = 'appledaily/profiles/' + aid[-1:] + '/' + aid + '/report.txt'
		if os.path.isfile(txtPath):
			if os.stat(txtPath).st_size < 10:
				continue

			with open (txtPath, 'rU') as txtIn:
				myLines = txtIn.read().splitlines()

			myLines = filter(None, myLines)
			outPath = dirDoneCase + '/' + aid + '.txt'
			with open (outPath, 'w') as txtOut:
				txtOut.write('\n'.join(myLines))
			# ex()

	for aid in aidsPendingCase:
		shutil.copy2('appledaily/profiles/未結案/' + aid[-1:] + '/' + aid + '/'+aid+'.htm',dirArticles+ '/' + aid + '.htm')
	
		txtPath = u'appledaily/profiles/未結案/' + aid[-1:] + '/' + aid + '/report.txt'
		if os.path.isfile(txtPath):
			if os.path.getsize(txtPath) == 0:
				continue

			with open (txtPath, 'rU') as txtIn:
				myLines = txtIn.read().splitlines()

			myLines = filter(None, myLines)
			outPath = dirPendingCase + '/' + aid + '.txt'
			with open (outPath, 'w') as txtOut:
				txtOut.write('\n'.join(myLines))
			# ex()

if __name__ == '__main__':
	try:
		main()
	except:
		traceback.print_exc(file=sys.stdout)