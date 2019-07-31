# How-To GitHub guide - all my own learning

### First steps into Git use and integration with Atom

**If there is something that you'd like to see in this how-to, then raise and issue against the repository(use the `Issue` button above to submit a request.)**

Guide to get Git working with Atom (from Callum)
https://www.hongkiat.com/blog/manage-git-github-atom/

The master guide - needs additional help though
https://flight-manual.atom.io/using-atom/sections/github-package/

If there are issues with the proxy, open Git Bash and type:
git config --global http.proxy http://<username>:<password>@<proxy-server-url>:<port>
https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187




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

> git config --global user.email "you@example.com"  
> git config --global user.name "Your Name"


### Restructuring directories and merging repositories

Done mostly in GitBash as needs the full set of commands.

Did it but need to recover the sources and summarise my steps.

## A few subtle markdown tips

 - If you want a single line break, place two spaces at the end of a line

# pre 2019-05-16

Some potentially useful tutorials I found online:

 - The basic operations of Git, done on a Mac so using the command line but the principle is sound: https://www.youtube.com/watch?v=0fKg7e37bQE
 - Adding an existing directory of code to a repository: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
 - proxy settings: https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187
