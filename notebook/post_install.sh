#!/bin/bash

mkdir -p /root/.config/fish
colonies completion fish > /root/.config/fish/config.fish
cd /root; git clone https://github.com/oh-my-fish/oh-my-fish; cd oh-my-fish; bin/install --offline --noninteractive; cd ..; rm -rf oh-my-fish
fish -c "omf install harleen"
