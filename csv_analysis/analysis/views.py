import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from io import BytesIO
import base64
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.conf import settings

def handle_uploaded_file(f):
    try:
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, f.name)
        with open(file_path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return file_path
    except Exception as e:
        print(f"Error handling uploaded file: {e}")
        raise

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                file_path = handle_uploaded_file(request.FILES['file'])
                return redirect(f'/analyze/?file_path={file_path}')
            except Exception as e:
                return render(request, 'analysis/error.html', {'message': str(e)})
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})

def analyze(request):
    file_path = request.GET.get('file_path')
    if not file_path:
        return render(request, 'analysis/error.html', {'message': 'No file path provided.'})

    try:
        data = pd.read_csv(file_path)
    except Exception as e:
        return render(request, 'analysis/error.html', {'message': str(e)})

    # Display the first few rows of the data
    head = data.head().to_html()

    # Calculate summary statistics
    summary = data.describe().to_html()

    # Calculate additional statistics
    stats = data.select_dtypes(include=['number']).agg(['mean', 'median', 'std']).to_html()

    # Identify missing values
    missing_values = data.isnull().sum()  # Series object of column-wise sum of missing values

    # Handle missing values (simple method: drop rows with missing values)
    data_cleaned = data.dropna()

    # Generate histograms for numerical columns
    histograms = []
    for column in data.select_dtypes(include=['number']).columns:
        plt.figure()
        sns.histplot(data[column].dropna(), kde=True)
        plt.title(f'Histogram for {column}')
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        image_base64 = base64.b64encode(image_png).decode('utf-8')
        histograms.append(image_base64)
        plt.clf()

    context = {
        'head': head,
        'summary': summary,
        'stats': stats,
        'missing_values': missing_values,  # Pass the Series object directly
        'histograms': histograms,
    }
    return render(request, 'analysis/analyze.html', context)
