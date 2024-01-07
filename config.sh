#!/bin/bash

# Check for existing SSH keys
if [ -f ~/.ssh/id_rsa ] || [ -f ~/.ssh/id_ed25519 ]; then
    echo "SSH key already exists."
else
    # Generate a new SSH key
    read -p "Enter your GitHub email: " github_email
    ssh-keygen -t rsa -b 4096 -C "$github_email"

    # Start the ssh-agent in the background
    eval "$(ssh-agent -s)"

    # Add your SSH private key to the ssh-agent
    ssh-add ~/.ssh/id_rsa

    echo "SSH key generated and added to ssh-agent."
    echo "Please manually add the public key to your GitHub account."
fi

