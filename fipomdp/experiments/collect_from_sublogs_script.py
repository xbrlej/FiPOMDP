#!/usr/bin/env python3

import os
import sys
import ast
from statistics import stdev


def main(argv):   # argv are [directory with logs, default value when died]
    if len(argv) != 2:
        raise ValueError("Incorrect length of arguments")

    all_dec_times = []
    target_hits = []
    rewards = []
    deaths = 0

    for filename in os.listdir(argv[0]):
        with open(os.path.join(argv[0], filename), "r") as f:
            text = f.read()
            lines = text.split("IN")[-9:]
            died = ("energy: -" in text) or ("energy: 0" in text)
            # died = True
            if not died:
                target_hits.append("True" in lines[4])
            rewards.append(int(argv[1]) if died else int(lines[8].split(" ")[-1].strip()))
            # path = ast.literal_eval(lines[5].split(": ")[1].strip())
            all_dec_times.extend(ast.literal_eval(lines[6].split(": ")[1].split("\n")[0].strip()))

            if died:
                deaths += 1

        f.close()

    print(stdev(all_dec_times))
    stats = []

    stats.append(f"Deaths by energy {deaths}")
    stats.append(f"Target hits: {target_hits.count(True)}/{len(target_hits)}")
    stats.append(
        f"Decision count: {len(all_dec_times)}, Average: {sum(all_dec_times) / len(all_dec_times)}")
    stats.append(f"Decision standard deviation: {stdev(all_dec_times)}")
    stats.append(f"Average reward: {sum(rewards) / len(rewards)}")
    stats.append(f"Reward standard deviation: {stdev(rewards)}")

    filename = str(argv[0]).replace("/", "")
    print(filename)

    for stat in stats:
        print(stat)

    stat_file = open(f"{filename}_SUBLOGS_STATS.txt", 'w')
    stat_file.write('\n'.join(stats) + '\n')

    stat_file.close()

if __name__ == "__main__":
    main(sys.argv[1:])
