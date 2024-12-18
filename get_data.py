from kademlia.network import Server
import asyncio

async def get_data(port, key):
    server = Server()
    await server.listen(port)

    bootstrap_ip = "192.168.1.199"
    bootstrap_port = 8080
    await server.bootstrap([(bootstrap_ip, bootstrap_port)])

    value = await server.get(key)
    print(f"Get {key}: {value}")

    server.stop()

asyncio.run(get_data(8081, "NetworkProject"))
