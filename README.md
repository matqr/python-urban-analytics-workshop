# python-urban-analytics-workshop

# !REPO STILL UNDER DEVELOPMENT!
Workshop about Python for Urban Analytics as part of the Singapore-ETH Centre (SEC) activities for the National Coding Week 2024.

# Takeaway
TODO

# Content

The slides used for this workshop can be found in this repo in the file `20240916-python-workshop.pdf`.

# Requirements

Install Python 3.10.14 and run

```
python install -r requirements.txt
```

Make sure you have at least **40GB** of free space.

# Data: Global Streetscapes

We will use the Global Streetscapes dataset! With more than 9 million images from 688 cities and 300+ features, it's the right place to start playing with SVIs.

- [Project](https://ual.sg/project/global-streetscapes/)
- [Paper](https://www.sciencedirect.com/science/article/pii/S0924271624002612)
- [Dataset](https://huggingface.co/datasets/NUS-UAL/global-streetscapes)
- [Code and wiki](https://github.com/ualsg/global-streetscapes)

## Download the dataset from huggingface
As mentioned in the [Dataset card](https://huggingface.co/datasets/NUS-UAL/global-streetscapes), please avoid using `git clone` to download the repo as Git stores the files twice and will double the disk space usage to 124+ GB.

Run the file `1-download-huggingface.py` to download the `data/` folder as well as the additional files `cities688.csv` and `info.csv`.

Then, follow the notebook `2-data_download.ipynb` to download the SVIs.

# Semantic Segmentation
The notebook for this is hosted on kaggle:
https://www.kaggle.com/code/matiasqr/semantic-segmentation

# Human Perception
The notebook for this is hosted on kaggle:
https://www.kaggle.com/code/matiasqr/human-perception

# References

- Ito, K., Kang, Y., Zhang, Y., Zhang, F. & Biljecki, F. (2024). Understanding urban perception with visual data: A systematic review. Cities, 152, 105169. https://doi.org/10.1016/j.cities.2024.105169
- Hou, Y., Quintana, M., Khomiakov, M., Yap, W., Ouyang, J., Ito, K., Wang, Z., Zhao, T. & Biljecki, F. (2024). Global Streetscapes — A comprehensive dataset of 10 million street-level images across 688 cities for urban science and analytics. ISPRS Journal of Photogrammetry and Remote Sensing, 215, 216–238. https://doi.org/10.1016/j.isprsjprs.2024.06.023
- Hou, Y. & Biljecki, F. (2022). A comprehensive framework for evaluating the quality of street view imagery. International Journal of Applied Earth Observation and Geoinformation, 115, 103094. https://doi.org/10.1016/j.jag.2022.103094

