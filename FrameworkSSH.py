import tkinter, time, os, paramiko

class OpenPyProgram:
	def __init__(self):

		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		self.value1 = tkinter.StringVar()
		self.label1 = tkinter.Label(self.top_frame, text ="Main Menu", font=72)
		
		self.ssh_button = tkinter.Button(self.bottom_frame, text='SSH',
		bg="blue", fg="white", command=self.openSSH)
		self.scp_button = tkinter.Button(self.bottom_frame, text='SCP',
		bg="blue", fg="white", command=self.openSCP)
		self.quit_button = tkinter.Button(self.bottom_frame,
		text='Quit', bg="blue", fg="white", command=self.main_window.destroy)
		self.user_button = tkinter.Button(self.bottom_frame, text='User Manual', bg="yellow", fg="black", font=24, command=self.user_manual)
		
		self.ssh_button.pack(side='left')
		self.scp_button.pack(side='left')
		self.quit_button.pack(side='left')
		self.user_button.pack(side='left')
		self.label1.pack(side='top')
		
		self.top_frame.pack()
		self.bottom_frame.pack()

tkinter.mainloop()

	def openSSH(self):

	import SSH

	def openSCP(self):

	import SCP

	def user_manual(self):

		self.main_window = tkinter.Tk()
		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
		self.value1 = tkinter.StringVar()
		self.label1 = tkinter.Label(self.top_frame, text ="To gather
		your super cool configurations, simply go back to the mainmenu and click on the
		buttons", font=48)
		self.label1.pack(side='top')
		self.top_frame.pack()
		self.bottom_frame.pack()


tkinter.mainloop()
open = OpenPyProgram()
