# Cattle Data Analysis 🐂:brazil:

This repository contains the code and data used to perform an analysis of cattle livestock in Brazil, using data from the Brazilian Institute of Geography and Statistics (IBGE).
# Getting Started

To reproduce the analysis, you will need to download the data from the IBGE website. The data used in this analysis can be found [here](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3).
# Data Analysis 💻🔍

The following steps were taken to analyze the data:

    - Importing data from IBGE api
    - Checking data types and NaN values
    - Plotting Brazil's cattle livestock timeseries
    - Yearly percentage changes (%) histogram analysis
    - Breaking down the analysis from country (Brasil) into regions (Norte, Nordeste, Centro-Oeste, Sudeste and Sul)
    - Analyzing Norte region and Amazon states (Amazon legal borders)
    - Plotting top 10 mesoregions, considering cattle livestock increase rates

# Results 📈🐂

The analysis showed a consistency on the increase of cattle livestock on Brazil over years. Centro-Oeste and Norte regions stand out as the main cattle producers, with continuously increase on their livestock numbers. Another meaningful result was that the top 10 increase rates of cattle livestock of all time series belongs to mesoregions inside the legal borders of Amazon forest.

For more details on the methodology and results (plots and graphs also), please refer to the Jupyter notebook [here](https://github.com/rpacco/cattlebr_data/blob/main/cattlebr_studies.ipynb).