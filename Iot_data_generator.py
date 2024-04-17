from azure.iot.device.aio import IoTHubDeviceClient
from random import randrange, random, choice
from datetime import datetime
import time
import json
import asyncio

num_devices = 15

# Define connection string
connectionString = "HostName=MM-IotHubProd.azure-devices.net;DeviceId=Device1;SharedAccessKey=fMM8562MLBr5v9rS+fp4G91RvDMpkWpolAIoTKuoedc="

async def sendToIotHub(data):
    try:
        # Create an instance of the IoT Hub Client class
        device_client = IoTHubDeviceClient.create_from_connection_string(connectionString)

        # Connect the device client
        await device_client.connect()

        #Send the message
        await device_client.send_message(data)

        #print("Message sent to IoT Hub:", data)

        # Shutdown the client
        await device_client.shutdown()
        
    
    except Exception as e:
        print("Error:", str(e))

def main():

    x = 1
    while x<100:
        # Generate random value
        msg = {}

        device_id = randrange(1, num_devices)
        tmp =  randrange(90, 120)
        hmdt =  randrange(60, 80)
        prsre = randrange(400, 500)
        ts = datetime.now().isoformat()

        msg["device_id"] = device_id
        msg["tmp"] = tmp
        msg["hmdt"] = hmdt
        msg["prsre"] = prsre
        msg["ts"] = ts
        msg["source"] = "IotHub"
        # Generate data packet
        print(json.dumps(msg))
        asyncio.run(sendToIotHub(data=json.dumps(msg)))
        time.sleep(5)
        x+=1

if __name__ == '__main__':
    main()