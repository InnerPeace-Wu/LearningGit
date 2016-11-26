1. mkdir dirname
   cd dirname
   pwd #show the current path
   git init  #initialize
2. git add file.txt #add several files the same time
3. git commit -m"write a comment"
4. git status #show the current status
5. git diff #show the last time submit difference
6. git log #logs of change've been made
   git log --pretty=oneline  #simplify the output
7. git reset --hard HEAD^  #HEAD^^ HEAD~100
   git reset --hard ID  #cat readme.txt
8. git reflog #show all the commit ID
9. git diff HEAD -- file.txt  #difference between work space and respositry
10. git checkout -- file  #discarding the change
    git reset HEAD file #same as the above
11. git rm file #delete the file
    git checkout -- file #undo delete
12. ssh-keygen -t rsa -C "youremail@example.com"
    #copy file id_rsa.pub to SSH in github
13. #Create a new repo with the same name with local dir
    git remote add origin git@github.com:name/dirname.git
14. git push -u origin master #parameter -u for the new repository
    git push origin master
15. #already got a repository online and clone it to local
    git clone git@github.com:name/dirname.git
16. #when changed ur repo name online, update it as below
    git remote add new_origin [updated link
    git remote rm origin
    git remote rename new_origin origin
    #easier way
    git remote set-url origin [updated link
17. #switch to a new branch
    git checkout -b dev#branch name
    git branch dev
    git checkout dev
18. git branch #show all the branches
19. cat filename #to show the file
20. git diff HEAD -- filename.txt #after add the file then check the diff
21. git merge <name> #the merge a branch with master one
22. git branch -d <name> #to delete a branch
23. git log --graph --pretty=oneline --abbrev-commit #merge map
24. git merge --no-ff -m"write a commit" branchname #merge with no-ff AKA
                                                    #fast forward
