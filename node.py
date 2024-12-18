from kademlia.network import Server
import asyncio

async def start_node(port, bootstrap_ip=None, bootstrap_port=None):
    print("Start node")
    server = Server()
    print(f"Listen on port {port}") 
    await server.listen(port)

    if bootstrap_ip and bootstrap_port:
        print(f"Bootstrapping to {bootstrap_ip}:{bootstrap_port}") 
        await server.bootstrap([(bootstrap_ip, bootstrap_port)])
        print(f"Node started and connected to {bootstrap_ip}:{bootstrap_port}")
    else:
        print(f"Bootstrap node started on port {port}")

    return server

async def main():
    port = 8080
    bootstrap_ip = "192.168.1.199"
    bootstrap_port = 8080  

    server = await start_node(port, bootstrap_ip, bootstrap_port)
    print("Node is running")
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down node")
        server.stop()

asyncio.run(main())


#node แรก run python node.py 8080
#node สอง run python node.py 8081 192.168.1.199 8080
#node สาม run python node.py 8082 192.168.1.199 8080
#python store_data.py, python get_data.py

#pip install kademlia