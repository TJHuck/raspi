#!/bin/bash

# Check if coordinates were provided
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Usage: ./run_spoof.sh <latitude> <longitude>"
    echo "Example: ./run_spoof.sh 40.7128 -74.0060 (New York)"
    exit 1
fi

LAT=$1
LON=$2

echo "Configuring browser environment for Coordinates: $LAT, $LON..."

# Dynamically overwrite the coordinates in the JS template
sed -i.bak "s/geolocation: { .*/geolocation: { latitude: $LAT, longitude: $LON },/" spoof.js

# Execute the script
node spoof.js
