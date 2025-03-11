# Bright Blue Add-on for Home Assistant

This add-on integrates the Bright Blue pool monitoring system with Home Assistant.

## Installation

1. Go to Home Assistant → Settings → Add-ons → Add-on Store.
2. Click "Repositories" (bottom right) and enter: https://github.com/TNogueira18/Bright-Blue-Add-ons
4. Click "Add", then find and install the Bright Blue Add-on.
5. Set the ESP device's IP in the Configuration.
6. Start the add-on and check the logs.

## API Endpoints

- **GET** `/api` → Returns all sensor data.
- **POST** `/api/ph` → Updates the pH value.

Enjoy!
