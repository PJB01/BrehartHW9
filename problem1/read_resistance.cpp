// read_resistance.cpp
// Created by Phil Brehart

#include <stdio.h>
#include <iostream>
#include "AnalogIn.h"

int main(void)
{
    float vcc = 1.8; // voltage across resistors

    std::cout << "Using AIN0 to read analog value." << std::endl;
    AnalogIn AIN0(0);
    std::cout << "Measuring resistance..." << std::endl;
    float adcVal = AIN0.readAdcSample();
    std::cout << "ADC value is: " << adcVal << std::endl;
    float voltageR = vcc * (adcVal / 4095);
    float resistance = 10000 / voltageR;
    std::cout << "Resistance: " << resistance << "Ohms" << std::endl;

    return 0;
}
