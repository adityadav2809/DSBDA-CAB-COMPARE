# Cab Fare Comparator

## Overview

The **Cab Fare Comparator** is a Python-based application that compares fares for different cab services like Uber, Ola, Rapido, InDrive, and Jugnoo based on the selected ride type (Mini, Sedan, SUV, Auto, Bike). The application allows users to input their starting point and destination, calculates the distance and ETA using the Google Maps API, and provides fare estimates for different cab services. The app also allows users to view their recent search history.

## Features

- **Fare Comparison:** Compare fares for different ride types and cab services.
- **Google Maps Integration:** Calculate distance and estimated time of arrival (ETA) between two locations using Google Maps API.
- **Search History:** Save and view recent searches, including start and end points, ride type, distance, ETA, and fare.
- **Interactive Menu:** Easy-to-use terminal-based interface for fare comparison and viewing recent searches.

## Requirements

- Python 3.6+
- Google Maps API Key
- `dotenv` package for loading environment variables
- `googlemaps` package for Google Maps API integration
- `readchar` package for capturing keypress inputs

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cab-fare-comparator.git
   cd cab-fare-comparator
