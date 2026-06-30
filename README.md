# framedog_description

Robot description (URDF/xacro + meshes) for **FrameDog**, an open-source 12-DOF
quadruped. This is the ROS 2 description package; the mechanical hardware (printable
parts, BOM) lives in [`framedog-hardware`](https://github.com/FuminoriSugawara/framedog-hardware).

## Contents

```
urdf/
  leg.xacro                 leg macro (3-DOF; knee 4-bar via mimic joints)
  framedog.urdf.xacro       full robot: body + 4 legs (12-DOF)
  legs_display.urdf.xacro   both legs side by side (preview)
  d435i.xacro               D435i camera macro (link + REP-103 optical frames)
  framedog_with_sensors.urdf.xacro  full robot + sensors (D435i camera; display / check_urdf)
meshes/
  body/body.stl
  leg/*.stl                 8 leg meshes (6 shared L/R + per-side knee cranks)
  sensors/d435i_assem.stl   D435i camera + mount mesh
launch/display.launch.py    robot_state_publisher + joint_state_publisher_gui + rviz2
rviz/framedog.rviz
docker/                     containerised RViz preview (no host ROS needed)
package.xml, CMakeLists.txt
```

## Quick preview (Docker)

No host ROS install needed. On a Linux/X11 host:

```bash
xhost +local:root
docker compose -f docker/docker-compose.yml up --build
```

RViz opens with `joint_state_publisher_gui` sliders for the 12 active joints
(roll/pitch/knee × 4 legs); each `calf`/`coupler` follows its knee via a mimic.

## Build in a ROS 2 workspace

```bash
# from your workspace root, with this repo under src/framedog_description
colcon build --packages-select framedog_description
source install/setup.bash
ros2 launch framedog_description display.launch.py

# with the D435i camera (full robot + camera link and REP-103 optical frames):
ros2 launch framedog_description display.launch.py model:=framedog_with_sensors.urdf.xacro
```

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE).
