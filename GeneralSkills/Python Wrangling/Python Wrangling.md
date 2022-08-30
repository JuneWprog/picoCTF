# Python Wrangling

Download python

		wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py    
--2022-08-30 13:09:35--  https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1328 (1.3K) [application/octet-stream]
Saving to: ‘ende.py’

ende.py             100%[================>]   1.30K  --.-KB/s    in 0s      

2022-08-30 13:09:35 (3.09 MB/s) - ‘ende.py’ saved [1328/1328]

                                                                             
Download password

		wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt 
--2022-08-30 13:11:42--  https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/pw.txt
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 33 [application/octet-stream]
Saving to: ‘pw.txt’

pw.txt              100%[================>]      33  --.-KB/s    in 0s      

2022-08-30 13:11:43 (29.2 MB/s) - ‘pw.txt’ saved [33/33]

                                                                             
Download encoded text

		wget https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en
--2022-08-30 13:12:59--  https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/flag.txt.en
Resolving mercury.picoctf.net (mercury.picoctf.net)... 18.189.209.142
Connecting to mercury.picoctf.net (mercury.picoctf.net)|18.189.209.142|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 140 [application/octet-stream]
Saving to: ‘flag.txt.en’

flag.txt.en         100%[================>]     140  --.-KB/s    in 0s      

2022-08-30 13:13:00 (62.7 MB/s) - ‘flag.txt.en’ saved [140/140]

                                                                             
Run the python

		python ende.py
Usage: ende.py (-e/-d) [file]
                                                                             
Check the password

		cat pw.txt
aa821c16aa821c16aa821c16aa821c16
                                                                          
Run python

		python ende.py -d flag.txt.en
Please enter the password:aa821c16aa821c16aa821c16aa821c16
picoCTF{4p0110_1n_7h3_h0us3_aa821c16}

## Flag
picoCTF{4p0110_1n_7h3_h0us3_aa821c16}


