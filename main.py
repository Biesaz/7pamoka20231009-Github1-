# :q - iseiti i terminala
# ls -a - parodo pasleptas direktorijas
########################################################################
# git status                          Raudona -   pakeitimai
# git add .                                   -   start tracking all files
# git status                          Zalia   -   start tracking all files
# git commit -m "renaiming dir"       Balta   -   sukurti commit'ą , kuris yra tiesiog projekto istorijos taškas, rodantis, kas buvo pakeista, kas ir kada tai padarė.
# git push <repo name> <branch name>          -   siųsti(pushinti) (git push origin staging (cia apie Cafeteria2024))
# git pull                                    -   nurodo git "pullinti" naujausius pakeitimus iš remote (github)
# rm -rf .git                                  - iseiti is (main) brancho
# git init
# git branch -M main
# git checkout -b staging                      - to create a new branch ("staging")


# Lesson 7: Git Github (Part 1)
# Version control systems (git, GitLab, GitHub, bitbucket...)

######################################################## # Setting up git 🧰

# open git bash if you are using windows or any terminal on other OS:

# 1.Setup your name:
# git config --global user.name "name surname"
# 2.setup email:
# git config --global user.email full@email.com
# 3.Check settings:
# git config --list

# Connecting with ssh key. Open git bash terminal
# generate ssh key:
# ssh-keygen -t rsa -b 4096 -C "email@email.com"
# open file id_rsa.pub with any text editor and copy it.
# Go to www.github.com on top right click on your profile -> settings -> SSH and GPG keys -> New SSH key. 
# Give the key a name of your choice and paste the key. Click Add SSH Key

######################################################### # Creating an empty project? 📃
# Open www.github.com Login and hit Start a project. Give it a name and click create repository

# How to start working with git?
# There are couple of ways to move from here and immediately github will describe opportunities to you if you open your newly created project.

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ first scenario Kai susikuri repo GitHube @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# open up terminal:
################# git clone repository (klonuoti saugyklą)
# create a file and check what can git say about the file:
# git status
# tell git to start tracking changes within the file:
# git add <filename>
# check status once again git status
# What is different this time? Now we need to create a commit, which is simply a point in history of your project showing what was changed and who and when did the change. Let's create it!
# git commit -m "first commit"
# check status once again git status
# We are ready to push now:
# git push
# congratulations you have now successfully tracked the changes and they are also visible on gitub! Check them out.

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ Second scenario @@@@@@@@@@@@@@@@@@@@@ KAi pirma susikuri folder(projekta) lokaliai
# What if you already had a codebase and now suddenly you want to start tracking it? Not a problem. initiate git project in the directory of your choice.

######################## @1@. git init #################### (Initialized empty Git repository in F:/VygaPytons/CodeAcademy/20240307-Testing-/.git/)
# now you can check git status once again:
# git status    (On branch master   No commits yet  Untracked files:) Raudona
# to start tracking all files simply:
# @2@. git add . 
# git status    (On branch master   No commits yet  Changes to be committed:)   Zalia    
# @3@. git commit -m "initial commit"

# And just like that you now have a repo that is being tracked. But how do we share this with our colleagues? 
# It is not yet connected to GitHub So for this project @4@.create a new GitHubproject. 
# Now all you have to do is to grab origin link which you can find on GitHub project you have created.

################################# @5@. git remote add origin pvz: https://github.com/vychiokas/test.git
# now we have to 'push' it to remote:
# @6@. git push -u origin master(main)

# Start working on existing project
# So far we've seen how to create a project but how do we join an already existing one? it's simple go to projects github page. 
# Click on green button saying Code choose the way you want to acquire a copy -> ssh/ hhtp open up the terminal, go to the place where you want to clone the project and then clone it:
############################################## git clone <link_to_project>
# Now you have acquired a copy of codebase to your computer. Be careful, because it does nto update automatically, to grab latest changes we need to do:
############################################### git pull
# this simply tells git to 'pull' latest changes from remote(github), note that the command is similar to git push but does the exact opposite - it updates the local copy of codebase.

########################################### .gitignore
# Sometimes there are files that we do not want to be tracked - files with credential information, data, huge files etc... 
# Git is only supposed to track changes in code, not to expose your passwords to the world.
# so in the root directory of your project you may add file called .gitignore and in the file you may list files/ folders/ patterns of 
# the files that you do not want to track, and git will not even show the changes or those files at all in git status. Try it yourself!

# ####################################### Readme.md 📑
# This is the frontpage information on your project, the main document visitor sees when visiting your project, 
# usually it is quite clear from this one if even the owner of the project cares about it, because we usually want more 
# people to be interested and spread good word about our work. Please feel free to add explanations about your project here, 
# how to launch it, what is it all about. Why did you even create it etc... There is also a whole syntax of how to write these pages, 
# more info in the additional links at the end of the lesson.

# 🧠 Exercises:
# 1.
# Create the project that you are going to use for our lessons, add already existing notes in order not to lose them.
# Go once again through todays lecture on your own, if anything is not clear - let us know