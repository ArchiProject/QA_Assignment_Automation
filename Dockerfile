# # Use the official Python base image
# FROM python:3.11-slim
#
# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
#
# # Install required system dependencies
# RUN apt-get update && apt-get install -y \
#     wget \
#     unzip \
#     curl \
#     gnupg \
#     firefox-esr \
#     xvfb \
#     && apt-get clean
#
# # Install Geckodriver
# RUN GECKODRIVER_VERSION="v0.33.0" && \
#     wget "https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz" && \
#     tar -xvzf "geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz" && \
#     mv geckodriver /usr/local/bin/ && \
#     chmod +x /usr/local/bin/geckodriver && \
#     rm "geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz"
# RUN geckodriver --version
# ENV PATH="/usr/local/bin:${PATH}"
#
# # Create working directory
# WORKDIR /app
#
# # Copy project files
# COPY . /app
#
# # Install Python dependencies
# RUN pip install --no-cache-dir -r requirements.txt
#
# # Default command to run test suite
# CMD ["behave"]
# Use the official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install required system dependencies for Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    libx11-xcb1 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libasound2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    fonts-liberation \
    libappindicator3-1 \
    libnss3 \
    lsb-release \
    libu2f-udev \
    && apt-get clean

# Install Google Chrome
RUN GOOGLE_CHROME_VERSION="google-chrome-stable_current_amd64.deb" && \
    wget https://dl.google.com/linux/direct/$GOOGLE_CHROME_VERSION && \
    dpkg -i $GOOGLE_CHROME_VERSION && \
    apt-get -y install -f && \
    rm $GOOGLE_CHROME_VERSION

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION="113.0.5672.63" && \
    wget https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Create working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to run test suite
CMD ["behave"]
