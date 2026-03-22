# FitWell Health Analytics

An end-to-end health and fitness analytics pipeline built with Python, SQL, and Highcharts.

## Overview

FitWell collects, cleans, and visualizes wellness data across four key metrics: workout frequency, calories burned, sleep quality, and mental health scores. Built as a portfolio project for the University of the Pacific M.S. Data Science program.

## Tech Stack

- **Python** — data pipeline (fetch, clean, transform)
- - **SQL** — database schema and queries
  - - **JavaScript / Highcharts** — interactive dashboard
    - - **JSON** — data exchange between pipeline and dashboard
      - - **Git / GitHub** — version control
       
        - ## Project Structure
       
        - ```
          fitwell-health-analytics/
          ├── pipeline/
          │   ├── fetch.py        # Fetches and generates fitness data
          │   ├── clean.py        # Cleans and structures data for dashboard
          │   └── main.py         # Entry point to run full pipeline
          ├── dashboard/
          │   └── index.html      # Interactive Highcharts dashboard
          ├── data/
          │   ├── fitness_data.json   # Raw data output
          │   └── clean_data.json     # Cleaned data for dashboard
          ├── sql/
          │   └── schema.sql      # Database schema
          └── requirements.txt
          ```

          ## How to Run

          1. Clone the repo
          2. ```bash
             git clone https://github.com/Dtumuhairwe/fitwell-health-analytics.git
             cd fitwell-health-analytics
             ```

             2. Install dependencies
             3. ```bash
                pip3 install requests
                ```

                3. Run the pipeline
                4. ```bash
                   python3 pipeline/fetch.py
                   python3 pipeline/clean.py
                   ```

                   4. Launch the dashboard
                   5. ```bash
                      python3 -m http.server 8000
                      ```
                      Then open `http://localhost:8000/dashboard/index.html` in your browser.

                      ## Dashboard Metrics

                      | Metric | Chart Type | Description |
                      |--------|-----------|-------------|
                      | Workout Frequency | Stacked Bar | Sessions per week by type |
                      | Calories Burned | Area Chart | Daily average vs target |
                      | Sleep Quality | Spline Line | Nightly score (0-100) |
                      | Mental Health | Spline Line | Weekly wellness score |

                      ## Author

                      **Doreen Tumuhairwe**
                      M.S. Data Science — University of the Pacific, Stockton CA
                      [LinkedIn](https://linkedin.com/in/dtumuhairwe) | [GitHub](https://github.com/Dtumuhairwe)
