import tkinter, paramiko, time, os

#tkinter is the framwork, paramiko is the ssh tool,
#time is to break when making ssh connection, 
#so it has time to connect and os is a portable way of 
#using operating systems dependent functionalities.
class ShowInfo:
#to run the program.
	def __init__(self):
#putting in frames to the main window.
		self.main_window = tkinter.Tk()
		
		self.top_frame = tkinter.Frame(self.main_window)
		self.mid_frame = tkinter.Frame (self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)
#This is to create variables for the labels, and specify it as text

		self.value1 = tkinter.StringVar()
		self.value2 = tkinter.StringVar()
		self.value3 = tkinter.StringVar()
		self.value4 = tkinter.StringVar()
		
		self.label1 = tkinter.Label(self.top_frame, textvariable = self.value1)
		self.label2 = tkinter.Label(self.top_frame, textvariable = self.value2)
		self.label3 = tkinter.Label(self.top_frame, textvariable = self.value3)
		self.label4 = tkinter.Label(self.top_frame, textvariable = self.value4)
		
#Input widget
		self.prompt_label = tkinter.Label(self.mid_frame, text='Enter IP of router:')
		self.ip_entry = tkinter.Entry(self.mid_frame, width=10)
		
		self.prompt_label2 = tkinter.Label(self.mid_frame, text='Enter the destination folder:')
		self.dir_entry = tkinter.Entry(self.mid_frame, width=10)

		self.prompt_label3 = tkinter.Label(self.mid_frame, text='Enter the username of the router:')
		self.usr_entry = tkinter.Entry(self.mid_frame, width=10)
		
		self.prompt_label4 = tkinter.Label(self.mid_frame, text='Enter the password of the router:')
		self.pwd_entry = tkinter.Entry(self.mid_frame, width=10)

		self.prompt_label5 = tkinter.Label(self.mid_frame, text='Enter the name of the output file:')
		self.name_entry = tkinter.Entry(self.mid_frame, width=10)

		self.prompt_label6 = tkinter.Label(self.mid_frame, text='Enter command:')
		self.sendrouter_entry = tkinter.Entry(self.mid_frame, width=10)

		self.prompt_label7 = tkinter.Label(self.mid_frame, text='Enter command:')
		self.sendcommand_entry = tkinter.Entry(self.mid_frame, width=40)
		

		
#pack input
#IP
		self.prompt_label.pack(side='top')
		self.ip_entry.pack(side='top')
#Directory
		self.prompt_label2.pack(side='top')
		self.dir_entry.pack(side='top')
#Username
		self.prompt_label3.pack(side='top')
		self.usr_entry.pack(side='top')
#Password
		self.prompt_label4.pack(side='top')
		self.pwd_entry.pack(side='top')
#Name of file
		self.prompt_label5.pack(side='top')
		self.name_entry.pack(side='top')
#Send first command
		self.prompt_label6.pack(side='top')
		self.sendrouter_entry.pack(side='top')
#Send command
		self.prompt_label7.pack(side='top')
		self.sendcommand_entry.pack(side='top')

#buttons
		self.show_button = tkinter.Button(self.bottom_frame, text='Send command', command=self.show_data)
		self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
		
		self.show_button.pack(side='left')
		self.quit_button.pack(side='left')

#pack labels
		self.label1.pack(side='top')
		self.label2.pack(side='top')
		self.label3.pack(side='top')
		self.label4.pack(side='top')
		
		self.top_frame.pack()
		self.mid_frame.pack()
		self.bottom_frame.pack()
#keep the window open at all times
		tkinter.mainloop()
		
#Text function
	def show_data(self):
		router_ip = 'Connecting to router ip: '+ str(self.ip_entry.get())
		router_usr = 'Username: '+ str(self.usr_entry.get())
		router_pwd = 'Login successful'
		location = 'Downloaded configuration to: '+ str(self.dir_entry.get())
		
		self.value1.set(router_ip)
		self.value2.set(router_usr)
		self.value3.set(router_pwd)
		self.value4.set(location)
		input = ('Did you enter the ip?')
		try:
			sshClient = paramiko.SSHClient() # Create SSHClient object
			sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			sshClient.connect(self.ip_entry.get(), username=self.usr_entry.get(), password=self.pwd_entry.get())
			channel = sshClient.invoke_shell() # Create a channel object
			time.sleep(2)
			os.system('clear') # Clear/Whipe the terminal window
			sendrouter = self.sendrouter_entry.get()
			channel.send(sendrouter+'\n') # Enter router the Command Line Interface
			time.sleep(1) # Leave time for the router to enter CLI
			routerOutput = channel.recv(100000) # Read router. Output/replies not used
			# time.sleep(3) # Wait to buffer times out and is empty
			# channel.send('edit\n')
			sendcommand = self.sendcommand_entry.get()
			channel.send(sendcommand+'\n') # Make router list config
			# shell.send('show route\n'
			time.sleep(2) # Leave time for the router to list config
			output = channel.recv(100000) # Read router configuration output
			print (output) # List the configuration in the terminal window
			
			save_path = self.dir_entry.get()
			name_of_file = self.name_entry.get()

			completeName = os.path.join(save_path, name_of_filel)

			outFile = open(completeName,'wb')
			outFile.write(output) # Save the configuration in a file
			outFile.close()
			channel.close()
		except Exception as ex:
			print ('Something went wrong:')
			print (ex)

show_info=ShowInfo()
