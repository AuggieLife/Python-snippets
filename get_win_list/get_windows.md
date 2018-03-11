### Retrieving a  list of open windows on Linux

I play a lot of online poker.  Now while playing under a windows system there are plenty of useful apps and utlities to make playing much easier and more engaging.  My problem is that I only run Linux boxes so I thought I would make myself some utilities to help enhance my playing experience under the operating system I love.

The first utility I thought of was automatically moving my open tables and maybe stacking them with the idea of having the table with the most urgent action required to 'pop' to the top so I could act upon it.  Maybe I could eventually create a HUD to display certain stats.  Lots of potential fun and learning here but the first thing I needed to do was to figure out what 'tables' were open.  To do this I first needed a list of all open windows on my system, then maybe I could do some stuff with them.  Plus I'm sure there are plenty of other uses for having a list of open windows.  

After plenty of googling I came across a linux command line utility called `wmctrl` that gave me lots of info about the X window system and ways to manipulate it.  So my first order of business was to figure out how to access this with python.  

It turns out the standard library provides a library called `subprocess` that allows us to run command line programs from a pyhon script and retrieve the output.

Now the command for `wmctrl` that will return a list of open windows is:

```
wmctrl -lG
```
This returns a list of open windows and a bunch of info on each. 
`<window ID> <desktop ID> <X>,<Y>,<W>,<H> <client machine> <window title>`


