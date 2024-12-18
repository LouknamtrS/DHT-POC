from kademlia.network import Server
import asyncio

async def store_data(port, key, value):
    server = Server()
    await server.listen(port)

    bootstrap_ip = "192.168.1.199"
    bootstrap_port = 8080
    await server.bootstrap([(bootstrap_ip, bootstrap_port)])

    await server.set(key, value)
    print(f"Stored {key}: {value} in the DHT")

    server.stop()

asyncio.run(store_data(8081, "NetworkProject", "This is my final project"))
