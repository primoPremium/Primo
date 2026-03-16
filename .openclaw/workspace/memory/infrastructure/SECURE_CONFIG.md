# Secure Gateway Configuration

## Required Changes

1. Gateway Configuration:
```json
"gateway": {
  "port": 18789,
  "mode": "local",
  "bind": "lan",
  "url": "wss://52.25.23.10:18789",
  "auth": {
    "mode": "token",
    "token": "e69755ed8dc40202f83f465d31e96ae1d08ff11d78407fc6"
  }
}
```

2. Device Pair Configuration:
```json
"plugins": {
  "entries": {
    "device-pair": {
      "config": {
        "publicUrl": "https://52.25.23.10:18789"
      }
    }
  }
}
```

## Implementation Steps
1. Stop OpenClaw gateway
2. Update configuration
3. Set up SSL certificate
4. Start gateway with new secure config

## Security Notes
- Requires valid SSL certificate
- All connections will be encrypted
- Token authentication preserved