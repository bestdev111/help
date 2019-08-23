### Curl

Below is a basic bash script example to load test an endpoint:

while true; do sleep 0.01; curl -H "Content-Type: application/json" -X GET www.example.com/someendpoint; echo -e '\n\n\n\n'$(date);done