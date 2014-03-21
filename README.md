Plan to Understand
===============
Christopher Lin, Jonathan Bragg
{c1,bragg}@uw.edu


Chris:
- Generated example MDP and policy
- Interaction to show equal states
- Developed example state visualization of GridWorld
- Static pan and zoom
- Multiedge adjustments
- Dynamic loading of tree
- Probability Filter Slider

Jonathan:
- Developed initial base node-link diagram with two different kinds of nodes
- Colors to show values of states
- Legend
- Tooltips
- Buttons to toggle different color schemes and scales

Commentary on development process:
- As always, much time was spent wrestling with and trying to debug javascript and d3 behavior. 
- We originally began by providing as input to d3 a fixed-depth tree. However, we soon saw that such a strategy was quite unscalable since the file for even a depth 5 tree was over 100 MBs. We then converted to dynamically loading data as requested by the user by expressing the MDP as a graph.
