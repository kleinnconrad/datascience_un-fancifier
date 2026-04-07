# Reddit Feedback: Unfancify Data Science

**Source:** [Reddit Post](https://www.reddit.com/r/dataengineering/comments/1se66gi/unfancify_data_science/)

---

## Original Post by /u/Basic-You7791

Some years back - when the term "Data Science" grew big - it became popular to use a GLM, Neural Network or Discriminant function for really every shitty little classification. It was really annoying somehow.
Since the rise of AI aided coding I feel that data science - as it was back then - is pretty dead. So no more guys running around and trying to classify everything small-ish with GLM, Discriminant or Neural Networks to make trivial stuff (and themselves) look more "smart and scientific".
To pick this up I'm? trying to get "back to the roots" and unfancify datascience. I started with a little CLI tool that turns standardized logistic regression functions into "if then else" ruleset
https://github.com/kleinnconrad/datascience\_un-fancifier
What do you think about this? Any suggestions for further "unfancifying"?
submitted by
/u/Basic-You7791
[link]
[comments]

---

### Comment by /u/JohnPaulDavyJones

My brother in Christ, you've recreated the basic outputs from R with extra steps.

---

### Comment by /u/Basic-You7791

I never used R for logistic regression but other tools. They all display statistics like the confusion matrix, p values etc to evaluate the model. But I have never seen that any of them derive conditional rulesets from the logistic regression function (apart from generating a decision tree - what is not meant here).
But I guess R is different then. There is always something new to learn.

---

### Comment by /u/ncist

I actually don't think glm in r will give "plain language" performance metrics like this which is really nice. At least I'm not aware that it does that. Normally I need a second package or calculate them by hand. However that's for good reason- these metrics imply OP optimizes the classifier in the background somewhere. There's no "tn rate" implicit in a logistic regression

---

### Comment by /u/andrew2018022

Posting summary statistics to the terminal stdout-I thought of that. Turned out it already existed, but I arrived at it independently.

---

### Comment by /u/Basic-You7791

Seems like adding the screenshot was strongly misleading. I take it as a learning for the next time. The two confusion matrix have the purpose to show how a "dumb" conditional ruleset performs compared to a logistic regression function.
It's absolutely not about the fact that the tool has the capability to print them out. Ofc that would be incredibly uninteresting.

---

### Comment by /u/Old_Tourist_3774

Not trying to be a prick but there is R and Python modules for that.

---

### Comment by /u/Basic-You7791

Doesn't surprise me. Tbh I didn't research it since I did not thought to "invent something entirely new" but to bring up an interesting starting point.
Thanks for pointing it though!

---

### Comment by /u/Willing_Box_752

I thought you wrote "uncify"
Like, to make it unc

---

### Comment by /u/Academic-Vegetable-1

Half of what got called "data science" was always just GROUP BY with extra steps.

---

### Comment by /u/Basic-You7791

Can't argue about that!

---

