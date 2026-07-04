# Binance Futures Testnet Trading Bot

## Overview

This project is a Python-based trading bot developed for the Binance Futures Testnet.

## Features

- Place MARKET orders
- Place LIMIT orders
- BUY and SELL support
- Command Line Interface (CLI)
- Input validation
- Logging
- Error handling

## Project Structure

```
TradingBot/
│
├── bot/
├── logs/
├── cli.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

## Installation

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file.

Replace the placeholder values with your own Binance Futures Testnet API credentials.

```env
API_KEY=YOUR_TESTNET_API_KEY
API_SECRET=YOUR_TESTNET_API_SECRET
```

## Running the Project

MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

## Note

This application requires valid Binance Futures Testnet API credentials.

The placeholder values in the `.env` file should be replaced with valid Testnet API keys before running the application.