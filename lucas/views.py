import io, base64
from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def analysis(request):
    x = np.arange(0, 10, 1)
    y = np.random.rand(10)
    df = pd.DataFrame(np.column_stack([x, y]), columns=['x', 'y'])
    
    fig, ax = plt.subplots()
    df.plot(kind='scatter', x='x', y='y', ax=ax)
    
    image_bytes = io.BytesIO()
    fig.savefig(image_bytes)

    image_base64 = base64.b64encode(image_bytes.getvalue()).decode()

    return render(request, 'analysis/lucas.html', { 'chart': image_base64 })
