Question 3b: This is one way to do it! You could also do `cut -f 4 | sort -n | uniq -c` which will tell you how many times you saw each state
Question 5b: You can actually shorten the cut command to `cut -f 1-9,13` but this will also work!
Question 5d: What command did you use for this?
Question 5e: I think you need another cut command before you do `cut -d ';' -f 7`. We first need to isolate the INFO field before we can cut within it

Nice work!
