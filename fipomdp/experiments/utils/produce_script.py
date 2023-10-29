

filenames = [("UUV_experiment_8_heavy", "logs_8_heavy", "UUVExperimentsFromPythonFile_8_heavy", "-100"),
             ("UUV_experiment_12_heavy", "logs_12_heavy", "UUVExperimentsFromPythonFile_12_heavy", "-100"),
             ("UUV_experiment_16_heavy", "logs_16_heavy", "UUVExperimentsFromPythonFile_16_heavy", "-100"),
             ("UUV_experiment_20_sparse_heavy", "logs_20_sparse_heavy", "UUVExperimentsFromPythonFile_20_sparse_heavy", "-100"),
             ("UUV_experiment_8_heavy_unshielded", "logs_8_heavy_unshielded", "UUVExperimentsFromPythonFile_8_heavy_unshielded", "-100"),
             ("UUV_experiment_12_heavy_unshielded", "logs_12_heavy_unshielded", "UUVExperimentsFromPythonFile_12_heavy_unshielded", "-100"),
             ("UUV_experiment_16_heavy_unshielded", "logs_16_heavy_unshielded", "UUVExperimentsFromPythonFile_16_heavy_unshielded", "-100"),
             ("UUV_experiment_20_sparse_heavy_unshielded", "logs_20_sparse_heavy_unshielded", "UUVExperimentsFromPythonFile_20_sparse_heavy_unshielded", "-100"),
             ("tiger_experiment", "logs_tiger", "TigerExperiments", "-500"),
             ("tiger_experiment_unshielded", "logs_tiger_unshielded", "TigerExperiments_unshielded", "-500"),
             ("tiger_experiment_fuzzy", "logs_tiger_fuzzy", "TigerExperimentsFuzzy", "-500"),
             ("tiger_experiment_fuzzy_unshielded", "logs_tiger_fuzzy_unshielded", "TigerExperimentsFuzzy_unshielded", "-500"),
             ("NYC_experiment", "logs_NYC", "NYCExperiments", "-5000"),
             ("NYC_experiment_unshielded", "logs_NYC_unshielded", "NYCExperiments_unshielded", "-5000")]


file = open("script", "w")

file.write("#!/bin/bash\n\n")

for exp in filenames:
    file.write("if [ -d \"./" + exp[1] + "\" ]\n")
    file.write("then\n")
    file.write("    rm -r ./" + exp[1] + "\n")
    file.write("    rm " + exp[2] + "\n")
    file.write("fi" + "\n")
    file.write("mkdir " + exp[1] + "\n")
    file.write("python3.8 ./" + exp[0] + ".py\n")
    file.write("\n")

file.write("\n\n")

for exp in filenames:
    if exp[0].find("unshielded") == -1:
        file.write("python3.8 collect_data_script.py " + exp[2] + "\n")
    else:
        file.write("python3.8 collect_from_sublogs_script.py " + exp[1] + " " + exp[3] + "\n")

file.close()