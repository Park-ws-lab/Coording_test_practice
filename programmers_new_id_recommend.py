def check(new_id):
    if new_id=='.':
        new_id=''
    else :
        while new_id[0]=="."or new_id[-1]=="." or ".." in new_id :
            if new_id[0]==".":
                new_id = new_id[1:]
            elif new_id[-1]==".":
                new_id = new_id[:-1]
            elif ".." in new_id:
                new_id = new_id.replace("..",".")
    return new_id
new_id="=.="
id=new_id.lower()
new_id=""
new_id=''.join([new_id+i for i in id if i.islower() or i.isdigit() or i=="-" or i=="_" or i=="."])
new_id=check(new_id)
if new_id=="":
    new_id=new_id+"a"

if len(new_id)>=16:
    new_id=new_id[0:15]
    
new_id=check(new_id)

while len(new_id)<=2:
    new_id = new_id + new_id[-1:]

print(new_id)
