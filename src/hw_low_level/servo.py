#!/usr/bin/env python
# # -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# servo.py
#
# G. Thomas
# 2018
#-------------------------------------------------------------------------------

import logging
import time

class Servo(object):
    '''Servo object that is able to go to a given angle using a PWM source'''

    SERVO_FREQ = 50

    def __init__(self, pwm_provider):
        '''Create a servo object with a PWM source'''
        self.__logger = logging.getLogger(__name__)

        self.__pwm = pwm_provider
        self.__angle = -90

    def set_angle(self, angle):
        '''Sets the angle of the servo

        Makes sure the servo is only moved between min and max angle values.
        Gives 0.5s for the servo to move then the servo is turned off to reduce
        power consumption and keep things quiet.
        '''

        # Check that the angle is in range
        assert(angle >= 0)
        assert(angle <= 180)

        if self.__angle != angle:
            # Calculate the duty cycle as a percentage
            # 50Hz => 20ms
            # 0.5ms => 0deg => 2.5%
            # 2.5ms => 180deg => 12.5%
            duty = (2.5 + (angle / 18))

            # Set the desired position
            self.__pwm.set_duty(duty)

            # Make sure that the freq is set correctly
            self.__pwm.set_freq(Servo.SERVO_FREQ)

            self.__pwm.turn_on()

        else:
            # If there is no change in angle from the last request turn the
            # servo off to reduce current and noise
            self.__pwm.turn_off()

        self.__angle = angle

    def get_angle(self):
        '''Return the current servo angle'''
        return self.__angle

