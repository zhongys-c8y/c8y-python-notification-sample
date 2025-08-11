# --- About ---
# Here we are registering a subscriber to the subscription that was created in step 01
# This subscriber will receive all updates from all tenant devices

import asyncio

from c8y_api.app import SimpleCumulocityApp
from c8y_api.model import Subscription
from c8y_tk.notification2 import AsyncListener

subscription_name = 'mySubscription'
subscriber_name = 'kobu'

async def main():
    c8y = SimpleCumulocityApp()
    print("CumulocityApp initialized.")
    print(f"{c8y.base_url}, Tenant: {c8y.tenant_id}, User:{c8y.username}")

    # Create a listener for previously created subscription
    listener = AsyncListener(c8y, subscription_name, subscriber_name)

    # This function is invoked (asynchronously) for each received notification
    async def callback(msg: AsyncListener.Message):
        print(
            f"Received message, ID: {msg.id}, Source: {msg.source}, Action: {msg.action}, Body: {msg.json}"
        )
        await msg.ack()

    # Start listening
    listener_task = asyncio.create_task(listener.listen(callback))

    # The update event is now being processed
    await asyncio.sleep(60)

    # close the listener and wait for it to end.
    await listener.close()
    await listener_task

asyncio.run(main())
