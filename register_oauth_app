from robobrowser import RoboBrowser
b = RoboBrowser(history=True)
b.open('https://github.com/login')
form= b.get_form(action='/session')
form['login'].value = ''#put your username here
form['password'].value = ''#put your password here
b.submit_form(form)
b.open('https://github.com/settings/applications/new')
form = b.get_form(action='/settings/applications')
form['oauth_application[callback_url]']='http://127.0.0.1:8080/callback'
form['oauth_application[name]']='tttte333st'
form['oauth_application[url]']='http://127.0.0.1:8080'
form['oauth_application[description]']='only my description'
r=b.submit_form(form)
keys=b.find_all(class_="keys")[0].find_all('dd')
client_id=keys[0].text
client_secret=keys[1].text
print (client_id)
print (client_secret)
