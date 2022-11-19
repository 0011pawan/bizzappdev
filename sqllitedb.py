import sqlite3

con=sqlite3.connect("MTS.db")
cr=con.cursor()

#Table creation task

creat1="create table Employee(eid int(5),ename varchar(10),primary key (eid))"
cr.execute(creat1)

create2="create table Department(eid int(5),Dname varchar(10),foreign key (eid) references Employee(eid) )"
cr.execute(create2)

create3="create table project(eid int(5), proname varchar(10),foreign key (eid) references Employee(eid))"
cr.execute(create3)

con.commit()
print('yes')

#Data insert task

eid=int(input('enter emp id'))
ename=input('enter emp name')
e="insert into Employee values(%d,'%s')"
cr.execute(e %(eid,ename))

eid=int(input('enter emp id for department'))
dname=input('enter department name')
d="insert into Department values(%d,'%s')"
cr.execute(d %(eid,dname))

eid=int(input('enter emp id for project'))
pname=input('enter project name')
p="insert into project values(%d,'%s')"
cr.execute(p %(eid,pname))

con.commit()
print('yes')


