# Use Ubuntu as base image for better Android emulator support
FROM ubuntu:20.04

# Avoid interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Set environment variables
ENV PYTHON_VERSION=3.9
ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH=${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/emulator
ENV APPIUM_VERSION=2.0.0
ENV NODE_VERSION=18

# Install required packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    openjdk-11-jdk \
    curl \
    git \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-dev \
    python3-pip \
    build-essential \
    nodejs \
    npm \
    qemu-kvm \
    libvirt-daemon-system \
    libvirt-clients \
    bridge-utils \
    cpu-checker \
    && rm -rf /var/lib/apt/lists/*

# Install Chrome dependencies and Chrome itself
RUN apt-get update && apt-get install -y \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libatspi2.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libexpat1 \
    libgbm1 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libx11-6 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxkbcommon0 \
    libxrandr2 \
    xdg-utils \
    && wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install \
    && rm google-chrome-stable_current_amd64.deb

# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash - \
    && apt-get install -y nodejs

# Install Appium
RUN npm install -g appium@${APPIUM_VERSION} \
    && npm install -g appium-doctor

# Download and install Android SDK
RUN mkdir -p ${ANDROID_HOME} \
    && cd ${ANDROID_HOME} \
    && wget https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip \
    && unzip commandlinetools-linux-*_latest.zip \
    && rm commandlinetools-linux-*_latest.zip \
    && mkdir -p cmdline-tools/latest \
    && mv cmdline-tools/* cmdline-tools/latest/ 2>/dev/null || true

# Accept licenses and install Android SDK packages
RUN yes | sdkmanager --licenses \
    && sdkmanager "platform-tools" "platforms;android-33" "build-tools;33.0.0" \
    && sdkmanager "system-images;android-33;google_apis;x86_64"

# Create an Android Virtual Device
RUN avdmanager create avd \
    --name test_device \
    --package "system-images;android-33;google_apis;x86_64" \
    --device "pixel_5"

# Set up Python environment
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Create database directory
RUN mkdir -p /app/database

# Copy your project files
COPY . /app

# Copy database file to dedicated directory
RUN cp /app/test_cases/Employees.db /app/database/ || true

# Create a script to start emulator and run tests
RUN echo '#!/bin/bash\n\
# Start the emulator in the background\n\
emulator -avd test_device -no-audio -no-window -gpu swiftshader_indirect -no-snapshot -no-boot-anim &\n\
\n\
# Wait for the emulator to be ready\n\
adb wait-for-device\n\
\n\
# Start Appium server\n\
appium --allow-insecure chromedriver_autodownload &\n\
\n\
# Wait for Appium to start\n\
sleep 10\n\
\n\
# Run the tests\n\
python3 -m pytest "$@"\n\
' > /app/run_tests.sh \
    && chmod +x /app/run_tests.sh

# Set the default command
CMD ["/app/run_tests.sh"]