# Offline Password Generator #

Welcome to the Offline Password Generator!

This program runs on Python(Python version 3.12.3 or newer)

I had this idea from seeing Google recommending generated passwords on sites and storing it for ease of access 
if you return to the site. My issue with this comes from the fact that many companies face cyber security issues 
and as such all of that information can fall into the wrong hands while connected to such a large online source.
So, I had the idea of make this program to create a randomly generated password(between 10 and 16 characters in
length and containing at least 1 number and 1 special character) and store it completely locally. The only time 
the internet is needed is to download the program. Hopefully it helps those that don't trust passwords saved
online to stay protected.

## Known issues: ##
The exe creation isn't working just yet. I plan to return to this and add it once I get done with my current project.

There is an odd bug when generating a password that I can't consistently replicate. It seems to only happen on a 
fresh file of the program, though that might not be the only factor. When first running the password generation, if 
you cancel it before it runs, it has a chance to generate an empty password. Rejecting this empty password and running 
again should fix the issue and I have yet to see it happen with a file that has been used for a while.
