# -*- coding: utf-8 -*-
"""
Data Fetcher Module - Binance Public API Client
Author: Wanzhen Fu
Description: Retrieves real-time tick data from Binance REST API
"""

import json
import urllib.request
import time


def get_data(symbol):
    """
    Fetch ticker data from Binance public API.
    
    Args:
        symbol (str): Cryptocurrency symbol ('btc', 'ltc', 'eth', etc.)
        
    Returns:
        dict: Contains 'time' (timestamp) and 'ticker' (last price)
    """
    # Map common symbols to Binance trading pairs
    symbol_map = {
        'btc': 'BTCUSDT',
        'ltc': 'LTCUSDT',
        'eth': 'ETHUSDT',
        'bnb': 'BNBUSDT',
        'xrp': 'XRPUSDT'
    }
    
    trading_pair = symbol_map.get(symbol.lower(), f'{symbol.upper()}USDT')
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={trading_pair}'
    
    try:
        response = urllib.request.urlopen(url, timeout=5)
        data = response.read().decode('utf-8')
        json_data = json.loads(data)
        
        # Get current timestamp
        current_time = str(int(time.time()))
        
        result = {
            'time': current_time,
            'ticker': json_data['price']
        }
        return result
        
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return {'time': str(int(time.time())), 'ticker': '0'}
