FROM amazon/aws-lambda-python:3.12

# Install chrome dependencies
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm jq unzip

# Copy chrome and chromedriver
COPY ./chromedriver-linux64 ./chromedriver-linux64
COPY ./chrome-headless-shell-linux64 ./chrome-headless-shell-linux64
COPY ./test.py ./test.py

RUN pip install selenium

