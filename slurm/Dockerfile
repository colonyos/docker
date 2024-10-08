FROM docker.io/tensorflow/tensorflow:2.18.0rc0-gpu

USER root

RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="Europe/Stockholm" apt-get install -y python3 python3-pip npm wget vim
RUN pip3 install jupyterlab jupyterthemes --break-system-packages

# Install NVM (Node Version Manager)
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash \
    && export NVM_DIR="$HOME/.nvm" \
    && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" \
    && nvm install --lts \
    && nvm use --lts

# Ensure nvm is loaded in the environment for all following layers
ENV NVM_DIR=/root/.nvm
ENV NODE_VERSION=12
ENV PATH=$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

# Source nvm and use it to install additional Node.js versions if needed
RUN . "$NVM_DIR/nvm.sh" && nvm install $NODE_VERSION && nvm use $NODE_VERSION
RUN node -v && npm -v

ENV NODE\_OPTIONS --experimental-worker
RUN jupyter notebook --generate-config

RUN DEBIAN_FRONTEND="noninteractive" TZ="Europe/Stockholm" apt-get install -y munge mariadb-client mariadb-server libmariadb-dev slurmdbd slurmd slurmctld libpmix-dev dbus
RUN mysql_install_db --user=mysql --datadir=/var/lib/mysql

# Setup Munge
RUN dd if=/dev/urandom bs=1 count=1024 >/etc/munge/munge.key
RUN chown munge:munge /etc/munge/munge.key
RUN chmod 600 /etc/munge/munge.key

# Setup Slurm environment
RUN mkdir -p /etc/slurm 
COPY cgroup.conf /etc/slurm
COPY slurmdbd.conf /etc/slurm/slurmdbd.conf
COPY slurm.conf /etc/slurm/slurm.conf
COPY entrypoint.sh /entrypoint.sh
RUN mkdir -p /var/run/slurm 
RUN mkdir -p /var/lib/slurm/slurmctld
RUN chmod 755 /var/lib/slurm/slurmctld
RUN mkdir -p /var/lib/slurm/slurmctld
RUN chown -R slurm:slurm /var/lib/slurm/slurmctld
RUN chmod 755 /var/lib/slurm/slurmctld
RUN chmod +x /entrypoint.sh
RUN chmod 755 /var/run/slurm
RUN chmod 600 /etc/slurm/slurmdbd.conf

# Install Apptainer/Singularity
#RUN DEBIAN_FRONTEND="noninteractive" TZ="Europe/Stockholm" apt-get install -y fakeroot libfakeroot libfuse3-3 liblzo2-2 squashfs-tools uidmap

ENV JUPYTER_TOKEN enccs

ENTRYPOINT ["/entrypoint.sh"]
