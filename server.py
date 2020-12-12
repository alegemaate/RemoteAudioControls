"""Server for media key server."""
import socket
from win32con import (
    VK_MEDIA_PLAY_PAUSE,
    KEYEVENTF_EXTENDEDKEY,
    VK_VOLUME_UP,
    VK_VOLUME_DOWN,
    VK_MEDIA_NEXT_TRACK,
    VK_MEDIA_PREV_TRACK
)
import win32api


def simulateKey(code):
    """Simulate Windows keycode."""
    win32api.keybd_event(code, 0, KEYEVENTF_EXTENDEDKEY, 0)


def main(ip_address, port):
    """Establish server."""
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip_address, port))
    serv.listen(5)
    toggle_count = 0

    print("Server started!")

    while True:
        conn, addr = serv.accept()
        while True:
            data = conn.recv(4096)
            if not data:
                break

            command = data.decode()
            print(command)

            if command in ("toggle", "play"):
                simulateKey(VK_MEDIA_PLAY_PAUSE)
                toggle_count += 1
                conn.send(f"🔫 You have toggled \
                    {toggle_count} times".encode())

            elif command == "up":
                simulateKey(VK_VOLUME_UP)
                simulateKey(VK_VOLUME_UP)
                simulateKey(VK_VOLUME_UP)
                simulateKey(VK_VOLUME_UP)
                simulateKey(VK_VOLUME_UP)
                conn.send("🔊 Volume increased".encode())

            elif command == "down":
                simulateKey(VK_VOLUME_DOWN)
                simulateKey(VK_VOLUME_DOWN)
                simulateKey(VK_VOLUME_DOWN)
                simulateKey(VK_VOLUME_DOWN)
                simulateKey(VK_VOLUME_DOWN)
                conn.send("🔉 Volume decreased".encode())

            elif command in ("next", "skip"):
                simulateKey(VK_MEDIA_NEXT_TRACK)
                conn.send("🤢 You didn't like that one!".encode())

            elif command in ("previous", "prev"):
                simulateKey(VK_MEDIA_PREV_TRACK)
                conn.send("❤️ You loved that one!".encode())

            else:
                conn.send("Unknown command".encode())

        conn.close()
        print('client disconnected')


main('0.0.0.0', 8080)
