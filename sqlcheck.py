#coding=utf-8

import json
import sys
import os
import urllib
import urllib2
import time



		

class sqlcheck():		
	#新建任务
	def __init__(self):
		self.sqlmap='http://127.0.0.1:8775'
		self.taskid=''

	#发送到sqlmap检查

	def sqlchecks(self,data):
		data=json.dumps(data)
		try:
			url=self.sqlmap+"/scan/"+self.taskid+"/start"
			req=urllib2.Request(url,data=data,headers={'Content-Type':'application/json'})
			res=urllib2.urlopen(req).read()
			res=json.loads(res)
			time.sleep(30)
			self.sqlstat()
		except urllib2.URLError, e:
			print e.reason
				
		


	def sqlstat(self):
		res=self.sendsqlmap("status")
		if res['status']=="terminated":
			datares=self.sendsqlmap("data")
			if datares['data']== None:
				 return False
			print datares['data']
			#注入 入库
		else:
			time.sleep(30)
			self.sqlstat()


	def checksql(self,args):
		if args=="task/new":
			res=self.sendsqlmap("task/new")
			self.taskid=res['taskid']
		elif args=="status":
			self.sendsqlmap("status")
		elif args=="data":
			self.sendsqlmap("data")

	def sendsqlmap(self,ags):
		try:
			if self.taskid =='':
				url=self.sqlmap+"/"+ags
			elif self.taskid != '':
				url=self.sqlmap+"/scan/"+self.taskid+"/"+ags
			res=urllib2.urlopen(url).read()
			res=json.loads(res)
			return res
		except urllib2.URLError, e:
			print e.reason
		




data={'url':'http://www.modsecurity.org/testphp.vulnweb.com/artists.php?artist=1'}
s=sqlcheck()
s.checksql('task/new')
s.sqlchecks(data)