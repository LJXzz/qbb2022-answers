Question 1: It looks like the fix you did (adding `-v` to `awk`) worked! There was one more fix that you should have had to make, which was removing the `$` from the `for $nuc in A C G T`, but given that you have the right output, I'm guessing you did. Just remember to comment all of your changes.

Question 2: I might have named your output bed file `promoters.bed` rather than `genes.bed` as I think it's probably a little bit more accurate about what's in the file, but your `awk` command looks really good!

Question 3: Interesting work around using perl to add tabs in the `variants.bed`! We can actually doing that in awk by changing the OFS (output field separator). But I like the ingenuity!

Great work!
