# CSV Analysis Web Application

This web application is built using Django and provides functionality to upload CSV files, perform data analysis using pandas and numpy libraries, and visualize the results on the web interface.

## Features

- **File Upload**: Users can upload CSV files through a web form.
- **Data Analysis**: Basic data analysis tasks are performed on the uploaded CSV files, including:
  - Displaying the first few rows of the data.
  - Calculating summary statistics (mean, median, standard deviation) for numerical columns.
  - Identifying and handling missing values.
- **Data Visualization**: Visualizations such as histograms for numerical columns are generated using matplotlib and seaborn.
- **User Interface**: A user-friendly interface built with Django templates displays the analysis results and visualizations.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- Pip package manager installed.

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd csv_analysis
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On macOS/Linux: source venv/bin/activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:

   Open your web browser and go to `http://localhost:8000/` to use the application.

### Usage

1. **Upload CSV File**:
   - Click on the "Upload CSV" button on the home page.
   - Select a CSV file from your local system and click "Submit".

2. **View Analysis**:
   - After uploading, you will be redirected to a page showing analysis results.
   - This includes displaying the first few rows, summary statistics, missing values count, and histograms for numerical columns.

3. **Repeat**:
   - You can upload different CSV files and analyze them as needed.


## Technology Stack

- **Backend**: Django
- **Frontend**: Django Templates, HTML, CSS
- **Libraries**: pandas, numpy, matplotlib, seaborn

