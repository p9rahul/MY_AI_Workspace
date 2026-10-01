#Lists all branches, including both "local branches" and those tracked on 'remote repositories" (like GitHub).
git branch -a

#Lists all local branches
git branch

#Only switch
git switch <Branch_name>

#Create and switch
git switch -c <branch-name>
git checkout -b <branch-name>

#git branch <branch-name>
Creates a new branch with the specified name based on your current location. Note: This "does not switch" your active workspace to the new branch.

#git branch -m <new-name> Renames the current active branch

#To see details like the latest commit message and how your local branches compare to the remote repository, use the verbose flag
main abfd06f [origin/main] Initial commit
master 64d9784 [origin/master] RAG code

#Delete branch
git branch -d <branch-name> -Deletes a branch safely.Git will block deletion if the branch contains unmerged work.

git branch -D <branch-name> Forces deletion of a branch, even if it contains unmerged changes.

================================================
$ git clone - Downloads a full copy of a remote repository into a brand-new local folder.
When you start working on a project for the first time. Yes (Runs in an empty or new folder).

$git fetch Downloads metadata and commits from the remote repo into your hidden local .git directory. It does not touch your current files. When you want to review what your team did before integrating their changes. Yes (Zero risk of overriding your work or causing conflicts).

$git pull Downloads changes AND integrates them immediately into your active branch. When your workspace is clean and you want to instantly sync up with the team. No (Can trigger immediate merge conflicts if you have uncommitted changes).
