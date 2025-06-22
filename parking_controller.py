from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

sensor = robot.getDevice("slot")  # Sensor name should match PROTO
sensor.enable(timestep)

while robot.step(timestep) != -1:
    print("Distance:", sensor.getValue())  # Debugging
