FROM docker.io/tensorflow/tensorflow:2.13.0-gpu

USER root

# Install dependencies
RUN apt-get update && DEBIAN_FRONTEND="noninteractive" TZ="Europe/Stockholm" apt-get install -y python3 python3-pip postgresql libpq-dev npm wget vim git fish
RUN python3 -m pip install --upgrade pip
RUN pip3 install datacube geojson geopandas folium ipyleaflet descartes fiona rioxarray pycrs gpytorch torch torchvision jupyterlab ipympl ipyleaflet jupyter_bokeh jupyterlab-geojson dask jupyterlab_theme_solarized_dark jupyterthemes pandas shapely pyproj rtree tslearn fastdtw statsmodels h5py pycolonies
RUN npm install --global yarn
RUN jupyter notebook --generate-config

# Install Colonies
ENV PATH="$PATH:/root/go/bin" 
RUN cd /root; wget https://go.dev/dl/go1.20.7.linux-amd64.tar.gz; tar -xzf go1.20.7.linux-amd64.tar.gz;git clone https://github.com/colonyos/colonies.git; cd colonies; make; make install; cd ..; rm -rf go; rm -rf colonies; rm go1.20.7.linux-amd64.tar.gz
RUN mkdir -p /root/.config/fish/

# Post install
COPY ./post_install.sh /bin/post_install.sh
RUN /bin/post_install.sh

# Change shell to fish
SHELL ["fish", "--command"]
RUN chsh -s /usr/bin/fish
ENV SHELL /usr/bin/fish

ENV JUPYTER_TOKEN hej

CMD ["jupyter", "lab", "--allow-root", "--ip", "0.0.0.0", "--notebook-dir", "/root"]
