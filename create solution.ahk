#SingleInstance, Force

F2::
difficult := ""
name := ""
url := ""

while (url == ""){
	InputBox, url,, Enter url of task
	if (ErrorLevel == 1 || ErrorLevel == 2)
		return
}
while (difficult == ""){
	InputBox, difficult,, Enter difficult of task %url%
	if (ErrorLevel == 1 || ErrorLevel == 2)
		return
}
while (name == ""){
	InputBox, name,, Enter name of task %url%
	if (ErrorLevel == 1 || ErrorLevel == 2)
		return
}
path = %A_WorkingDir%\\%difficult%\\%name%
FileCreateDir, %path%
FileCreateDir, %path%\\python
FileCreateDir, %path%\\cpp
FileCreateDir, %path%\\%name%

FileAppend, # %name%`n<a href=%url%>source</a>, %path%\\README.md
FileAppend, # %name%`n<a href=%url%>source</a>, %path%\\%name%\\README.md
FileAppend, # %url%, %path%\\python\\main.py
FileAppend, `/`/ %url%, %path%\\cpp\\main.cpp
Run, %path%
Run, %path%\\python
Run, %path%\\cpp

return


F3::
reload
