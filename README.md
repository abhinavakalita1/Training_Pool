# Training Pool

This workspace contains multiple ROS 2 + Gazebo resources for simulating a UGV/Ackermann rover and DRDO-style terrain worlds.

Packages in this repo:
- `uavcollab` — Gazebo world launcher and world assets
- `ackermann_gz_bringup` — spawn and bridge for the Ackermann robot
- `drdo_gz_worlds` — DRDO terrain world launch files and models

---

## 1. Setup

### Prerequisites
- Ubuntu/Linux with ROS 2 Humble installed
- Gazebo Harmonic / `gz sim` available
- `colcon` installed
- `rosdep` available

### Workspace setup
From the repo root:

```bash
cd /path/to/training_pool
source /opt/ros/humble/setup.bash
rosdep install --from-paths src --ignore-src -y
colcon build --symlink-install
source install/setup.bash
```

### Optional: PX4 / Gazebo resources
If you plan to run PX4 SITL with Gazebo, add the following to your shell startup file:

```bash
export GZ_SIM_RESOURCE_PATH=$HOME/PX4-Autopilot/Tools/simulation/gz/models:$HOME/PX4-Autopilot/Tools/simulation/gz/worlds:$HOME/training_pool/src/uavcollab/worlds
```

Then reload the shell:

```bash
source ~/.bashrc
```

---

## 2. Launch files and arguments

### 2.1 `uavcollab` world launcher
File: `src/uavcollab/launch/gazebo_launch.py`

Launch a Gazebo world directly:

```bash
ros2 launch uavcollab gazebo_launch.py
```

Launch a specific world file:

```bash
ros2 launch uavcollab gazebo_launch.py world:=model.world
ros2 launch uavcollab gazebo_launch.py world:=world1.world
```

Arguments:
- `world` — world filename inside `src/uavcollab/worlds`.
  - default: `world1.world`
  - examples:
    - `model.world` → `nb_park` world
    - `world1.world` → `my_park` world

This launch sets `GZ_SIM_RESOURCE_PATH` so the world assets and PX4 model resources can be found.

---

### 2.2 `ackermann_gz_bringup` model spawner
File: `src/ackermann_gz_bringup/launch/spawn_ackermann.launch.py`

This launch file does not start Gazebo itself. It spawns the Ackermann robot into an already-running world and bridges ROS/Gazebo topics.

Example:

```bash
ros2 launch ackermann_gz_bringup spawn_ackermann.launch.py world:=empty
```

Custom spawn pose:

```bash
ros2 launch ackermann_gz_bringup spawn_ackermann.launch.py \
  world:=my_world \
  robot_name:=ackermann_bot \
  x:=1.5 y:=-2.0 z:=0.1 yaw:=0.7
```

Arguments:
- `world` — name of the already-running Gazebo world
  - default: `empty`
- `robot_name` — spawned model name / namespace
  - default: `ackermann_bot`
- `x` — spawn X position
  - default: `0.0`
- `y` — spawn Y position
  - default: `0.0`
- `z` — spawn Z position
  - default: `0.1`
- `yaw` — spawn yaw in radians
  - default: `0.0`

The bridge exposes:
- `/cmd_vel` → Gazebo vehicle command
- `/odom` → odometry output
- `/joint_states` → joint states
- `/clock` → sim clock

---

### 2.3 `uavcollab` Ackermann bridge
File: `src/uavcollab/worlds/ackermann_bridge_launch.py`

This is a separate bridge launch for a model already present in the running world.

Examples:

```bash
ros2 launch uavcollab ackermann_bridge_launch.py
ros2 launch uavcollab ackermann_bridge_launch.py model_name:=ackermann_rover
```

Arguments:
- `model_name` — model name in the world
  - default: `ackermann_rover`

This bridges:
- `/model/<name>/cmd_vel` ↔ `/cmd_vel`
- `/model/<name>/odometry` ↔ `/odom`
- `/model/<name>/pose` ↔ `/tf`

---

### 2.4 `drdo_gz_worlds` terrain launcher
File: `src/drdo_gz_worlds/launch/world.launch.py`

This launches the DRDO terrain worlds in Gazebo Harmonic.

Basic examples:

```bash
ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world1
ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world1_overlay
ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world2
ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world2_overlay
ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world3
```

Arguments:
- `world` — terrain world to load
  - default: `drdo_world2`
  - supported: `drdo_world1`, `drdo_world1_overlay`, `drdo_world2`, `drdo_world2_overlay`, `drdo_world3`
- `gui` — enable/disable Gazebo GUI
  - default: `true`
- `uav_sdf` — path to UAV SDF model, leave empty to skip spawning UAV
  - default: empty string
- `uav_name` — UAV model name
  - default: `iris`
- `uav_x`, `uav_y`, `uav_z` — UAV spawn position
  - default: `0`
- `uav_roll`, `uav_pitch`, `uav_yaw` — UAV orientation in radians
  - default: `0`
- `ugv_sdf` — path to UGV SDF model, leave empty to skip spawning UGV
  - default: empty string
- `ugv_name` — UGV model name
  - default: `prius`
- `ugv_x`, `ugv_y`, `ugv_z` — UGV spawn position
  - default: `0`
- `ugv_roll`, `ugv_pitch`, `ugv_yaw` — UGV orientation in radians
  - default: `0`

Example with both vehicles:

```bash
ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world1 \
  uav_sdf:=/path/to/iris.sdf \
  uav_x:=-10.226 uav_y:=311.831 uav_z:=22.863 \
  uav_roll:=0.011338 uav_pitch:=0.135709 uav_yaw:=-2.161422 \
  ugv_sdf:=/path/to/prius.sdf \
  ugv_x:=-12.220319 ugv_y:=308.976703 ugv_z:=22.295580 \
  ugv_roll:=0.011338 ugv_pitch:=0.135709 ugv_yaw:=-2.161422
```

---

## 3. DRDO world offset note

Important: the DRDO terrain world has a fixed world offset. If you spawn the drone or UGV at the origin, they will appear in the wrong place relative to the terrain.

Use the terrain offsets below when loading the drone/UGV into the DRDO world.

### `drdo_world1`
- UAV: `x=-10.226`, `y=311.831`, `z=22.863`, `roll=0.011338`, `pitch=0.135709`, `yaw=-2.161422`
- UGV: `x=-12.220319`, `y=308.976703`, `z=22.295580`, `roll=0.011338`, `pitch=0.135709`, `yaw=-2.161422`

### `drdo_world2`
- UAV: `x=103.776917`, `y=-101.472992`, `z=17.318562`, `roll=-0.054656`, `pitch=0.032451`, `yaw=2.460081`
- UGV: `x=104.742386`, `y=-101.9010777`, `z=15.730011`, `roll=-0.054656`, `pitch=0.032451`, `yaw=2.460081`

### `drdo_world3`
- UAV: `x=108.849`, `y=-265.663`, `z=49.4752`, `roll=0.045161`, `pitch=0.003268`, `yaw=1.588`
- UGV: `x=109.076`, `y=-262.736`, `z=49.2026`, `roll=0.005846`, `pitch=-0.047033`, `yaw=1.56611`

> This offset is required for the DRDO world; do not use raw `(0,0,0)` spawn poses unless you intentionally want to place the robot away from the terrain.

---

## 4. PX4 example (optional)

If you are using PX4 SITL with Gazebo:

```bash
PX4_GZ_STANDALONE=1 PX4_SIM_MODEL=gz_x500 PX4_GZ_WORLD=my_park_world PX4_GZ_MODEL_POSE="-45,0,5,0,0,0" ./build/px4_sitl_default/bin/px4
```

Replace the world name and starting pose as needed.

---

## 5. Typical workflow

1. Launch the terrain world:
   ```bash
   ros2 launch drdo_gz_worlds world.launch.py world:=drdo_world1
   ```
2. Spawn the robot(s) with the terrain-specific offset values above.
3. Connect PX4 or other autonomy stack if needed.
4. Use `/cmd_vel`, `/odom`, and `/tf` for control and monitoring.

This is the expected pattern for DRDO terrain testing and for custom Ackermann/UAV experimentation in this workspace.
