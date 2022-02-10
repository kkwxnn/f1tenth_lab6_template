# Lab 6: Pure Pursuit

## I. Learning Goals

- Localization with Particle Filter
- Pure Pursuit Algorithm

## II. Running Cartographer on the car

[TODO]

## III. Localization with Particle Filter

[TODO]

## IV. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node. As per usual, test your algorithm first in the
simulator before you test it on the car. As shown in the lecture, the curvature of the arc to track
can be calculated as:

![](https://latex.codecogs.com/svg.latex?\gamma=\frac{2|y|}{L^2})

## V. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

## VI: Grading Rubric
- Compilation: **10** Points
- Occupancy grid init and update: **20** Points
- Correct collision check: **30** Points
- Correct find path: **30** Points
- Video: **10** Points
