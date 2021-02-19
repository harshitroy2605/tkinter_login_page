from tkinter import *
#from PIL import Image, ImageTk

root=Tk()

root.geometry("700x600")
root.resizable(False, False)


def execute_function():
	print("function which will be executed after the button click")


def instagram_function():
	print("this function is executed when instagram button is pressed ")


def facebook_function():
	print("this function is executed when facebook button is executed")

def twitter_function():
	print("this function is executed when twitter butoon is executed")



background_img=PhotoImage(file='background_img.png')



background_image_label =Label(root,image=background_img)

background_image_label.place(x=0,y=0,relwidth=1,relheight=1)

canvas =Canvas(root, width=400, height=450)
canvas.place(x=150,y=60)

login_title=Label(root,text="Login",font="bold, 30")
login_title.place(x=300,y=90)


user_name_label=Label(root,text="Email",font="8")
user_name_label.place(x=200,y=150)

user_name=Text(root, borderwidth=0, highlightthickness=0, wrap="word",width=29, height=2)
user_name.place(x=200,y=185)



password_label=Label(root,text="Password",font="8")
password_label.place(x=200,y=250)

password=Entry(root, borderwidth=0,show='*', highlightthickness=0)
password.place(x=200,y=285,width=235,height=33)



facebook_button_image=PhotoImage(file="facebook.png")
facebook_button=Button(root,image=facebook_button_image,command=facebook_function,border=0)
facebook_button.place(x=278,y=440)


instagram_button_image=PhotoImage(file="instagram.png")
instagram_button=Button(root,image=instagram_button_image,command=instagram_function,border=0)
instagram_button.place(x=328,y=440)

twitter_button_image=PhotoImage(file="twitter.png")
twitter_button=Button(root,image=twitter_button_image,command=twitter_function,border=0)
twitter_button.place(x=380,y=440)

button_image=PhotoImage(file="button.png")
button=Button(root,image=button_image,command=execute_function,border=0)
button.place(x=268,y=350)

root.mainloop()