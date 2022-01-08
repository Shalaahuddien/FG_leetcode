思考 state + choice是 分析subproblem的核心，故 dfs,dp的核心。
Can we move robot1 firstly to the bottom row, and then move robot2?
​
Maybe not. In this case, the movement of robot1 will impact the movement of robot2. In other words, the optimal track of robot2 depends on the track of robot1. If we want to apply DP, we need to record the whole track of robot1 as the state. The number of sub-problems is too much.
​
In fact, in any case, when we move one robot several steps earlier than the other, the movement of the first robot will impact the movement of the second robot.