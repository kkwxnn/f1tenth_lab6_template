# Lab 6: Pure Pursuit

## I. Learning Goals

- Localization with Particle Filter
- Pure Pursuit Algorithm

## II. Localization with Particle Filter

[TODO]

## III. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node. As per usual, test your algorithm first in the
simulator before you test it on the car. As shown in the lecture, the curvature of the arc to track
can be calculated as:

![](https://latex.codecogs.com/svg.latex?\gamma=\frac{2|y|}{L^2})

## IV. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the \textit{visualization\_msgs} messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

## V: Grading Rubric
- Compilation: **30** Points
- Provided Video: **20** Points
- Correctly stops before collision: **30** Points
- Correctly calculates TTC: **10** Points
- Able to navigate through the hallway: **10** Points