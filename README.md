
# Chicken Disease Classification Project

Chicken coccidiosis is a common intestinal disease caused by protozoan parasites from the genus Eimeria. Seven species of this genus can affect chickens, each with different pathogenic characteristics and targeting a specific intestinal location. The parasites rapidly multiply, damaging the intestinal lining, preventing chickens from absorbing nutrients from their food. Vaccination, preventative medication, and good flock management practices can help control the disease. 

**The disease is a major menace to the global poultry industry and hampers chicken's productivity and welfare.**

The aim of this machine learning project is to identify the disease of the chicken based on the fecal image of the chicken. The model can determine whether the chicken is infected with Coccidiosis or not, by just analysing the image of the fecal matter of the chicken.
## ⚒️ Workflow

The workflow defines the way the components and pipeline is constructed in the project. The basic workflow followed in this project is as follows:

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
## ⚙️ Tech Stack

**Programming Language:** Python

**Packages used:** Tensorflow, Keras, Flask, Flask-Cors, DVC(Data-Version-Control), Pandas, Numpy, Matplotlib, Seaborn, Streamlit, Scipy




## 💻 How to run?

#### **STEPS,-**

**Step 1:** Clone this repository
```bash
https://github.com/krishanwalia30/Chicken-Disease-Classification-Project
```

**Step 2:** Create a conda environment inside the repository
```bash
conda create -n cnncls python=3.8 -y
```
```bash
conda activate cnncls
```

**Step 3:** Install the requirements
```py
pip install -r requirements.txt
```
```py
# Finally run the following command
python app.py
```

**Step 4:** See the project running

```bash
open: https://localhost/8000
```
## 📚  Outcome

* Learned to create an end-to-end machine learning pipeline.
* Created different modules and components for different stages in pipeline development
* Learned about Data Version Control (DVC)
* Integrated DVC with the project to make it more efficient.
* Learned to create a Flask webapp for the model.
* Discovered the functionalities of Streamlit.
* Deployed the webapp successfully on Streamlit.
* Developed Continuous Integration and Development pipeline.




## 🧮 Features

- CNN Classifier with accuracy of *0.7982*
- Image upload on the web app interface and decode at the server backend.
- Model can be trained from the webapp interface as well.
- Cross platform



## 🚀 Deployment

The project is deployed as a webapp using Streamlit.

Link: https://chicken-disease-classification-project.streamlit.app/



## 🧾 Appendix

#### Running the DVC:
Run the following command in the main project command prompt,-
```py
dvc init
dvc repro
```

#### Running the Tensorboard
Run the following command in the main project command prompt,-
```py
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
```