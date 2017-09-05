# idark-ml
Machine Learning is great fun.


## Setup git so it plays nice with Jupyter notebooks
The Jupyter notebooks are modified everytime they are run, even when nothing is really changed.
This makes them very noisy in version control. 
We fix that by preprocessing the notebooks before git sees them. 
This is based on the excellent [guide by Tim Staley](http://timstaley.co.uk/posts/making-git-and-jupyter-notebooks-play-nice/).
We use the program [jq >1.5](https://stedolan.github.io/jq/), the equivalent of sed for json, 
to modify the notebook files, and automate its use by [gitattribute](https://git-scm.com/docs/gitattributes) 
filters. 
The only difference from Tim Staley's setup is that we do not remove the output as we want to distribute plots and the like.

**In summary**, install jq and add this snippet to your local .git/config

~~~~
[filter "nbstrip_jq"]
        clean = "jq --indent 1 \
        '(.cells[] | select(has(\"execution_count\")) | .execution_count) = null  \
        | .metadata = {\"language_info\": {\"name\": \"python\", \"pygments_lexer\": \"ipython3\"}} \
        | .cells[].metadata = {} \
        '"
        smudge = cat
~~~~

