#!/usr/bin/env python
import __future__
from builtins import input
from simplegist import Simplegist
import pickle
import sys
class gist:
        def __init__(self):
                self.usrname=''
                self.apitoken=''
                self.check=1
                self.prof=''
                self.delnm=''
                self.path=''
        def create(self):
                global cgist
                if self.usrname=='':
                        self.entry()
                cgist = Simplegist(username=self.usrname,api_token=self.apitoken)
                name=input("Enter name of Gist: ")
                desc=input("Enter description of Gist: ")
                self.prof=input("Public [T]/F: ").upper() or 'T' 
                if self.check!=0:
                        self.path=input("Enter path of file: ")
                file=open(self.path,"r")
                if self.prof=="T":
                        cgist.create(name=name, description=desc ,public='true', content=file.read())

                else:
                        cgist.create(name=name, description=desc ,public='false', content=file.read())
                print "\nurl : ",'https://gist.github.com/'+self.usrname+'/'+cgist.profile().getMyID(name)+"\n"
                file.close()
        def entry(self):
                data=open("details.dat","ab+")
                if len(data.read())==0:
                        self.usrname=input("Enter username :")
                        self.apitoken=input("Enter your API token (One time process) :")
                        pickle.dump(self.usrname,data)
                        pickle.dump(self.apitoken,data)
                        data.close()
                        return
                
                else:
                        data.close()
                        data=open("details.dat","rb")
                        self.usrname=pickle.load(data)
                        self.apitoken=pickle.load(data)
                        data.close()
                        return
        def view(self):
                if self.usrname=='':
                        self.entry()
                cgist = Simplegist(username=self.usrname,api_token=self.apitoken)
                lst=cgist.profile().listall()
                srno=1
                d=max([len(i) for i in lst])
                for i in lst:
                        id=cgist.profile().getMyID(i)
                        if srno<10:
                                print str(srno)+ ' '*((d+1)-len(i))+i +" : "+'https://gist.github.com/'+self.usrname+'/'+id
                        else:
                                print str(srno)+ ' '*(d-len(i))+i +" : "+'https://gist.github.com/'+self.usrname+'/'+id
                
                        srno+=1
                
        def delete(self):
                if len(self.delnm)==0:
                        self.delnm=input("Enter name of gist to be deleted :")
                cgist = Simplegist(username=self.usrname,api_token=self.apitoken)
                cgist.profile().delete(name=self.delnm)

        def deleteall(self):
                if self.usrname=='':
                        self.entry()
                cgist = Simplegist(username=self.usrname,api_token=self.apitoken)
                lst=cgist.profile().listall()
                for i in lst:
                        cgist.profile().delete(name=i)

a=gist()
	
if len(sys.argv)==1:
        print("Choices\n1) Upload\n2) View\n3) delete\n4) deleteall")
        ch=int(input("Enter your choice :"))
        if ch==1:
                a.entry()
                a.create()
        if ch==2:
                a.entry()
                a.view()
        if ch==3:
                a.entry()
                a.delete()
        if ch==4:
                a.entry()
                a.deleteall()
else:
        if sys.argv[1]=="-u":
                try:
                        a.path=sys.argv[2]
                        a.check = 0
                except:
                        pass
                a.create()
        if sys.argv[1]=="-l":
                a.entry()
                a.view()
        if sys.argv[1]=="-d":
                a.entry()
                try:
                        a.delnm=sys.argv[2]
                except:
                        pass
                a.delete()
        if sys.argv[1]=="-da":
                a.entry()
                try:
                        a.delnm=sys.argv[2]
                except:
                        pass
                a.deleteall()
        if sys.argv[1]=="-h":
                print "Usage: gist [COMMAND]\n"
                print "Upload: "
                print "  -u [*Path of File]        Uploads FILE to the GITHUB"
                print "View:"
                print "  -l                        Shows the LIST of all the GIST "
                print "Delete:"
                print "  -d [*Name of Gist]        DELETES the gist of the GIVEN NAME "
                print "  -da                       DELETES all the GISTS"
                print "Help:"
                print "  -h                        Displays help file"