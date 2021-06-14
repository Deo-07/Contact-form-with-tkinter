from tkinter import*
import random
from PIL import Image,ImageTk
class Register:
    def __init__(self,root):
       self.root=root
       self.root.title("Registration Window")
       self.root.geometry("1350x700+0+0")
       self.root.config(bg="#cd2a87")
      
       #This is backgroung images (No need -----but IF you want to use )

      # self.bg=ImageTk.PhotoImage(file="back.jpg")
     #bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1) 



     
       
        #====Registration frames===
        
       frame1=Frame(self.root,bg="white") 
       frame1.place(x=480,y=80,width=760,height=600)

         
       frame2=Frame(self.root,bg="white") 
       frame2.place(x=720,y=80,width=150,height=90)
       

       frame3=Frame(self.root,bg="lightgrey") 
       frame3.place(x=700,y=440,width=250,height=50)
       



       #==Left images==
       self.left=ImageTk.PhotoImage(file="leftside.jpg")
       left=Label(self.root,image=self.left).place(x=80,y=80,width=400,height=600)



        #Right images  image of frame 2

       
       image = Image.open("perfact.jpg")
       photo = ImageTk.PhotoImage(image.resize((150, 70), Image.ANTIALIAS))
       label = Label(frame2, image=photo)
       label.image = photo
       label.pack()
     







       #Login-------
       title=Label(frame1,text="Login",font=("times new roman",30,"bold"),bg="white",fg="Black").place(x=50,y=50) 
       title2=Label(frame1,text="Login to your Account",font=("times new roman",20,"bold"),bg="white",fg="Black").place(x=50,y=120) 
       title3=Label(frame1,text="Thank You for getting back to the child desk",font=("times new roman",15),bg="white",fg="Black").place(x=50,y=190)


        #USERNAME -------
       fname=Label(frame1,text="Username",font=("Book Antiqua",18),bg="white",fg="Black").place(x=130,y=250)
       text_fname=Entry(frame1,font=("times new roman",15),bd=5).place(x=90,y=290,width=200)

       #password
       password=Label(frame1,text="Password",font=("Book Antiqua",18),bg="white",fg="Black").place(x=490,y=250)
       text_password=Entry(frame1,show="*",font=("times new roman",15),bd=5).place(x=490,y=290,width=200)


         
     #This is Captcha code ------------
   
     # create a combined string of alphabets and numbers 
       text = 'abcdefghijklmnopqrstuvwxyz0123456789'
       # make random choice of alphabets and
     # numbers from above string using choices() method.
       c = random.choices(text, k = 5)
       captcha = ''.join(c)
       print("Generated captcha is: ",captcha)
       Captcha=Label(frame1,text="Captcha",font=("",20,"bold"),bg="white",fg="Black").place(x=80,y=370) 
       capi=Label(frame3,text=captcha,font=("",25,"bold"),bg="lightgrey",fg="green").place(x=86,y=3)
       
 


      #This is Checkbox code -----------------
       chk=Checkbutton(frame1,text="",bg="#cd2a87",onvalue = 0, offvalue = -2, height=0,width = 0).place(x=90,y=440)
       reset=Label(frame1,text="Remmber me",font=("Arial",18),bg="white",fg="black").place(x=130,y=440)
       btn_reset=Button(frame1,text="Reset Password?",font=("Arial",18),bg="white",bd=0,fg="#cd2a87",cursor="hand2").place(x=490,y=440)
       self.btn_img=ImageTk.PhotoImage(file="button.jpg")
       btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=250,y=500)

      #------- Join child Desk
       reset=Label(frame1,text="Don't have an account yet?",font=("Arial",18),bg="white",fg="Black").place(x=190,y=550)
       btn_login=Button(self.root,text="join child desk",font=("Arial",18),bg="white",bd=0,fg="#cd2a87",cursor="hand2").place(x=915,y=625)


root=Tk()
obj=Register(root)  
root.mainloop()




