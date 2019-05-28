# how-to

## Creating a repository locally then uploading to GitHub
### 2019-05-17

Creating a repository locally then uploading to GitHub

 - create a folder with appropriate name
 - open GitBash and navigate into this folder

 > git init

 - create some kind of file or something so it contains something

 > git add <filename>

 > git commit -m '<commit message>'

 - then need to connect it to a remote repository, you have to create the repo either with the desktop app or straight on the website, there's no way to do it from the command line sadly

 > git remote add origin <https://github.com/agosling/<repo name>

 > git push origin master


## Restructuring directories and merging repositories
### 2019-05-28

Done mostly in GitBash as needs the full set of commands.



## First steps into Git use and integration with Atom
###2019-05-16

Guide to get Git working with Atom (from Callum)
https://www.hongkiat.com/blog/manage-git-github-atom/

The master guide - needs additional help thoug
https://flight-manual.atom.io/using-atom/sections/github-package/

If there are issues with the proxy, open Git Bash and type:
git config --global http.proxy http://<username>:<password>@<proxy-server-url>:<port>
https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187


When starting out a new repo, must make the first commit as a detached commit
Once this has been created you can then push that to the repo
This will create the first branch - before that there isn't anything



## pre 2019-05-16

Some potentially useful tutorials I found online:

 - The basic operations of Git, done on a Mac so using the command line but the principle is sound: https://www.youtube.com/watch?v=0fKg7e37bQE
 - Adding an existing directory of code to a repository: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
 - proxy settings: https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187
