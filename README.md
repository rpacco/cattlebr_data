# Cattle Data Analysis 🐂:brazil:

This repository contains the code and data used to perform an analysis of cattle livestock in Brazil, using data from the Brazilian Institute of Geography and Statistics (IBGE).
# Getting Started

To reproduce the analysis, you will need to download the data from the IBGE website. The data used in this analysis can be found [here](https://servicodados.ibge.gov.br/api/docs/agregados?versao=3).

Amazon deforestation rates were gathered trough PRODES (in English, "Project for Monitoring Deforestation in the Amazon by Satellites") and can be found [here](http://www.obt.inpe.br/OBT/assuntos/programas/amazonia/prodes).
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

Due to it, a web application was built to analyze the correlation between Brazilian cattle livestock and Amazon mesoregions (selected by the user) over time. In addition, a map is provided to show the location of the selected mesoregion and some important data, including:

    Mesoregion selected by the user
    State in which the mesoregion is located
    Deforestation of the mesoregion state in the current year
    Cumulative deforestation in the mesoregion state (since available data)

Please note that the above items will be displayed in the map (hovering text) along with the mesoregion.

## Web app - [link](https://cattlebr.onrender.com)

For more details on the methodology and results (plots and graphs also), please refer to the Jupyter notebook [here](https://github.com/rpacco/cattlebr_data/blob/main/cattlebr_studies.ipynb).