# -*- coding: utf-8 -*-
"""
Data Processor Module - Moving Average Calculator
Author: Wanzhen Fu
Description: Implements sliding window queue for MA(8) calculation
"""

import numpy as np
from collections import deque
import data_fetcher


class DataQueue(object):
    """
    Sliding window queue for calculating moving averages.
    
    Uses a fixed-size deque to maintain the last 8 tick prices
    and calculates their mean efficiently.
    """
    
    def __init__(self):
        self.que = deque()
        self.que_len = 0

    def len_out(self):
        """
        Check if queue has reached maximum size (8).
        
        Returns:
            int: 0 if queue is full (size 8), 1 otherwise
        """
        if self.que_len == 8:
            return 0
        else:
            return 1

    def ldrop(self):
        """Remove the oldest (leftmost) element from queue."""
        self.que.popleft()

    def rpush(self, r_data):
        """
        Add new tick data to the right end of queue.
        
        Filters duplicate data by comparing timestamps.
        Only adds if timestamp differs from the last entry.
        
        Args:
            r_data (dict): Contains 'ticker' (price) and 'time' (timestamp)
        """
        global time_temp

        data = float(r_data['ticker'])
        
        if self.que_len == 0:
            # First entry
            self.que.append(data)
            self.que_len += 1
            time_temp = r_data['time']
        else:
            # Only add if timestamp is different (avoid duplicates)
            if r_data['time'] != time_temp:
                self.que.append(data)
                self.que_len += 1
                time_temp = r_data['time']

    def average(self):
        """
        Calculate the mean of all values in queue.
        
        Returns:
            float: Mean value of queue elements
        """
        return np.mean(self.que)

    def average_eight(self, signal):
        """
        Calculate 8-period moving average for given cryptocurrency.
        
        Fetches new data, maintains sliding window of size 8,
        and returns the current moving average.
        
        Args:
            signal (str): Cryptocurrency symbol ('btc', 'ltc')
            
        Returns:
            float: 8-period moving average
        """
        data = data_fetcher.get_data(signal)
        
        # Remove oldest if queue is full
        if self.len_out() == 0:
            self.ldrop()
        
        # Add new data point
        self.rpush(data)
        
        # Return current average
        return self.average()
