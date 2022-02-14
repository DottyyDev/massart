from inspect import isdatadescriptor
from PIL import Image
import random

ids = [*range(0,9999)]
random.shuffle(ids)

count = 2 #how many you want generated

def pad(num):
    return num.rjust(4,0)

def file(fol,num):
    return str('./assets/'+str(fol)+'/'+num).rjust(4,'0')+'.png'
    
    
    
count -=1 
while count > 0:
    img = Image.open(file(1,str(count)[0])) 
    img.paste(file(2,str(count)[1]),(0,0),file(2,str(count)[1]))
    img.paste(file(3,str(count)[2]),(0,0),file(3,str(count)[2]))
    img.paste(file(4,str(count)[3]),(0,0),file(4,str(count)[3]))
    
    img.save(str(ids)[count].rjust(4,0)+'.png')

    count -= 1