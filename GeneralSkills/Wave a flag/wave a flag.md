# Wave a flag

		wget https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm       
--2022-08-30 13:17:20--  https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10936 (11K) [application/octet-stream]
Saving to: ‘warm’

warm                100%[================>]  10.68K  --.-KB/s    in 0s      

2022-08-30 13:17:20 (26.0 MB/s) - ‘warm’ saved [10936/10936]

                                                                                                                                                          


		./warm -h
zsh: permission denied: ./warm
                                                                             
Warm is not executable, use chmod +x (change mode)to permit it execute.

r: read 1 

w: write 2

x: execute 4


		chmod +x warm
		
or 		
		chmod 777 warm


		./warm --help
I don't know what '--help' means! I do know what -h means though!                                                                             


		 ./warm -h
Oh, help? I actually don't do much, but I do have this flag here: picoCTF{b1scu1ts_4nd_gr4vy_755f3544}
