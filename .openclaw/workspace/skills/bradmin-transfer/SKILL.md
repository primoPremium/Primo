# Bradmin File Transfer Skill

## Description
Securely transfer files to bradmin_bot using SSH/SCP.

## Connection Details
- Target Host: 16.147.201.24
- Username: ubuntu
- SSH Key: ~/.ssh/bradmin_bot_clawdbot_key.pem
- Target Directory: /home/ubuntu/

## Usage
When the user requests "send that image to bradmin" or similar:

1. Verify the file exists locally
2. Use scp with the private key to transfer:
```bash
scp -i ~/.ssh/bradmin_bot_clawdbot_key.pem [local_file] ubuntu@16.147.201.24:/home/ubuntu/[filename]
```

## Example
Previous successful transfer:
```bash
scp -i ~/.ssh/bradmin_bot_clawdbot_key.pem /etc/security/limits.conf ubuntu@16.147.201.24:/home/ubuntu/limits.conf
```

## Security Notes
- Host key fingerprint (ED25519): SHA256:klkQJx7aZzkiYW5expqjsTqn9Ei/AMa2hwqZ4lV4EvM
- Host has been added to known_hosts

## Validation
Always verify:
1. File exists locally before transfer
2. File permissions are appropriate
3. Target directory has sufficient space