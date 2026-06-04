# RViz preview via Docker

Runs `robot_state_publisher` + `joint_state_publisher_gui` + `rviz2` for
`framedog_description` in a container, displaying RViz on your host (Linux/X11).

## Prerequisites

- Docker + Docker Compose, and an X11 desktop session on the host.
- Allow the container to talk to your X server (once per login):

  ```bash
  xhost +local:root
  ```

## Run

From the repository root:

```bash
docker compose -f docker/docker-compose.yml up --build
```

This shows the **full robot** (body + 4 legs) with `joint_state_publisher_gui`
sliders for the 12 active joints (`roll`, `pitch`, `knee` × 4 legs); each `calf` and
`coupler` follows its knee automatically via a mimic.

Show both legs side by side instead of the whole robot:

```bash
docker compose -f docker/docker-compose.yml run --rm framedog_rviz \
  ros2 launch framedog_description display.launch.py model:=legs_display.urdf.xacro
```

Stop:

```bash
docker compose -f docker/docker-compose.yml down
```

## Options

- `ROS_DISTRO` (default `jazzy`, using a local `osrf/ros:jazzy-desktop-full` image).
  For another distro override both args, e.g.:
  `ROS_DISTRO=humble BASE_IMAGE=osrf/ros:humble-desktop docker compose ... up --build`
- `LIBGL_ALWAYS_SOFTWARE=1`: set if RViz fails to render (forces software OpenGL).
- NVIDIA GPU: add the `nvidia` runtime / `NVIDIA_*` env if you want hardware GL.

## Notes

- The package source is bind-mounted, so edits to `urdf/`, `meshes/`, `launch/`,
  `rviz/` are picked up on the next `up` (the container rebuilds the package).
- Build artifacts stay inside the container (`/ws/build`, `/ws/install`).
