# ROV Control Structure

A basic description of the existing control software.

## joy

Pre-existing joystick package reading joystick inputs and publishing it to a topic.

## joy_map

Mapping the joystick input topic to whatever we want.

## controller

Controls position. At the moment a controller for an open loop structure.

## allocator

Allocates the right amount of force (N) to each thruster to maintain a stable position.

## thruster_interface

Converts the force into PWM-signals determined by the T200 force graph.

## pwm_interface

Simple python script using the local variable consisting of PWM signals and sends the to the ESC's. Uses the PCA9865 board from Adafruit.

### sensor_node

Simple node reading raw data from sensors. Mainly pressure and IMU data.

### estimator

Estimates the position given at least pressure (depth) and IMU data (position, velocity, acceleration)

