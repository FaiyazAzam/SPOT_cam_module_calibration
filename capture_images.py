import bosdyn.client
from bosdyn.client.image import ImageClient

def capture_images(robot_ip, username, password, output_dir, camera_source):
    # Initialize SDK and connect to the robot
    sdk = bosdyn.client.create_standard_sdk('FiducialImageCapture')
    robot = sdk.create_robot(robot_ip)
    robot.authenticate(username, password)

    # Create ImageClient
    image_client = robot.ensure_client(ImageClient.default_service_name)

    # Capture image from specified camera source
    image_response = image_client.get_image_from_sources([camera_source])
    image_file = f"{output_dir}/{camera_source}.jpg"
    
    # Save the image
    with open(image_file, "wb") as f:
        f.write(image_response[0].shot.image.data)
    print(f"Image saved: {image_file}")

if __name__ == "__main__":
    capture_images(
        robot_ip="<ROBOT_IP>",
        username="<USERNAME>",
        password="<PASSWORD>",
        output_dir="images",
        camera_source="frontleft_fisheye_image"  # Replace with desired camera source
    )
