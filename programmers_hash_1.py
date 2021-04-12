participant=["mislav","stanko","mislav","ana"]
completion=["mislav","stanko","ana"]
person={}
participant.sort()
completion.sort()
for i, j in zip(participant,completion):
    if i != j:
        print(i)
print(participant[-1])
    
