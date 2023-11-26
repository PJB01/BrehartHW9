#!/bin/bash
echo "Setting p9.12 as output."
config-pin p9.12 gpio
echo "Setting p8.16 as input with pull-up resistor enabled."
config-pin p8.16 gpio_pu
echo "Compiling myGpioApp application ................"
g++ read_resistance.cpp AnalogIn.cpp -o readResistance
echo " ................. Done!"
echo ""