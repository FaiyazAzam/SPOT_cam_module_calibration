import bosdyn.client
from bosdyn.client.fiducial import FiducialClient

def detect_fiducials(robot_ip, username, password):
    # Initialize SDK and connect to the robot
    sdk = bosdyn.client.create_standard_sdk('FiducialDetection')
    robot = sdk.create_robot(robot_ip)
    robot.authenticate(username, password)

    # Create FiducialClient
    fiducial_client = robot.ensure_client(FiducialClient.default_service_name)

    # Detect fiducials
    fiducial_data = fiducial_client.get_visible_fiducials()
    for fiducial in fiducial_data.fiducials:
        print(f"Fiducial ID: {fiducial.fiducial_id}")
        print(f"Pose (x, y, z): {fiducial.pose_in_world.position}")
        print(f"Rotation (quaternion): {fiducial.pose_in_world.rotation}")
        print(f"Image Coordinates: {fiducial.image_coordinates}")

    return fiducial_data

if __name__ == "__main__":
    detect_fiducials(
        robot_ip="<ROBOT_IP>",
        username="<USERNAME>",
        password="<PASSWORD>"
    )
