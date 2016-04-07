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



	def newtask(self):
		res=urllib.urlopen(self.sqlmap+'/task/new').read()
		res=json.loads(res)
		self.taskid=res['taskid']
		return self.taskid

	#发送到sqlmap检查

	def sqlchecks(self,data):
		data=json.dumps(data)
		url=self.sqlmap+"/scan/"+self.taskid+"/start"
		req=urllib2.Request(url,data=data,headers={'Content-Type':'application/json'})
		res=urllib2.urlopen(req).read()
		res=json.loads(res)
		time.sleep(30)
		self.sqlstat(self.taskid)


	def sqlstat(self,taskid):
		url=self.sqlmap+"/scan/"+self.taskid+"/status"
		res=urllib2.urlopen(url).read()
		res=json.loads(res)
		if res['status']=="terminated":
			url=self.sqlmap+"/scan/"+self.taskid+"/data"
			datares=urllib2.urlopen(url).read()
			print type(datares)
			print datares
			return
		else:
			time.sleep(30)
			self.sqlstat(self.taskid)


	def checksql(self,args):
		if self.args=="task/new":
			self.taskid=self.sendsqlmap("task/new")
		elif self.args=="status"::
			res=self.sendsqlmap("status")

	

	def sendsqlmap(self,args):
		url=self.sqlmap+"/scan/"+self.taskid+"/"+slef.args
		res=urllib2.urlopen(url).read()
		res=json.loads(res)
		return res




data={'url':'http://xgb.hnist.cn/index.php?m=About&a=index&id=2'}
s=sqlcheck()
taskid=s.newtask()
s.sqlchecks(data)