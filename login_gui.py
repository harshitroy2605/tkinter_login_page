from tkinter import *



class Login_Form(Tk):
	def __init__(self):
		super().__init__()
		self.geometry("700x600")
		self.resizable(False, False)

	def Labels(self):
		self.Background_Image=PhotoImage(file='background_img.png')

		self.Background_Image_Label=Label(self,image=self.Background_Image)   #Background image
		self.Background_Image_Label.place(x=0,y=0,relwidth=1,relheight=1)
		
		self.canvas=Canvas(self, width=400, height=450)                       #backgrounf canvas
		self.canvas.place(x=150,y=60)
		
		self.Login_Title=Label(self,text="Login",font="bold, 30")             #login Title on Top
		self.Login_Title.place(x=300,y=90)
		
		self.User_Name_Label=Label(self,text="Email",font="8")                 #User Name Label
		self.User_Name_Label.place(x=200,y=150)

		self.Password_label=Label(self,text="Password",font="8")               #Password Label
		self.Password_label.place(x=200,y=250)


	def Entry(self):
		self.User_Name=Text(self, borderwidth=0, highlightthickness=0, wrap="word",width=29, height=2)
		self.User_Name.place(x=200,y=185)


		self.Password=Entry(self, borderwidth=0,show='*', highlightthickness=0)
		self.Password.place(x=200,y=285,width=235,height=33)



	def Buttons(self):
		self.Facebook_Button_Image=PhotoImage(file="facebook.png")
		self.Facebook_Button=Button(self,image=self.Facebook_Button_Image,command=self.Facebook_Function,border=0)
		self.Facebook_Button.place(x=278,y=440)


		self.Instagram_Button_Image=PhotoImage(file="instagram.png")
		self.Instagram_Button=Button(self,image=self.Instagram_Button_Image,command=self.Instagram_Function,border=0)
		self.Instagram_Button.place(x=328,y=440)


		self.Twitter_Button_Image=PhotoImage(file="twitter.png")
		self.Twitter_Button=Button(self,image=self.Twitter_Button_Image,command=self.Twitter_Function,border=0)
		self.Twitter_Button.place(x=380,y=440)


		self.Button_Image=PhotoImage(file="button.png")
		self.Button=Button(self,image=self.Button_Image,command=self.Execute_Function,border=0)
		self.Button.place(x=268,y=350)

	def Facebook_Function(self):
		print("rhyt")


	def Instagram_Function(self):
		print("regyre")

	def Twitter_Function(self):
		print("rgyre")

	def Execute_Function(self):
		print("er4hyg")



if __name__=="__main__":
	window=Login_Form()
	window.Labels()
	window.Entry()
	window.Buttons()
	window.mainloop()