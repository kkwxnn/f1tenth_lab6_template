# Lab 6: SLAM and Pure Pursuit

## I. Learning Goals

- SLAM
- Localization with Particle Filter
- Pure Pursuit Algorithm

## II. Running slam_toolbox on the car

Follow the instructions in class to run `slam_toolbox` to make a map of Levine second floor. Save the map as `levine_2nd.pgm` and `levine_2nd.yaml`.

## III. Localization with Particle Filter

Follow the instructions in class to run `particle_filter` on the car using the new map you've made on Levine second floor.

## IV. Pure Pursuit Implementation

We have provided a skeleton for the pure pursuit node. As per usual, test your algorithm first in the simulator before you test it on the car. When you're testing in the simulator, use the groud truth pose provided by the sim as the localization. When you move to the car, use particle filter to provide localization.

As shown in the lecture, the curvature of the arc to track
can be calculated as:

![](https://latex.codecogs.com/svg.latex?\gamma=\frac{2|y|}{L^2})

## V. Visualizing Waypoints

To visualize the list of waypoints you have, and to visualize the current waypoint you're picking, you'll need to use the `visualization_msgs` messages and RViz. You can find some information [here](http://wiki.ros.org/rviz/DisplayTypes/Marker).

## VI. Deliverables

**Deliverable 1**: submit the map files (.pgm and .yaml) that you've made using `slam_toolbox`.
**Deliverable 2**: commit your pure pursuit package to GitHub.
**Deliverable 3**: submit a link to a video on YouTube showing pure pursuit running on the car. Show a screen recording of rviz. If you want to include a video of the car running that's also ok.

## VII: Grading Rubric
- Compilation: **10** Points
- Running slam_toolbox and producing a map: **30** Points
- Running particle_filter: **20** Points
- Implementing pure pursuit: **30** Points
- Video: **10** Points
