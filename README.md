
### Getting a list of open Windows
This is going to produce a list  that will contain the information and attributes of all open windows in a linux system.  I enjoy playing online poker and plan on creating an app that will organize my open poker tables on my screen (the window titles also contain lots of info).  I also usually have an external monitor on my laptop and sometimes when I open a program without a monitor it opens up off my laptop screen.  When this happens I use wmctrl to move it so it is visable... I think a python script to automate this seems appropriate. However neither of these projects can get off the ground without being able to parse the open windows on my system.  Plus it was fun and a good learning process to build this little script.

First make sure you have "wmctrl" installed on your system

    sudo apt-get install wmctrl

Lets import the libraries we are going to use.  
We are going to use subprocess in order to run wmctrl
and we are also going to use regex to do a little parsing.


```python
import subprocess
import re
```

We will start by running wmctrl and pipeing the output to a variable.    
As this would normally return a 'bytes' type we will pass the 'encoding' keyword to 'run'
so we end up with a string.


```python
proc = subprocess.run(['wmctrl', '-lG'], encoding='utf-8', stdout=subprocess.PIPE)
windstr = proc.stdout
print (windstr)
```

    0x01000024 -1 0    744  1366 24   lubunto1 panel
    0x00c00003 -1 0    0    1366 768  lubunto1 pcmanfm
    0x00c0001e -1 1366 0    1920 1080 lubunto1 pcmanfm
    0x02800003  0 10   77   923  686  lubunto1 PokerStars Lobby
    0x03400001  0 5    25   1312 665  lubunto1 Get a list of open windows - Google Chrome
    0x03c0028b  0 65   66   1128 700  lubunto1 test.py [/tmp/test.py] - ~/Projects/testing/get_window_list.py [test.py] - PyCharm
    0x01400004  0 709  332  657  434  lubunto1 auggie@lubunto1: ~
    0x00c01170  0 2    219  798  547  lubunto1 testing
    


Cool!  However to make it look pretty 'wmctrl' adds a bunch of spaces as padding so lets get rid of the excess spaces so each attribute is separated by a single space to make splitting them up easier.


```python
windstr = re.sub(' +', " ", windstr)
print (windstr)
print (type(windstr))
```

    0x01000024 -1 0 744 1366 24 lubunto1 panel
    0x00c00003 -1 0 0 1366 768 lubunto1 pcmanfm
    0x00c0001e -1 1366 0 1920 1080 lubunto1 pcmanfm
    0x02800003 0 10 77 923 686 lubunto1 PokerStars Lobby
    0x03400001 0 5 25 1312 665 lubunto1 Get a list of open windows - Google Chrome
    0x03c0028b 0 65 66 1128 700 lubunto1 test.py [/tmp/test.py] - ~/Projects/testing/get_window_list.py [test.py] - PyCharm
    0x01400004 0 709 332 657 434 lubunto1 auggie@lubunto1: ~
    0x00c01170 0 2 219 798 547 lubunto1 testing
    
    <class 'str'>


So we now have a string that contains all of our seperate windows that are separated by a new line  "\n"  
Lets split that into a list of individual windows.


```python
windlist = windstr.split('\n')
print (windlist)
print (type(windlist))
```

    ['0x01000024 -1 0 744 1366 24 lubunto1 panel', '0x00c00003 -1 0 0 1366 768 lubunto1 pcmanfm', '0x00c0001e -1 1366 0 1920 1080 lubunto1 pcmanfm', '0x02800003 0 10 77 923 686 lubunto1 PokerStars Lobby', '0x03400001 0 5 25 1312 665 lubunto1 Get a list of open windows - Google Chrome', '0x03c0028b 0 65 66 1128 700 lubunto1 test.py [/tmp/test.py] - ~/Projects/testing/get_window_list.py [test.py] - PyCharm', '0x01400004 0 709 332 657 434 lubunto1 auggie@lubunto1: ~', '0x00c01170 0 2 219 798 547 lubunto1 testing', '']
    <class 'list'>


It appears we have an empty element at the end of our list so lets get rid of it.


```python
if windlist[-1] == '':
    windlist = windlist[:-1]
print (windlist)
```

    ['0x01000024 -1 0 744 1366 24 lubunto1 panel', '0x00c00003 -1 0 0 1366 768 lubunto1 pcmanfm', '0x00c0001e -1 1366 0 1920 1080 lubunto1 pcmanfm', '0x02800003 0 10 77 923 686 lubunto1 PokerStars Lobby', '0x03400001 0 5 25 1312 665 lubunto1 Get a list of open windows - Google Chrome', '0x03c0028b 0 65 66 1128 700 lubunto1 test.py [/tmp/test.py] - ~/Projects/testing/get_window_list.py [test.py] - PyCharm', '0x01400004 0 709 332 657 434 lubunto1 auggie@lubunto1: ~', '0x00c01170 0 2 219 798 547 lubunto1 testing']


Alright.  Now we can loop through our list of windows and create a list of each attribute and create a list of lists.  Note that each window has the following attributes:

* Window ID
* Desktop ID
* 'X' coordinate
* 'Y' coordinate
* Width
* Hieght
* Client Machine
* Window Title

Lets note that our Window Title can contain a bunch of spaces which could be annoying when splitting, however they are listed at the end of our list so we can simply split our string by spaces up until we reach the title and just keep the leftover as our title.


```python
windowlist = []
for line in range(len(windlist)):
    win = windlist[line].split(" ", 7)
    windowlist.append(win)
    
for item in range(len(windowlist)):
    print (windowlist[item])
    
    
    

```

    ['0x01000024', '-1', '0', '744', '1366', '24', 'lubunto1', 'panel']
    ['0x00c00003', '-1', '0', '0', '1366', '768', 'lubunto1', 'pcmanfm']
    ['0x00c0001e', '-1', '1366', '0', '1920', '1080', 'lubunto1', 'pcmanfm']
    ['0x02800003', '0', '10', '77', '923', '686', 'lubunto1', 'PokerStars Lobby']
    ['0x03400001', '0', '5', '25', '1312', '665', 'lubunto1', 'Get a list of open windows - Google Chrome']
    ['0x03c0028b', '0', '65', '66', '1128', '700', 'lubunto1', 'test.py [/tmp/test.py] - ~/Projects/testing/get_window_list.py [test.py] - PyCharm']
    ['0x01400004', '0', '709', '332', '657', '434', 'lubunto1', 'auggie@lubunto1: ~']
    ['0x00c01170', '0', '2', '219', '798', '547', 'lubunto1', 'testing']


And there you have it.  We can now access all of the information about each open window on our system.  I'm sure there are uses for this down the road.   

Here is our complete script without my babble.


```python
import subprocess
import re


def get_window_list():
    """
    A function that returns a list of open windows and
    their attributes.
    Each window in the list has a list of attributes in the following order:
    <window ID> <desktop ID> <X>,<Y>,<W>,<H> <client machine> <window title>
    """
    proc = subprocess.run(['wmctrl', '-lG'], encoding='utf-8', stdout=subprocess.PIPE)
    windstr = proc.stdout
    windstr = re.sub(' +', " ", windstr)
    windlist = windstr.split('\n')
    if windlist[-1] == '':
        windlist = windlist[:-1]
    windowlist = []
    for line in range(len(windlist)):
        win = windlist[line].split(" ", 7)
        windowlist.append(win)
    return windowlist


if __name__ == "__main__":
    print(*get_window_list(), sep='\n')
```

    ['0x01000024', '-1', '0', '744', '1366', '24', 'lubunto1', 'panel']
    ['0x00c00003', '-1', '0', '0', '1366', '768', 'lubunto1', 'pcmanfm']
    ['0x00c0001e', '-1', '1366', '0', '1920', '1080', 'lubunto1', 'pcmanfm']
    ['0x02800003', '0', '10', '77', '923', '686', 'lubunto1', 'PokerStars Lobby']
    ['0x03400001', '0', '5', '25', '1312', '665', 'lubunto1', 'Get a list of open windows - Google Chrome']
    ['0x03c0028b', '0', '65', '66', '1128', '700', 'lubunto1', 'test.py [/tmp/test.py] - ~/Projects/testing/get_window_list.py [test.py] - PyCharm']
    ['0x01400004', '0', '709', '332', '657', '434', 'lubunto1', 'auggie@lubunto1: ~']
    ['0x00c01170', '0', '2', '219', '798', '547', 'lubunto1', 'testing']

