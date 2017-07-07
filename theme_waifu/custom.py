import json
import subprocess
import time
import datetime
import psutil
import socket

#For some reason transparency fucks up

p = "#d2cbf5"
s = "#222222"
b = "#222222"

fg = "%{F"+p+"}"
bg = "%{B"+b+"}"

sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sc.connect(("8.8.8.8", 1))
ip = sc.getsockname()[0]

def get_left():
	raw = subprocess.check_output(["i3-msg", "-t", "get_workspaces"]).decode("utf-8")
	#res = "%{F"+p+"}%{B"+s+"} " + psutil.Process().username() + " "
	res = ""
	i3 = json.loads(raw)
	for w in i3:
		if(w["num"] == 1):
			if(w["focused"]):
				res += "%{B"+p+"}%{F"+b+"} " + w["name"].split(": ")[1] + " " + fg + bg + "\u25E3 "
			else:
				res += " " + w["name"].split(": ")[1] + " "
		elif(w["focused"]):
			res += "%{F"+b+"}%{B"+p+"}\u25E3 " + w["name"].split(": ")[1] + " " + fg + bg + "\u25E3 "
		else:
			res += w["name"].split(": ")[1] + " "
	return res

def get_right():
	out = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"]).decode("utf-8").strip()
	return out + " \u25E2%{F"+b+"}%{B"+p+"} " + ip + " %{F"+s+"}%{B"+p+"}\u25E2%{F"+p+"}%{B"+s+"} " + str(psutil.disk_usage("/home").free/1024/1024/1024).split(".")[0] + " GiB %{F"+p+"}%{B"+b+"}"

def get_center():
	return "\u25E2%{F"+b+"}%{B"+p+"} " + str(datetime.datetime.now().time()).split(".")[0] + " " + fg + bg + "\u25E3 "

while(True):
	res = fg + bg
	try:
		res += "%{l}" + get_left() + "%{c}" + get_center() + "%{r}" + get_right()
	except:
		pass
	print(res)
	time.sleep(1./100)
