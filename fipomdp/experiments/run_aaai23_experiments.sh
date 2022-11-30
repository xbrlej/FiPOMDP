#!/bin/bash

if [ -d "./logs_8_heavy" ]
then
    rm -r ./logs_8_heavy
    rm UUVExperimentsFromPythonFile_8_heavy
fi
mkdir logs_8_heavy
python3.8 ./UUV_experiment_8_heavy.py

if [ -d "./logs_12_heavy" ]
then
    rm -r ./logs_12_heavy
    rm UUVExperimentsFromPythonFile_12_heavy
fi
mkdir logs_12_heavy
python3.8 ./UUV_experiment_12_heavy.py

if [ -d "./logs_16_heavy" ]
then
    rm -r ./logs_16_heavy
    rm UUVExperimentsFromPythonFile_16_heavy
fi
mkdir logs_16_heavy
python3.8 ./UUV_experiment_16_heavy.py

if [ -d "./logs_20_sparse_heavy" ]
then
    rm -r ./logs_20_sparse_heavy
    rm UUVExperimentsFromPythonFile_20_sparse_heavy
fi
mkdir logs_20_sparse_heavy
python3.8 ./UUV_experiment_20_sparse_heavy.py

if [ -d "./logs_8_heavy_unshielded" ]
then
    rm -r ./logs_8_heavy_unshielded
    rm UUVExperimentsFromPythonFile_8_heavy_unshielded
fi
mkdir logs_8_heavy_unshielded
python3.8 ./UUV_experiment_8_heavy_unshielded.py

if [ -d "./logs_12_heavy_unshielded" ]
then
    rm -r ./logs_12_heavy_unshielded
    rm UUVExperimentsFromPythonFile_12_heavy_unshielded
fi
mkdir logs_12_heavy_unshielded
python3.8 ./UUV_experiment_12_heavy_unshielded.py

if [ -d "./logs_16_heavy_unshielded" ]
then
    rm -r ./logs_16_heavy_unshielded
    rm UUVExperimentsFromPythonFile_16_heavy_unshielded
fi
mkdir logs_16_heavy_unshielded
python3.8 ./UUV_experiment_16_heavy_unshielded.py

if [ -d "./logs_20_sparse_heavy_unshielded" ]
then
    rm -r ./logs_20_sparse_heavy_unshielded
    rm UUVExperimentsFromPythonFile_20_sparse_heavy_unshielded
fi
mkdir logs_20_sparse_heavy_unshielded
python3.8 ./UUV_experiment_20_sparse_heavy_unshielded.py

if [ -d "./logs_tiger" ]
then
    rm -r ./logs_tiger
    rm TigerExperiments
fi
mkdir logs_tiger
python3.8 ./tiger_experiment.py

if [ -d "./logs_tiger_unshielded" ]
then
    rm -r ./logs_tiger_unshielded
    rm TigerExperiments_unshielded
fi
mkdir logs_tiger_unshielded
python3.8 ./tiger_experiment_unshielded.py

if [ -d "./logs_tiger_fuzzy" ]
then
    rm -r ./logs_tiger_fuzzy
    rm TigerExperimentsFuzzy
fi
mkdir logs_tiger_fuzzy
python3.8 ./tiger_experiment_fuzzy.py

if [ -d "./logs_tiger_fuzzy_unshielded" ]
then
    rm -r ./logs_tiger_fuzzy_unshielded
    rm TigerExperimentsFuzzy_unshielded
fi
mkdir logs_tiger_fuzzy_unshielded
python3.8 ./tiger_experiment_fuzzy_unshielded.py

if [ -d "./logs_NYC" ]
then
    rm -r ./logs_NYC
    rm NYCExperiments
fi
mkdir logs_NYC
python3.8 ./NYC_experiment.py

if [ -d "./logs_NYC_unshielded" ]
then
    rm -r ./logs_NYC_unshielded
    rm NYCExperiments_unshielded
fi
mkdir logs_NYC_unshielded
python3.8 ./NYC_experiment_unshielded.py



python3.8 collect_data_script.py UUVExperimentsFromPythonFile_8_heavy
python3.8 collect_data_script.py UUVExperimentsFromPythonFile_12_heavy
python3.8 collect_data_script.py UUVExperimentsFromPythonFile_16_heavy
python3.8 collect_data_script.py UUVExperimentsFromPythonFile_20_sparse_heavy
python3.8 collect_from_sublogs_script.py logs_8_heavy_unshielded -100
python3.8 collect_from_sublogs_script.py logs_12_heavy_unshielded -100
python3.8 collect_from_sublogs_script.py logs_16_heavy_unshielded -100
python3.8 collect_from_sublogs_script.py logs_20_sparse_heavy_unshielded -100
python3.8 collect_data_script.py TigerExperiments
python3.8 collect_from_sublogs_script.py logs_tiger_unshielded -500
python3.8 collect_data_script.py TigerExperimentsFuzzy
python3.8 collect_from_sublogs_script.py logs_tiger_fuzzy_unshielded -500
python3.8 collect_data_script.py NYCExperiments
python3.8 collect_from_sublogs_script.py logs_NYC_unshielded -5000
