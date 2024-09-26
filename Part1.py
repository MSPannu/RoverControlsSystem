import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (replace with actual server IP and port)
server_address = ('localhost', 10000)
client_socket.connect(server_address)
def send_drive_packet(right_wheel_pwms, left_wheel_pwms):
    packet = f"D_{'_'.join(map(str, right_wheel_pwms))}_{'_'.join(map(str, left_wheel_pwms))}"
    print(packet)  # Print the packet
    client_socket.sendall(packet.encode('utf-8'))

def send_arm_packet(motor_pwms):
    packet = f"A_{'_'.join(map(str, motor_pwms))}"
    print(packet)  # Print the packet
    client_socket.sendall(packet.encode('utf-8'))
import pygame

pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Example of reading joystick axis for control
def get_controller_input():
    pygame.event.pump()  # Process event queue
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    return x_axis, y_axis
def map_joystick_to_pwm(value):
    # Normalize joystick input (-1 to 1) to PWM (0 to 255)
    return int((value + 1) * 127.5)

def send_movement_commands():
    x_axis, y_axis = get_controller_input()
    right_wheel_pwms = [map_joystick_to_pwm(y_axis)] * 3  # Example
    left_wheel_pwms = [map_joystick_to_pwm(y_axis)] * 3   # Example
    send_drive_packet(right_wheel_pwms, left_wheel_pwms)
test_right_pwms = [128, 150, 200]
test_left_pwms = [128, 150, 200]
send_drive_packet(test_right_pwms, test_left_pwms)

test_arm_pwms = [200, 150, 128, 255, 200, 180]
send_arm_packet(test_arm_pwms)
client_socket.close()
