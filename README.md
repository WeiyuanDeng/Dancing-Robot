# Dancing Robot

This is a simple algorithm that is able to let a 3D humanoid robot model dance with whatever songs that is detected in the dataset while the user plays a piece of song to the microphone.

Currently supports ten songs (more could be added) with only two movement, there will be improvement on different  and more movements soon.

## Demo Video (To be continue...)

The project can be divided into two parts. The first part is song learning and classification, the second part is the dance movement capture.

## Dataset and classification

The song learning and classification part in the dancing robot project was an implementation of Will Drevo's remarkable work, Dejavu.

The learning and classification of songs are based on audio fingerprinting. For more information about how Devaju works, please see [here](https://github.com/worldveil/dejavu).

## Humanoid Robot URDF

The description of the humanoid robot is written in [humanoid.urdf](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/urdf/humanoid.urdf). It has totally 22 degrees of freedom.

This is how the humanoid robot URDF viewed (front view and side view) in [Rviz](http://wiki.ros.org/rviz), a 3D visualizer for displaying sensor data and state information from ROS.

![image2](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/front_side_robot.png)

## Dancing Movements

There are 2 ways to get waving movements for the dancing part. One is given joint angle as a function of time, the other is to transform data from Kinect Skeleton Tracking to joint state information.

### Hard coded movements

For test of the movement, there are two waving poses that is only for 2-D plane. The joint state information varies with time is directly given in [waving.py](not yet uploaded).

The graph below is the front view and side view of waving pose 1, with the joint "upper_body_to_right_shoulder" fixed while the joint "right_upper_arm_to_right_elbow" moves.

![waving_pose_1](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/waving1_front_side.png)

The graph below is the front view and side view of waving pose 2, with the joint "right_upper_arm_to_right_elbow" fixed while the joint "upper_body_to_right_shoulder" moves.

![waving_pose_2](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/waving2_front_side.png)

### Movement Capture with Kinect Skeleton Tracking

To implement, please download [OpenNI](http://openni.ru/openni-sdk/openni-sdk-history-2/index.html) and install [openni_tracker](http://wiki.ros.org/openni_tracker).

With the skeleton tracker, the x, y and z position of the frame of each joint can be collected into a csv file and view in excel. To convert this data into joint states, [movement.py]() was written (not yet uploaded), and it is based on the formula below.

![formula](https://github.com/WeiyuanDeng/Dancing-Robot/blob/master/image/vector.png)

The Kinect Skeleton Tracking is only for the movement capture for the dancing, it is not mandantory if you are satisfied with the movements I provided.

## Dance

Finally for the dancing part, each song corresponds to different movements, which was written in dancing.py (some of the lines are still left commented as there will still be improvement in movements in 2 weeks).


