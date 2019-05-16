# how-to


## 2019-05-16
Guide to get Git working with Atom (from Callum)
https://www.hongkiat.com/blog/manage-git-github-atom/

The master guide - needs additional help thoug
https://flight-manual.atom.io/using-atom/sections/github-package/

If there are issues with the proxy, open Git Bash and type:
git config --global http.proxy http://<username>:<password>@<proxy-server-url>:<port>
https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187


Better just to always start a repo on the website and then clone to the comp
However if the stuff already exists, create on line then:
> open GitBash

> navigate to the directory you wish to link to the repo

> git init

> git remote add origin https://github.com/<username>/<repository>.git

> git push -u origin master


When starting out a new repo, must make the first commit as a detached commit
Once this has been created you can then push that to the repo
This will create the first branch - before that there isn't anything



## pre 2019-05-16

Some potentially useful tutorials I found online:

 - The basic operations of Git, done on a Mac so using the command line but the principle is sound: https://www.youtube.com/watch?v=0fKg7e37bQE
 - Adding an existing directory of code to a repository: https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/
 - proxy settings: https://www.freecodecamp.org/forum/t/git-behind-a-proxy-server/13187
