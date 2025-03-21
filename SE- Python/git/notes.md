# Version Control 
is creating safe points that save your project , this let's you have the freedom to change absloutely anything about.
- Centeralized 
- Distriputed : every one take a copy on his computer  and work on it and eg of it git.

### git hub:
- is the service that hosts git projects


Commit
Git thinks of its data like a set of snapshots of a mini filesystem. Every time you commit (save the state of your project in Git), it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. You can think of it as a save point in a game - it saves your project's files and any information about them.

Everything you do in Git is to help you make commits, so a commit is the fundamental unit in Git.

Repository / repo
A repository is a directory which contains your project work, as well as a few files (hidden by default on Mac OS X) which are used to communicate with Git. Repositories can exist either locally on your computer or as a remote copy on another computer. A repository is made up of commits.

Working Directory
The Working Directory is the files that you see in your computer's file system. When you open your project files up on a code editor, you're working with files in the Working Directory.

This is in contrast to the files that have been saved (in commits!) in the repository.

When working with Git, the Working Directory is also different from the command line's concept of the current working directory which is the directory that your shell is "looking at" right now.

Checkout
A checkout is when content in the repository has been copied to the Working Directory.

Staging Area / Staging Index / Index
A file in the Git directory that stores information about what will go into your next commit. You can think of the staging area as a prep table where Git will take the next commit. Files on the Staging Index are poised to be added to the repository.

SHA
A SHA is basically an ID number for each commit. Here's what a commit's SHA might look like: e2adf8ae3e2e4ed40add75cc44cf9d0a869afeb6.

It is a 40-character string composed of characters (0–9 and a–f) and calculated based on the contents of a file or directory structure in Git. "SHA" is shorthand for "Secure Hash Algorithm". If you're interested in learning about hashes, check out our Intro to Computer Science course.

Branch
A branch is when a new line of development is created that diverges from the main line of development. This alternative line of development can continue without altering the main line.

Going back to the example of save point in a game, you can think of a branch as where you make a save point in your game and then decide to try out a risky move in the game. If the risky move doesn't pan out, then you can just go back to the save point. The key thing that makes branches incredibly powerful is that you can make save points on one branch, and then switch to a different branch and make save points there, too.

With this terminology in mind, let's take a high-level look at how we'll be using Git by looking at the typical workflow when working with version control.



# sets up Git with your name
git config --global user.name "<Your-Full-Name>"

# sets up Git with your email
git config --global user.email "<your-email-address>"

# makes sure that Git output is colored
git config --global color.ui auto

# displays the original state in a conflict
git config --global merge.conflictstyle diff3

git config --list



### Git init 
create new repos in your computer 
The init subcommand is short for "initialize", which is helpful because it's the command that will do all of the initial setup of a repository. We'll look at what it does in just a second.
Running the git init command sets up all of the necessary files and directories that Git will use to keep track of everything. All of these files are stored in a directory called .git (notice the . at the beginning - that means it'll be a hidden directory on Mac/Linux). This .git directory is the "repo"! This is where git records all of the commits and keeps track of everything!

Let's take a brief look at the contents of the .git directory.


### Git Clone 
copy existing repos from somewhere else to your local computer
### git status 
to check the status of your repo
eg . 
You can see that git status tells us that there's "nothing to commit, working directory clean". That means we're good to go ahead and check out the project!



### git logs 
is about the history of your extsting commits , it's something like the journaling when you wrtie the date and where did you go?
git log --oneline
git log --stat
git log -p   short of patch
to scroll down, press
j or ↓ to move down one line at a time
d to move by half the page screen
f to move by a whole page screen
to scroll up, press
k or ↑ to move up one line at a time
u to move by half the page screen
b to move by a whole page screen
press q to quit out of the log (returns to the regular command prompt)


### git show 
display info about specific commit
git show fdf5493


### git add git commit git diff

## Git Ignore
If you want to keep a file in your project's directory structure but make sure it isn't accidentally committed to the project, you can use the specially named file, .gitignore (note the dot at the front, it's important!). Add this file to your project in the same directory that the hidden .git directory is located. All you have to do is list the names of files that you want Git to ignore (not track) and it will ignore them.

Let's try it with the "project.docx" file. Add the following line inside the .gitignore file:

project.docx
Now run git status and check its output:



### git tag 
is about adding tags to my commit
### git branch is about creating brancing
Change 2 - Add Sidebar
Let's add a sidebar to the page. But let's say that we're not really sure if we like the new background color. So we'll place the sidebar branch on the commit before the one that sets the page's color. Your SHAs will be different, but, for me, the commit that's before the one that adds the color has a SHA of 5bfe5e7. So adding the branch to that commit would look like:

$ git branch sidebar 5bfe5e7


### git commit --amend 
you can alter commits 
If your Working Directory is clean (meaning there aren't any uncommitted changes in the repository), then running git commit --amend will let you provide a new commit message. Your code editor will open up and display the original commit message. Just fix a misspelling or completely reword it! Then save it and close the editor to lock in the new commit message.



### git revert 
reverses gitting commit 
The git revert Command
Now that I've made a commit with some changes, I can revert it with the git revert command

$ git revert <SHA-of-commit-to-revert>
Since the SHA of the most-recent commit is db7e87a, to revert it:
I'll just run git revert db7e87a (this will pop open my code editor to edit/accept the provided commit message)

I'll get the following output:


#### git resset 
erase commits
⚠️ Resetting Is Dangerous ⚠️
You've got to be careful with Git's resetting capabilities. This is one of the few commands that lets you erase commits from the repository. If a commit is no longer in the repository, then its content is gone.

To alleviate the stress a bit, Git does keep track of everything for about 30 days before it completely erases anything. To access this content, you'll need to use the git reflog command. Check out these links for more info:

### git checkout is switching  between branches 

git combine changes in different branches


### Git Tag Command
Pay attention to what's shown (just the SHA and the commit message)

The command we'll be using to interact with the repository's tags is the git tag command:

$ git tag -a v1.0

git log

Adding A Tag To A Past Commit
Running git tag -a v1.0 will tag the most recent commit. But what if you wanted to tag a commit that occurred farther back in the repo's history?

All you have to do is provide the SHA of the commit you want to tag!

$ git tag -a v1.0 a87984



