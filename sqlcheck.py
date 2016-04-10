#coding=utf-8

import json
import sys
import os
import urllib
import urllib2
import time
import threading


		

class sqlcheck(threading.Thread):		
	#新建任务
	def __init__(self,data):
		self.sqlmap='http://127.0.0.1:8775'
		self.taskid=''
		self.data=data
		self.checksql('task/new')
		self.sqlchecks()

	def run():
		for i in range(1,1000):
			self.data.put(i)
	#发送到sqlmap检查

	def sqlchecks(self):
		data=json.dumps(self.data)
		try:
			url=self.sqlmap+"/scan/"+self.taskid+"/start"
			req=urllib2.Request(url,data=data,headers={'Content-Type':'application/json'})
			res=urllib2.urlopen(req).read()
			res=json.loads(res)
			if res['success']==True:
				time.sleep(60)
				self.sqlstat()
			return False
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
		


