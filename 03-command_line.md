# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > 
* show current working directory path - pwd
* creating a directory - mkdir directory name
* deleting a directory - rmdir directory name
* creating a file using `touch` command - touch filename
* deleting a file - rm filename
* renaming a file - mv oldname newname
* listing hidden files ls -a
* copying a file from one directory to another - cp source target
* View a file - less filename
* Looking inside files - grep word_to_be_found in_which_files(eg. *.txt)

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
`ls`     - displays files in current directory
`ls -a`  - Lists hidden files also. If a file or directory name starts with a dot, it is referred to as hidden.
`ls -l`  - Displays long listing with detailed file information including file type, permissions, link count, owner, group, s       ize, date and time
`ls -lh` - displays long listing with file sizes in human readable format 
`ls -lah`- displays the following information for a file:
           file permissions, number of links, owner name, owner group, file size, time of last modification, and file/directory name
`ls -t`  - lists all files sorted by date and time with the newest file first
`ls -Glp`- displays long listing of files, does not display group information, appends file type indicator (one of /=@|) to entries  

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -c	Displays files by file timestamp.
    ls -d	Displays only directories.
    ls -r	Displays files in reverse order.
    ls -R	Displays subdirectories as well.
    ls -u	Displays files by the file access time.
    ls -1	Displays each entry on a line.
    
---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
The xargs command takes in a standard input and will split up the standard input so that it can be passed to utlities that may otherwise not be able to take such long inputs. Additionally, some utilities do not accept standard inputs and instead the input is required to be spelled out (for example: rm, touch, cp, etc.). xargs, when used with these utilities will take an input and split the input into individual arguments that can then be passed into these utilities.

The below example searches in the current directory (and other subdirectories) for files ending in .txt and removes these files.
$ find . -name "*.txt" -print0 | xargs -0 rm -rf
 

