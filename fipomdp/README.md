# FiPOMDP - Fuel in Partially Observable Markov Decision Processes

##### Python package for synthesizing resource-safe strategies on Resource-constrained POMDPs
FiPOMDP is a tool for solving Consumption POMDPs (CoPOMDPs) with a combination of qualitative and quantitative objectives. The key functionality provided:
* Synthesizing a shield (device disabling unsafe actions) against resource-safety and almost-sure reachability specifications.
* Performing shielded planning w.r.t. minimum-cost reachability performance criterion. That is, the planning algorithm minimizes the expected cost of reaching a goal while formally ensuring that the goal is eventually reached with probability one and that the resource is never exhausted. This is done by applying the shield to the [POMCP](https://papers.nips.cc/paper/2010/hash/edfbe1afcf9246bb0d40eb4d8027d90f-Abstract.html) planning algorithm. 

This project extends the [FiMDP] tool for qualitative synthesis in Consumption MDPs. Necessary libraries of the tool are included in this repository. 

The shielding itself is done by reducing the qualitative analysis of a Consumption POMDPs to a problem of solving Token Consumption MDPs with qualitative objectives (more details in the submission for AAAI 2023). In particular, we use the [FiMDP] libraries for computing the threshold resource levels. 
FiPOMDP itself implements the Token CoMDP construction, extraction of a shield from the threshold levels, and shielded POMCP planning (with a custom POMCP implementation).

## Installation (regarding experiments)
See the [Experiment reproducibility guide].

## Demo (Work in progress)
The directory fipomdp/demo includes a demo notebook showing how to create a simple CoPOMDP and create a shield via qualitative analysis.
For more information about FiMDP, creating perfectly observable Consumption MDPs, look at [FiMDP README].

## Experiments for AAAI 2023
The experiments we performed use environments from the [FiMDPEnv] library modified to include an aspect of partial observability. A small tutorial how to launch them and collect results from them is included. The experiments from the AAAI'23 submission can be reproduced with the help of the [Experiment reproducibility guide].



[FiMDPEnv]: https://github.com/FiMDP/FiMDPEnv
[FiMDP]: https://github.com/FiMDP/FiMDP
[FiMDP README]: https://github.com/xbrlej/FiPOMDP/blob/master/FiMDP-README.md
[Experiment reproducibility guide]: ./REPROD-GUIDE.md
