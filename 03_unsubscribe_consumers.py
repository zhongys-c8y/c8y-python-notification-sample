# --- About ---
# Unsubscribing a subscriber (kobu) will clear any unacknowledged messages in the backlog.
from c8y_api.app import SimpleCumulocityApp
subscription_name = 'mySubscription'
subscriber_name = 'kobu'

def main():
    c8y = SimpleCumulocityApp()
    print("CumulocityApp initialized.")
    print(f"{c8y.base_url}, Tenant: {c8y.tenant_id}, User:{c8y.username}")

    token = c8y.notification2_tokens.generate(subscriber=subscriber_name, subscription=subscription_name)
    ## If listener created in step 02 is available, can also get token from listener's _current_uri.
    # token = listener._current_uri[listener._current_uri.find('token=') + 6:]
    c8y.notification2_tokens.unsubscribe(token)


main()



# Use https://github.com/Cumulocity-IoT/cumulocity-python-api/blob/6134a5f5dfdba1fa209c15c2a9971cd4fe9d306d/c8y_api/model/notification2.py#L309
