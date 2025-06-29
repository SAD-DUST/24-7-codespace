import time
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet

SERVER_IP = '148.113.216.61'
SERVER_PORT = 3162
USERNAME = 'ChunkLoaderVIP'

def create_connection():
    conn = Connection(SERVER_IP, SERVER_PORT, username=USERNAME)

    def handle_join_game(join_game_packet):
        print("[+] Bot joined the game. Staying idle.")

    def handle_disconnect(disconnect_packet):
        print("[-] Disconnected from server. Reason:", disconnect_packet.json_data)

    conn.register_packet_listener(handle_join_game, Packet.JOIN_GAME)
    conn.register_packet_listener(handle_disconnect, Packet.DISCONNECT)

    return conn

while True:
    try:
        print("[*] Connecting to server...")
        conn = create_connection()
        conn.connect()
    except Exception as e:
        print("[!] Connection failed:", e)
        print("[*] Reconnecting in 5 seconds...")
        time.sleep(5)
