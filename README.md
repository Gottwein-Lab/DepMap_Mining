# DepMap_Mining
Code for identifying cohort-specific oncogenic dependencies and cohort-insensitive pan-essentials using DepMap + a cohort of CRISPR screens analyzed with MAGeCk.

Main analysis is in the Juypter Notebook. R script (for the log-likelihood ratio testing) is taken from [P. Montgomery](https://forum.depmap.org/t/normlrt-code-availability/436/5) of the DepMap Consortium, [available on GitHub](https://gist.github.com/pgm/92bf5b9e3c80187da1ed14618abc4dc9). I've included my results here.

Note: some of the NormLRT values returned are probably erroneous, likely related to bad/failed MLE when estimating skewed t-dist parameters, but I haven't gotten around to examining the DepMap R code closely enough to fix this. The R script is run in my Notebook indirectly via Python/rpy2. If the pre-calculated LRT (available in this repo) file is included, the notebook will use that instead as estimating parameters for ~18k genes is slow.

DepMap data should be downloaded from the [DepMap data portal](https://depmap.org/portal/download/all/).

You will want:
* CRISPR_gene_effect.csv
* CRISPR_common_essentials.csv
* Achilles_gene_effect.csv
* Achilles_common_essentials.csv

I included DepMap_Selective_Genes.csv which is derived from the relevant column of the table available for [here](https://depmap.org/portal/api/download/gene_dep_summary) (link directly initiates download), targeting only the combined dataset rows.
