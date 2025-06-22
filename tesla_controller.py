from controller import Supervisor

# Create the Supervisor instance
supervisor = Supervisor()

# Get the robot node (TeslaModel3Simple)
robot = supervisor.getSelf()

# Get the initial translation and rotation
initial_translation = robot.getField("translation")
initial_rotation = robot.getField("rotation")

# Set initial values
current_x = initial_translation.getSFVec3f()[0]  # x-coordinate
current_y = initial_translation.getSFVec3f()[1]  # y-coordinate
current_z = initial_translation.getSFVec3f()[2]  # z-coordinate
current_angle = initial_rotation.getSFRotation()[3]  # rotation angle around z-axis

# Time step for simulation
timestep = int(supervisor.getBasicTimeStep())

# Movement parameters
speed = 0.1  # meters per second
turn_rate = 0.1  # radians per second
direction = 0  # 1 for forward, -1 for backward, 0 for stop
turn = 0      # 1 for right, -1 for left, 0 for straight

# Main loop
while supervisor.step(timestep) != -1:
    # Keyboard input for control
    if supervisor.getKeyboard() != -1:
        key = supervisor.getKey()
        if key == ord('W'):  # Move forward
            direction = 1
        elif key == ord('S'):  # Move backward
            direction = -1
        elif key == ord('A'):  # Turn left
            turn = -1
        elif key == ord('D'):  # Turn right
            turn = 1
        elif key == ord(' '):  # Stop
            direction = 0
            turn = 0

    # Update position based on direction
    current_x += direction * speed * (timestep / 1000.0)
    current_angle += turn * turn_rate * (timestep / 1000.0)

    # Apply new translation and rotation
    initial_translation.setSFVec3f([current_x, current_y, current_z])
    initial_rotation.setSFRotation([0, 0, 1, current_angle])

    # Optional: Reset if out of bounds (e.g., x > 10 or x < -10)
    if current_x > 10 or current_x < -10:
        current_x = 0
        initial_translation.setSFVec3f([current_x, current_y, current_z])