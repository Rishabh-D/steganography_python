

from pylab import *

def encript():
    ask_msg=input("Enter the Message : ")
    ask_img=input("Enter the full Path  of Image file to encript:")
    
    
    img=imread(ask_img)
    img_split_address=ask_img.split('.')
    msg=ask_msg

    msg_len=str(len(msg))
    row,col,zi=img.shape
    


    for r in range(len(msg)):
        
        img[0][r][0]= ord(msg[r])
           
    
    imsave(img_split_address[0]+"_edit.jpg",img)
    print()    
    
    print("Original image retained")
    
    print("Message is encripted in file :"+img_split_address[0]+"_edit.jpg")
    print("Your key :"+msg_len)
    
    print("message encription successful")
    

    
def decript():
    key=int(input("Enter the key : "))
    img_address=input("Enter the full path of image to decript : ")
    img_data=imread(img_address)
   
    
    for i in range(key):
        print(chr(img_data[0][i][0]),end="")
    
                
    
    
    

ask=input("PRESS 1 to encript and 2 to decript image: ")

if(ask=="1"):
    encript()
    
elif (ask=="2"):
    decript()    




