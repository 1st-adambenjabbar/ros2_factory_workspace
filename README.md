# Dog Factory ROS 2 Workspace

This repository contains an in-progress ROS 2 workspace for a quadruped dog robot simulation. The current focus is the robot description, Gazebo environment, and basic simulation bringup.

> **Project status**  This project is not finished yet. Interfaces, configuration, and simulation behavior may change as development continues.

## Workspace structure

```text
src/
├── dog_robot_description/   # URDF and Xacro robot description
├── dog_factory_environment/ # Gazebo world and environment assets
├── dog_factory_bringup/     # Basic simulation launch files
└── dog_factory_control/     # Keyboard teleoperation
```

## Current scope

The workspace provides the foundation for launching the robot model in a Gazebo factory environment. The project is being developed incrementally, starting with a stable simulation foundation.

## References

### A  ROS 2 Core

- [ROS 2 Documentation (Humble)](https://docs.ros.org/en/humble/index.html). The main entry point for ROS 2 documentation.
- [rclpy Node API reference](https://docs.ros2.org/foxy/api/rclpy/api/node.html). Reference for Node methods such as `create_publisher`, `create_subscription`, `create_timer`, and `get_logger`. The same API is available for other ROS 2 distributions on the corresponding documentation pages.
- [rclcpp API reference](https://docs.ros2.org/humble/api/rclcpp/). The C++ equivalent for `rclcpp::Node`, publishers, subscriptions, and related patterns.
- ROS 2 concepts include [Topics](https://docs.ros.org/en/humble/Concepts/Basic/AboutTopics.html), [Services](https://docs.ros.org/en/humble/Concepts/Basic/About-Services.html), and [Actions](https://docs.ros.org/en/humble/Concepts/Basic/About-Actions.html).
- [colcon documentation](https://colcon.readthedocs.io/en/released/). Documentation for the ROS 2 build tool.
- [ament_cmake documentation](https://docs.ros.org/en/humble/How-To-Guides/AmentCMake-Documentation.html). Reference for the CMake build system used by ROS 2 packages.
- [REP-149 Package manifest format 3](https://ros.org/reps/rep-0149.html). Specification for `package.xml` files.

### B  URDF, Xacro, and TF

- [URDF XML specification](http://wiki.ros.org/urdf/XML). Reference for the robot description format used by the Xacro files.
- [Xacro documentation](http://wiki.ros.org/xacro). Reference for properties, macros, and expression syntax.
- [URDF joint types](http://wiki.ros.org/urdf/XML/joint). Reference for URDF joint definitions.
- [tf2 documentation](https://docs.ros.org/en/humble/Tutorials/Intermediate/Tf2/Tf2-Main.html). Documentation for the transform tree system used with `robot_state_publisher`.

### C  Gazebo and SDF

- [SDF specification](http://sdformat.org/spec). Reference for the format used by `factory.world`, including `<model>`, `<link>`, and `<physics>` elements.
- [Gazebo documentation](https://gazebosim.org/docs). Documentation for the Gazebo simulation environment.
- [gazebo_ros_pkgs](https://github.com/ros-simulation/gazebo_ros_pkgs). ROS 2 and Gazebo integration packages, including `spawn_entity.py` used by the bringup launch file.

### D  ros2_control

- [ros2_control documentation](https://control.ros.org/). Documentation for the ROS 2 control framework and controller configuration concepts.
- [ros2_control controller types reference](https://control.ros.org/master/doc/ros2_controllers/doc/controllers_index.html). Reference for available controller types, including joint group position controllers.

### E  Nav2

- [Nav2 documentation](https://docs.nav2.org/). Documentation for the ROS 2 navigation stack.
- [Nav2 costmap layers](https://docs.nav2.org/configuration/packages/configuring-costmaps.html). Reference for navigation costmaps.
- [AMCL localization](https://docs.nav2.org/configuration/packages/configuring-amcl.html). Reference for particle filter localization.
- [DWB local planner](https://docs.nav2.org/configuration/packages/configuring-dwb-controller.html). Reference for the DWB local controller.
- [Behavior trees in Nav2](https://docs.nav2.org/behavior_trees/index.html). Reference for Nav2 behavior tree navigation flows.

### F  Python and C++ Language References

- [Python official tutorial on classes and inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance). Language reference for class inheritance such as `class KeyboardTeleop(Node)`.
- [Python enum module](https://docs.python.org/3/library/enum.html). Reference for `Enum` and `auto()`.
- [Python termios module](https://docs.python.org/3/library/termios.html). Unix terminal I/O reference used by keyboard teleoperation.
- [cppreference.com on `std::bind`](https://en.cppreference.com/w/cpp/utility/functional/bind). C++ functional binding reference.
- [cppreference.com on `std::shared_ptr`](https://en.cppreference.com/w/cpp/memory/shared_ptr). C++ shared ownership pointer reference.

### Useful YouTube Videos

 [URDF](https://youtu.be/Eie-KoMQtxs)
 [XML / Xacro](https://youtu.be/GdVXeAgla1E)

## License

Apache-2.0
