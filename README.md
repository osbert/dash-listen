# dash-listen
Docker container to forward Amazon Dash button presses to arbitrary URLs

# Usage/Quickstart

[HOWTO: Find your Dash's MAC address](https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8)

```
docker pull osbert/dash-listen
docker run -d --net=host -e DASH_MAC_ADDRESS=re:ad:ab:ov:e0 -e URL_CALLBACK=http://url/to/callback osbert/dash-listen
```

Listens for button presses from the given `DASH_MAC_ADDRESS` and issues HTTP GET requests to `URL_CALLBACK`.

