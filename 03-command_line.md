# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. grep - search for a string in a file  
2. find - find a file   
3. more - paginate through a file    
4. cat - stream text to stdout  
5. pwd - list current directory  
6. top - list top of a file  
7. man - help page for a command    
8. ps - see what else is running  
9. diff - see what is different between two files
10. sort - sort the file  

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > ls   - list files in the directory  
ls -a  - list all files in the directory, including hidden files  
ls -l  - list the long format, including disk size and last update time  
ls -lh - collapses size to k, mB, gB  
ls -lah - list all files, long format with sizes in k, mB, gB  
ls -t - display files with newest first  
ls -Glp - enables color output, long format, slash after all directories  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -R - recursive directories, helpful for file system grep  
ls -c - by timestamp  
ls -m  
ls -t - always looking for the latest ones  
ls -1 - so much easier to read  

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs takes input from either stdin or piped from another operation and executes a command on the input. It is especially helpful when doing a complex find of files based on criteria and want to move, delete, rename etc those exact files.

find /tmp -name core -type f -print0 | xargs -0 /bin/rm -f

 

