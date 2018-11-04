import subprocess

subprocess.getoutput("iptables -F")
serip = input("enter the server ip address")
serpass = input("enter the server password")
clip = input("enter the client ip address")
clpass = input("enter the client password")
#option = input(""" 1 : to configure server nfs press 1
#		2 :	to configure client nfs press 2 """)
#if option == 1:
vikalp = input("""1- to share an existing directory press 1
		2- to make a new directory and then share""")
if vikalp == "1":
	
	path = input("enter the path of the directory")	
	subprocess.getstatusoutput("echo {} {} | cat >> /etc/exports".format(path,clip)) 
elif vikalp == "2":
	path = input("enter the directory name")
	
	subprocess.getstatusoutput("mkdir /{}".format(path)) 
	
	subprocess.getstatusoutput("echo /{} {} | cat >> /etc/exports".format(path,clip)) 
	subprocess.getstatusoutput("systemctl restart nfs")
	subprocess.getstatusoutput("iptables -F")


	yes =input("to make a file in this directory and share it type yes")
	if yes == "yes":
		name =input(" enter file name(eg.file.txt)")
		subprocess.getstatusoutput(" touch /{}/{}".format(path,name))
		
		message = input("write your message here")
		subprocess.getoutput("echo {} | cat >> /{}/{}".format(message,path,name)) 
 
option = input("""1- to share in an existing directory press 1
                2- to share in a new directory press 2""")
if option == "1":
                
	subprocess.getoutput("sshpass -p {} ssh -l root {} systemctl restart nfs".format(clpass,clip))
	subprocess.getoutput("sshpass -p {} ssh -l root {} iptables -F".format(clpass,clip))
	marg = input("enter the path of the directory")
	subprocess.getoutput("sshpass -p {} ssh -l root {} mount {}:{} {}".format(clpass,clip,serip,path,marg))
elif option == "2":
        marg = input("enter the directory name")
        subprocess.getoutput("sshpass -p {} ssh -l root {} mkdir /{}".format(clpass,clip,marg))
        subprocess.getoutput("sshpass -p {} ssh -l root {} mount {}:/{} /{}".format(clpass,clip,serip,path,marg))
  

	
