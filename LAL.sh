#!/bin/bash

# Loop over the fold values from 0.02 to 0.1 with a step size of 0.01
for fold in $(seq 0.02 0.01 0.1)
do
    # Run the Python script with the current fold value
    python3 ./LAL/LALnet.py --fold $fold
done
