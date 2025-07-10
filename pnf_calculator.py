# pnf_calculator.py

import numpy as np

def calculate_pnf_data(data, box_size, reversal_amount):
    """
    Calculates the Point and Figure data from OHLC data.
    This implementation uses the traditional method considering high and low prices.
    """
    if data.empty or len(data) < 2:
        return []

    pnf_columns = []
    
    # Use the first day's close to establish the initial box level
    initial_price = data['close'].iloc[0]
    box_level = np.round(initial_price / box_size) * box_size

    # Determine initial trend based on the second day's price movement
    if data['high'].iloc[1] > box_level + box_size:
        trend = 'up'
        current_col = [{'price': box_level, 'type': 'X'}]
        current_level = box_level
        # Fill initial boxes
        while current_level < data['high'].iloc[1]:
            current_level += box_size
            current_col.append({'price': current_level, 'type': 'X'})

    elif data['low'].iloc[1] < box_level - box_size:
        trend = 'down'
        current_col = [{'price': box_level, 'type': 'O'}]
        current_level = box_level
        # Fill initial boxes
        while current_level > data['low'].iloc[1]:
            current_level -= box_size
            current_col.append({'price': current_level, 'type': 'O'})
    else: # Not enough movement to establish a trend yet
        # We'll start checking from the next day
        trend = None
        current_col = []
        current_level = box_level

    for index, row in data.iloc[2:].iterrows():
        high = row['high']
        low = row['low']

        if trend == 'up':
            # How many new boxes can we add to the current uptrend?
            num_boxes = int((high - current_level) / box_size)
            if num_boxes > 0:
                for _ in range(num_boxes):
                    current_level += box_size
                    current_col.append({'price': current_level, 'type': 'X'})
            
            # Check for reversal
            reversal_price = current_level - (reversal_amount * box_size)
            if low < reversal_price:
                if current_col:
                    pnf_columns.append(current_col)
                
                trend = 'down'
                num_boxes_rev = int((current_level - low) / box_size)
                current_col = []
                # The first box of the new column is one below the high of the last column
                current_level = current_level - box_size
                for i in range(num_boxes_rev):
                    current_col.append({'price': current_level, 'type': 'O'})
                    if i < num_boxes_rev -1:
                         current_level -= box_size


        elif trend == 'down':
            # How many new boxes can we add to the current downtrend?
            num_boxes = int((current_level - low) / box_size)
            if num_boxes > 0:
                for _ in range(num_boxes):
                    current_level -= box_size
                    current_col.append({'price': current_level, 'type': 'O'})

            # Check for reversal
            reversal_price = current_level + (reversal_amount * box_size)
            if high > reversal_price:
                if current_col:
                    pnf_columns.append(current_col)

                trend = 'up'
                num_boxes_rev = int((high - current_level) / box_size)
                current_col = []
                # The first box of the new column is one above the low of the last column
                current_level = current_level + box_size
                for i in range(num_boxes_rev):
                    current_col.append({'price': current_level, 'type': 'X'})
                    if i < num_boxes_rev - 1:
                        current_level += box_size
        
        else: # Trend not established yet
            if high > current_level + box_size:
                trend = 'up'
                while current_level < high:
                    current_level += box_size
                    current_col.append({'price': current_level, 'type': 'X'})
            elif low < current_level - box_size:
                trend = 'down'
                while current_level > low:
                    current_level -= box_size
                    current_col.append({'price': current_level, 'type': 'O'})


    if current_col:
        pnf_columns.append(current_col)

    # Flatten the columns into a single list with column indices
    pnf_data = []
    for col_idx, column in enumerate(pnf_columns):
        for point in column:
            pnf_data.append({
                'column': col_idx,
                'price': point['price'],
                'type': point['type']
            })
            
    return pnf_data
