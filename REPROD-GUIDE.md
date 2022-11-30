## Reproducing the experiments for AAAI 2023



**IMPORTANT**: It is essential that your python installation does not have the fimdp module installed, since FiPOMDP uses a modified version of this module that is shipped within it (see the _./fimpd_ folder withint the repo root.) In case you get strange _the provided vector is not a distribution_ exceptions, it is likely caused by the having a wrong fimdp version. In such a case, uninstall the Python version if fimdp by 

```
python3.8 -m pip uninstall fimdp
```


### Setting up your system

The experiments were conducted with python3.8. We recommend setting up a virtual environment to launch FiPOMDP.

#### Installing dependencies

Once a clean virtual environment with python3.8 is created and activated, you can use the requirements.txt file to install the required packages. We recommend using the pip-sync tool from (pip-tools)[https://pypi.org/project/pip-tools/], since should ensure that the packaged version of fimdp is not installed:

```
pip-sync requirements.txt
```

You can also use the standard pip install -r, though make sure to uninstall fimdp afterwards:

```
python3.8 -m pip install -r requirements.txt
python3.8 -m pip uninstall fimdp
```
#### Setting up FiPOMDP

Go to the **```./fipomdp/experiments```** folder, which contains the files needed for experiments.

Open the **```syspath.py```** file and change the path in the file to the location of your FiPOMDPs root directory (the directory containing the **```requirements.txt```** file). Save.

Open the **```threads_macro.py```** file. Change the value of the ```THREADS``` macro to the maximal number of parallel threads you want to enable during the experiments (depending in your HW configuration). Save.

The experiments then can be launched by launching the script

```
./run_aaai23_experiments.sh
```

located in the  **```./fipomdp/experiments```** directory.

(You might need to make it executable by ```chmod +x run_aaai23_experiments.sh```)

After the experiments conclude, the summary statistics can be found in the *STATS.txt files (again in the **```./fipomdp/experiments```** folder).

Note that the experiments might take several hours to complete (or even more, depending on your HW configuration). It is preferable to launch the via nohup to prevent accidental killing of the process:

```
nohup ./run_aaai23_experiments.sh
```

The output (consisting of logging messages) can then be found in the ```nohup.out``` file.

[//]: # (Included are also pickled files with pre-computed min Büchi levels, to reduce preprocessing time.)

## Closer look at the experimental setup

The experiments work in the following manner.
Firstly, the token CoMDP is created and analyzed by computing threshold levels. This is a purely deterministic process and thus it only needs to be performed once per model. The resulting shield can be _pickled_ (stored in a binary file) and loaded for further shielded experiments. This part is not parallelized.

Secondly multiple runs of the POMCP part (shielded or unshielded) are evaluated in parallel. This part is randomized. Each evaluation uses a different seed value, though the seed values are themselves computed deterministically, which makes our experiments reproducible. More precisely, the seed for the first evaluation is 1, and is incremented by 1 with each new evaluation launched.

### Experiment launch files

The shielded POMCP implementation files are located in the **```fipomdp```** folder, while the experiment launch files are in the **```fipomdp/experiments```** folder. Since the benchmarks employ varying rollout functions (e.g., the UUV benchmark uses heavy rollouts described in the paper submission), there needs to be some mechanism for switching between these parameters. Implementing a switch is a work in progress, so now we just use a separate copy of the **```pomcp.py```** file for each experiment. Similarly, each experiment has a separate launch file (a python file whose name contains the _experiment_ keyword) where the hyperparameters are set and from which the individual FiPOMDP runs are launched.

### Loggers
There is a global logger and a logger for each random seed per POMCP evaluation. The global logger is set in the **main** method.
In each experiment file, in method **log_experiment_with_seed**, you can specify the directory where the seeded logs are to be created (one log per seed may take up to 7 MB).
These logs are then used to collect data from the experiments. You can also specify the level of debugging in the main method,
though this is to be done with caution, because debug logs can produce over a GB of data.
Logging level is by default set to INFO.

###### Collecting results
There are two collecting scripts in the directory **fipomdp/experiments** - ***collect_data_script.py***, ***collect_from_sublogs_script.py***.
In case of shielded models, the first one will suffice, but when collecting data with the possibility of the agents death, use ***sublogs_script***. 

***
***collect_data_script***

Takes one parameter, that is the path to the master log (without the ```.log``` suffix).

***collect_from_sublogs_script***

Takes two parameters, first is the path to directory with all sublogs, and second is a default reward to use upon agent's death.

### Hyper-parameters and rollout functions
The top of each experiment file (first 40-60 lines) contains a section for modifying hyper parameters (e.g. exploration, rollout horizon, etc...).
There is also a section for setting the rollout function evaluation (see module ***rollout_functions.py*** in package **fipomdp**)

### Turning off the shield (Work in progress!)
There is currently no parameter for switching of the shield; instead the shield has to be turned off directly in the source code.
To turn the shield off, in package **fipomdp** in file ***energy_solvers.py***, uncomment line 153. Then to reverse it just comment it back. The  ***energy_solvers_unshielded.py*** file contains the uncommented version used in unshielded experiments.
By setting minimal level for each action in each belief support state to theoretical negative infinity (for our experiments where no action cost exceeds 100, minimal level of -1000000 should suffice),
this effectively turns the shield off.

