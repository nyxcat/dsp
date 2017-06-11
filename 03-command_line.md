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

> > pwd: show current working directory
    mkdir: create a directory
    rmdir: delete a directory
    touch: create a file using 'touch' command
    rm: delete a file
    mv: rename a file
    ls -a: list hidden files
    cp: copy a file from one directory to another
    cat: print the whole file
    find: find files
    echo: print some arguments
    cd: change directory
    
    

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

> > ls: list directory

ls -a: display all files
    
ls -l: display the long format listing
    
ls -lh: display the files with human readable sizes in long format
    
ls -lah: display all the files with human readable sizes in long format
    
ls -t: display the files from newest to oldest
    
ls -Glp: display file list with different colors for different file types, show long formating listing and dispaly directories with /.

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -a: display all files
    ls -t: display files from newest to oldest
    ls -u: display files by the file access time
    ls -r: display files in reverse order
    ls -l: display long formating list

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 'xargs' exacutes arguments. For example, if I want to print multiple words with two words in a line, I can do as follwoing.
$ echo "hello world hello world" | xargs -n2
Then I will get:
hello world
hello world


 

