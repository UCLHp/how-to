# How-To GitHub guide - all my own learning

### First steps into Git use and integration with Atom

**If there is something that you'd like to see in this how-to, then raise and issue against the repository(use the `Issue` button above to submit a request.)**

Guide to get Git working with Atom (from Callum)
https://www.hongkiat.com/blog/manage-git-github-atom/

  

The master guide - needs additional help though
https://flight-manual.atom.io/using-atom/sections/github-package/

  

If there are issues with the proxy, open Git Bash and type:
```console
git config --global http.proxy http://<username>:<password>@<proxy-server-url>:<port>
```
https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187

N.B. The UCLH proxy address is http://[uclh_username]:[uclh_pwd]@www-cache-n:3128

To determine the IP address for the proxy, you can ping www-cache-n and use that explicitly as sometimes the DNS doesn't convert the address when using this as a workaround.




### Creating a repository locally then uploading to GitHub

Creating a repository locally then uploading to GitHub

 - create a folder with appropriate name
 - open GitBash and navigate into this folder

> git init

 - create some kind of file or something so it contains something

> git add [filename]  
> git commit -m ' [commit message] '

 - then need to connect it to a remote repository, you have to create the repo either with the desktop app or straight on the website, there's no way to do it from the command line sadly

> git remote add origin https://github.com/agosling/[repo-name]  
> git push origin master


### Renaming a branch and updating locally and remotely

 - source:  https://www.w3docs.com/snippets/git/how-to-rename-git-local-and-remote-branches.html

Rename your local branch.
 - If you are on the branch you want to rename:

> git branch -m new-name

 - Or if you are on a different branch:

> git branch -m old-name new-name

Delete the old-name remote branch and push the new-name local branch.
> git push origin :old-name new-name

Reset the upstream branch for the new-name local branch.
Switch to the branch and then:

> git push origin -u new-name



### Stopping tracking of filetypes

source:  https://docs.microsoft.com/en-us/azure/devops/repos/git/ignore-files?view=azure-devops&tabs=visual-studio

 - Navigate to the directory of the repo
 - Create a `.gitignore` file if not already present.  Add the file type to the `.gitignore` file in the format `*.tif` or similar (`*` is a wildcard to indicate any filename).
 - In GitBash run the following command to remove existing tracking of that filetype (do not include the [ ] around the filetype/filenames)

> git rm --cached [filetype/filename]

 - Make a commit to log the change

### Setting git username and password globally so that Atom recognises it:

source:  https://github.com/atom/github/issues/932

set it in terminal/powershell/cmd:

> git config --global user.email \"you@example.com\"  
> git config --global user.name "Your Name"



### Removing a branch

source:  https://koukia.ca/delete-a-local-and-a-remote-git-branch-61df0b10d323

remove a branch locally:

> git branch -d [branch name]

remove a remote branch:

> git push [remote name] --delete [branch name]

## Some extra commands shamelessly stolen from an "sdc" presentation
### Source and credit is Haroon Chughtai:  2019-03-01

##### Set Up Your Details
> git config --global user.name "Haroon Chughtai"  
> git config --global user.email "h.chughtai@nhs.net"

##### Configure Line Endings
> git config --global core.autocrlf input # macOS & Linux  
> git config --global core.autocrlf true # Windows

##### Choose an Editor
> git config --global core.editor "nano -w"

##### Set Up Proxy
> git config --global http.proxy proxy-url  
> git config --global https.proxy proxy-url  

N.B. The UCLH proxy address is http://[uclh_username]:[uclh_pwd]@www-cache-n:3128

To determine the IP address for the proxy, you can ping www-cache-n and use that explicitly as sometimes the DNS doesn't convert the address when using this as a workaround.

##### Tracking Changes
> git add [filename]  
> git commit -m "Reason for change"

##### Exploring History
Compare with previous versions of a file
> git diff HEAD [filename] # the last commit  
> git diff HEAD~1 [filename] # the commit 1 behind the last commit  
> git diff [commit_id] [filename] # a specific commit  

Restore a previous version of a file to the working directory
> git checkout HEAD [filename]  

Detaches head and should be used as a read-only view
> git checkout [commit_id]  

Reattaches head and puts repo back into a safe state
> git checkout master  

##### Remotes
> git remote add origin [remote repository address]  
> git push origin master

##### Collaborating
get someone’s repo
> git clone [someone's repo] [your local file path]

to get changes
> git pull origin master

to make changes
> git add [file]
> git commit -m "meaningful comment"
> git push origin master

> git pull = git fetch + git merge

##### Resource List
What this talk was based on:  http://swcarpentry.github.io/git-novice/  
Some notes that I like:  https://www.atlassian.com/git/tutorials  
An amazing reference:  https://github.com/k88hudson/git-flight-rules  
An interactive git tutorial app:  https://github.com/jlord/git-it-electron  
An interactive git branching tutorial:  https://learngitbranching.js.org/  
Lots of posts by devs at different career stages:  https://dev.to/search?q=Git







## A few subtle markdown tips

 - If you want a single line break, place two spaces at the end of a line
