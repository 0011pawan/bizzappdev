#find distance program



totaldistance=100

leftc=0
rightc=100
meet=0
leftc_meetdistance=0
rightc_meetdistance=0
lefttotaltime=0
righttotaltime=0


for i in range(1,151):
    if leftc<100:
        leftc=leftc+1
        if i//10==0:
            leftc=leftc-2
        
    if rightc>0:
        rightc=rightc-2
        if i//5==0:
            rightc=rightc+1
    

    if leftc>=rightc and meet==0:
        print('condition')
        meet=i
        leftc_meetdistance=leftc
        rightc_meetdistance=100-rightc
    if leftc==100 and lefttotaltime==0:
        lefttotaltime=i
    if rightc==0 and righttotaltime==0:
        righttotaltime=i

print('meeting time',meet)
print('meetdistance left',leftc_meetdistance)
print('meetdistance right',rightc_meetdistance)

print(lefttotaltime)
print(righttotaltime)


        
        
        
        
        

    
