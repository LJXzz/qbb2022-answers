Exercise 1 and 2 both look great! Just FYI, you can actually run `plink` without creating intermediate `.bed`/`.ped` files. Just doing `plink --vcf <vcf_file? --pca 3` will run PCA on the vcf

Exercise 3: I don't see you're join command in your README, so definitely add that in. Your python code looks good though! One minor thing: For your population figure, it looks like you're repeating certain colors in a row, but I suspect that might be a mistake and not intentional. There are ways to get 26 different colors... maybe look into `sns.color_palette()` as an example?

Really really great work though!
