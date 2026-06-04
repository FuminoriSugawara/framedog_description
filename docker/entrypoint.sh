#!/usr/bin/env bash
set -e

# ROS underlay
source "/opt/ros/${ROS_DISTRO}/setup.bash"

# Build the mounted framedog_description package (fast after first run).
if [ -f /ws/src/framedog_description/package.xml ]; then
  cd /ws
  colcon build --symlink-install --packages-select framedog_description \
    --cmake-args -DCMAKE_BUILD_TYPE=Release >/tmp/colcon_build.log 2>&1 \
    || { echo "colcon build failed:"; cat /tmp/colcon_build.log; exit 1; }
  source /ws/install/setup.bash
fi

exec "$@"
