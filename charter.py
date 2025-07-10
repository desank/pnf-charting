# charter.py

import plotly.graph_objects as go

def create_pnf_chart(pnf_data, ticker, box_size):
    """Creates a Point and Figure chart using Plotly."""
    if not pnf_data:
        print("No P&F data to plot.")
        return

    fig = go.Figure()

    # Separate X's and O's for plotting
    x_columns = [d['column'] for d in pnf_data if d['type'] == 'X']
    x_prices = [d['price'] for d in pnf_data if d['type'] == 'X']
    
    o_columns = [d['column'] for d in pnf_data if d['type'] == 'O']
    o_prices = [d['price'] for d in pnf_data if d['type'] == 'O']

    fig.add_trace(go.Scatter(
        x=x_columns,
        y=x_prices,
        mode='markers',
        marker=dict(symbol='x', color='green', size=10),
        name='Up (X)'
    ))

    fig.add_trace(go.Scatter(
        x=o_columns,
        y=o_prices,
        mode='markers',
        marker=dict(symbol='circle-open', color='red', size=10),
        name='Down (O)'
    ))

    fig.update_layout(
        title=f'Point and Figure Chart for {ticker} (Box Size: {box_size})',
        xaxis_title='Column Number',
        yaxis_title='Price',
        xaxis=dict(
            showgrid=True, 
            gridwidth=1, 
            gridcolor='LightGray',
            tickmode='linear',
            tick0=0,
            dtick=1
        ),
        yaxis=dict(
            showgrid=True, 
            gridwidth=1, 
            gridcolor='LightGray'
        ),
        plot_bgcolor='white'
    )

    fig.show()
