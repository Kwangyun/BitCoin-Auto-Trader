# Bitcoin Trading Bot

A Python program that automatically buys and sells Bitcoin, using various short-term trading strategies to gain 7%+ annual income.

## Features
- Implements various short-term trading strategies such as volatility, golden cross, and moving average line strategies to signal the optimal time to buy and sell coins.
- Uses Upbit API to fetch live coin data.
- Uses Slack API to send notifications upon bitcoin purchase and selling.

## Usage
This program is designed to automate the process of buying and selling bitcoin, using short-term trading strategies to maximize profits. To use this program, you must first create an account with Upbit and Slack to obtain authentication keys for the Upbit API and Slack API respectively. It uses live coin data from Upbit API and sends notifications through Slack API to keep you updated on its actions.

## Strategies
The program implements the following short-term trading strategies to signal the optimal time to buy and sell coins:
1. Volatility Trading: A strategy that buys low and sells high based on the fluctuations in the coin's price.
2. Golden Cross Trading: A strategy that buys when a short-term moving average crosses above a long-term moving average and sells when the opposite occurs.
3. Moving Average Line Trading: A strategy that buys when the price crosses above the moving average line and sells when the price crosses below the moving average line.

## Requirements
- Python 3.x
- Upbit API Key
- Slack API Key

## Disclaimer
Please note that the results achieved by using this program may vary and are not guaranteed. Trading cryptocurrencies can be volatile and carry a high level of risk. The author and contributors of this program are not responsible for any financial losses that may result from using this program. It is recommended to thoroughly research and understand the risks involved in cryptocurrency trading before making any investment decisions.

