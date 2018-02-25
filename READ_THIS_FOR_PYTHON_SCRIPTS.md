This text file has instructions on how to run the two python scripts found in
this repository.

DOWNLOADING DATA----------------------------------------------------------------

To download all of the data, first make sure you have the scripts downloaded.
Then, when you're in the directory with the scripts, type

`python3 save_chart_as_json.py project_data`

This will start the script; nothing else needs to be done for
downloading. Just let your computer sit there and finish up. If you press CTRL+C
when the script is running, this will interrupt and halt the downloads (so do
this if you need to go somewhere). If the file already existed before you did
this, the script will go ahead and delete the halfway downloaded file so that
when you run the script again it doesn't re-append old data. If the file didn't
exist already, then you're good to just run the script again.

The script, if the file name you give it isn't one that exists yet, will create
that file when it tries to write the .json information, so don't worry about
having to create the file before you run the script. If it exists, it'll use it;
if it doesn't exist, it'll make it.

VERIFYING DATA------------------------------------------------------------------

To verify the datafile when you're done, you'll need to read the .json file.
However, simply typing `less project_data.json` will present you with unreadable
formatting for the file, making it really quite difficult to discern what is
going on. There's another script in the file, titled "print_json.py", which will
print out the file in a much more readable format.

To run this script, type

`python3 print_json.py project_data`

This will run the printing script, which will use some python
modules to print out the verified files to make it more readable. You
shouldn't need to scan the ENTIRE thing, but you will just need to scan parts of
it to make sure it actually did download all of the data needed. It will raise
(and handle) errors relating to bad I/O (file not existing, file unable to be
read as .json, etc), so if an error is raised, just make sure the file actually
is usable. It's nicer to read my error messages than it is trying to read the
full stack trace given to you by the python native exception handler :)

If you have any more questions, or just want to know how the scripts themselves
actually work, just let me know! I can explain the code and everything behind it
if you're curious in how both scripts do what they do.
