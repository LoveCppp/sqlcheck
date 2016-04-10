#coding=utf-8

import threading

from sqlcheck import sqlcheck





for t in range(1,10):
	threads = []
	urls='http://www.modsecurity.org/testphp.vulnweb.com/artists.php?artist='+str(t)
	data={'url':urls}

	t1 = threading.Thread(target=sqlcheck,args=(data))
	threads.append(t1)
	for t in threads:
		t.setDaemon(True)
		t.start()
