# Dancing Robot

This is a simple algorithm that is able to let a 3D humanoid robot model dance with different songs that is detected.

Currently supports ten songs (more could be added) with only two movement, there will be improvement on different  and more movements soon.

## Demo Video (To be continue...)

The project can be divided into two parts. The first part is song learning and classification, the second part is the dance movement capture.

## Dataset and classification

The song learning and classification part in the dancing robot project was an implementation of Will Drevo's remarkable work, Dejavu.

For more information about Devaju, please see [here](https://github.com/worldveil/dejavu).

## Humanoid Robot URDF

The description of the humanoid robot is written in [humanoid.urdf](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/urdf/humanoid.urdf). It has totally 22 degrees of freedom.

This is how the humanoid robot URDF viewed in [Rviz](http://wiki.ros.org/rviz), a 3D visualizer for displaying sensor data and state information from ROS.

![image2](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/front_side_robot.png)

## Dancing Movements

For test, there are two waving poses.

The graph below is the front view and side view of waving pose 1, with the joint "upper_body_to_right_shoulder" fixed while the joint "right_upper_arm_to_right_elbow" moves.

![waving_pose_1](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/waving1_front_side.png)

The graph below is the front view and side view of waving pose 2, with the joint "right_upper_arm_to_right_elbow" fixed while the joint "upper_body_to_right_shoulder" moves.

![waving_pose_2](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/waving2_front_side.png)


### Hard code movements

### Movement Capture with Kinect Skeleton Tracking



The Kinect Skeleton Tracking is only for the movement capture for the dancing, it is not mandantory if you are satisfied with the movements I provided.


## Dance

An









**Bold** and _Italic_ and `Code` text


