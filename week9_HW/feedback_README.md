Great work Jiaxin!

1. Your labels for the dendrogram and heatmap are a bit funky. I think when you use the `labels` argument in the dendrogram function, it automatically rearranges the labels, so you don't actually have to do that on your end (no points deducted)
2. I think when you run your regression and when you're looing at overlaps in the genes between the two different models, you're mistakenly using the `row_names` variable which contains the transcript names BEFORE filtering, which is not correct. After the filtering step, we are only working with the filtered trancripts. This may help explain why your overlap is so low between the two models. (-0.25)

Everything else looks great!

(9.75/10)
