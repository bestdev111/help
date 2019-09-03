## Curl

### Cookbook (General Examples)

Below taken from the [Curl Cookbook](https://catonmat.net/cookbooks/curl)

* Make a POST Request (TLDR: Use -X POST argument)*
* Add POST Data to a Request (TLDR: Use -d var=val argument)*
* Construct a Query String (TLDR: Use -G argument)*
* Add HTTP Headers (TLDR: Use -H 'Header: Value' argument)*
* Change the User Agent (TLDR: Use -A 'User Agent' argument)*
* Set Cookies (TLDR: Use -b name=value argument)*
* Add a Referrer (TLDR: Use -e URL argument)*
* Follow a 3XX Redirect (TLDR: Use -L argument)*
* Use the Basic HTTP Authentication (TLDR: Use -u user:pass argument*)
* Print the Response Headers (TLDR: Use -i argument)*
* Use a Proxy (TLDR: Use -x protocol://host:port argument)*
* Ignore the SSL Certificate (TLDR: Use -k argument)*
* Make Curl Silent (TLDR: Use -s argument)*
* Save the Response to a File (TLDR: Use -o file argument)*
* Make Curl Slow (TLDR: Use --limit-rate 8k (8KB/sec) argument)*
* Debug Curl Requests (TLDR: Use -v or --trace arguments)*
* Make a GET Request (TLDR: No arguments required, it's the default)*

### Pass JSON as a request parameter

```
curl \
  -G \
  -H "Authorization: $AUTH_TOKEN" \
  -H "Content-type: application/json" \
  -d "filter=[{\"name\":\"email\",\"op\":\"eq\",\"val\":\"richardgray@yahoo.com\"}]" \
   https://example.com/resource
```

# Upload a base64 string from file

```
curl -H "Authorization: $AUTH_TOKEN" -H "Content-Type: application/json" -d @./example.json -X POST https://example.com/resource
```

# Upload a base64 string inline

```
curl -H "Authorization: $AUTH_TOKEN" -H "Content-Type: application/json" -d '{"identity_card": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAABCAYAAAD5PA/NAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAACXBIWXMAAAsTAAALEwEAmpwYAAAED2lUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS40LjAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICAgICA8eG1wTU06RGVyaXZlZEZyb20gcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICA8c3RSZWY6aW5zdGFuY2VJRD54bXAuaWlkOjk2QkM3NjMxOTJCQTExREY4QzAxODZFMzY4MjU3NkQwPC9zdFJlZjppbnN0YW5jZUlEPgogICAgICAgICAgICA8c3RSZWY6ZG9jdW1lbnRJRD54bXAuZGlkOjk2QkM3NjMyOTJCQTExREY4QzAxODZFMzY4MjU3NkQwPC9zdFJlZjpkb2N1bWVudElEPgogICAgICAgICA8L3htcE1NOkRlcml2ZWRGcm9tPgogICAgICAgICA8eG1wTU06RG9jdW1lbnRJRD54bXAuZGlkOjk2QkM3NjM0OTJCQTExREY4QzAxODZFMzY4MjU3NkQwPC94bXBNTTpEb2N1bWVudElEPgogICAgICAgICA8eG1wTU06SW5zdGFuY2VJRD54bXAuaWlkOjk2QkM3NjMzOTJCQTExREY4QzAxODZFMzY4MjU3NkQwPC94bXBNTTpJbnN0YW5jZUlEPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBDUzUgV2luZG93czwveG1wOkNyZWF0b3JUb29sPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4Kql2HygAAABBJREFUCB1jYIAATiAFwgwAAI8AE1czr0wAAAAASUVORK5CYII="}' -X POST https://example.com/resource
```

# Include headers in output

```
curl --include https://example.com/resource
```

### Load Testing

Below is a basic bash script example to load test an endpoint using Curl

```
while true; do sleep 0.01; curl -H "Content-Type: application/json" -X GET www.example.com/someendpoint; echo -e '\n\n\n\n'$(date);done
```

