# Windows Virtual Monitor

Here is the procedure to add a virtual monitor to your system (Windows 10 and Higher!)

Download our virtual display driver from <https://www.amyuni.com/downloads/usbmmidd_v2.zip>

Unpack the zip file to an empty folder, e.g. `c:\temp\usbmmidd_v2`

Make sure you read the License.txt file as with any other software product

Open a command prompt window as Administrator (you cannot add a device to your system unless you "Run As Administrator")

Run the following commands:

```bash
    cd c:\temp\usbmmid_v2 # (or whatever destination folder you chose)
    deviceinstaller64 install usbmmidd.inf usbmmidd
    # Make sure you see the message that the drivers 
    # are signed by Amyuni Technologies Inc. 
    # This is a confirmation that the drivers went through 
    # Microsoft driver signing procedure and are virus free
    deviceinstaller64 enableidd 1
```
