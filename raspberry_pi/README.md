# Raspi

Here we will share the code for the raspberry pi, as well as some basic documentation when neccessary.

## Guide: Connecting to the Raspberry Pi using a computer and TigerVNC

### For Windows/Mac

1. Install TigerVNC on your device.
	- Go to [tigervnc.org](https://tigervnc.org/) and navigate to the [github release page](https://github.com/TigerVNC/tigervnc/releases). Then navigate to the [sourceforge link](https://sourceforge.net/projects/tigervnc/files/stable/1.15.0/) in latest releases and install the one appropriate to your device.

2. Power the Raspberry Pi.

3. You should now be able to see the "rover" wifi network in the list of networks you can connect to. Check your "available networks" under device settings if you can't see it listed. Connect to the "rover" wifi. <br />
### The IP address should always be <ins>10.20.1.1</ins>, if it doesn't work follow the instruction below:

	**For windows**
	- open terminal and run the following command:
	  ``` ipconfig /all ```
	- look for the Raspberry Pi or the "DHCP address" (it should look something like ``` xx.xx.x.x ```)
	
	**For Mac**
	- go to Settings -> Network -> Click Details -> Scroll down to Router, that's the IP address

5. Enter this address into the dialog box "VNC server: " and click "Connect"

6. The program should close and a new dialog box with username and password will appear.

7. Fill in the username and password (check discord for further details), a new window with the Raspberry Pi will open.

## Guide: Setting up the python server on the Raspberry Pi

1. Using the guide above, connect to the Raspberry Pi using TigerVNC.

2. Double click the terminal icon in the navigation bar.

3. Run the following commands in the terminal:
	- Setting up the virtual environment
	    - ```cd```
	    - ```source env/bin/activate```
	- Starting the server
	    - ```cd Desktop/RC```
	    - ```python3 x.py``` (whatever the current server file is)
     		- It should say "Server Started on Port XXXX" if you are successful.

### Frequent Errors

1. "/dev/tty0..." not found - unplug and replug the USB to the arduino it should fix it. If it doesnt well o777
2. Tab/Indent errors - just copy paste into vscode and fix it there.
3. Compilation errors - yo code bad fix it
