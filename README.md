# Project Title : Cement Strength Prediction
## Understanding the dataset
**Cement (component 1)** (kg in a m^3 mixture): The amount of cement, measured in kilograms, present in one cubic meter of the concrete mixture. Cement is a binding material responsible for providing strength and durability to concrete.

**Blast Furnace Slag (component 2) (kg in a m^3 mixture)**: The quantity of blast furnace slag, measured in kilograms, included in one cubic meter of the concrete mixture. Blast furnace slag is a byproduct of the iron and steel industry and is commonly used as a supplementary cementitious material in concrete production.

**Fly Ash (component 3) (kg in a m^3 mixture)**: The amount of fly ash, measured in kilograms, added to one cubic meter of the concrete mixture. Fly ash is a waste product from coal combustion and is often used as a partial replacement for cement in concrete to enhance its properties.

**Water (component 4) (kg in a m^3 mixture)**: The volume of water, measured in kilograms, incorporated in one cubic meter of the concrete mixture. Water is required for the hydration process of cement and is crucial for the hardening of concrete.

**Superplasticizer (component 5) (kg in a m^3 mixture)**: The quantity of superplasticizer, measured in kilograms, utilized in one cubic meter of the concrete mixture. Superplasticizers are chemical admixtures that are added to concrete to enhance its workability and flow without compromising its strength.

**Coarse Aggregate (component 6) (kg in a m^3 mixture)**: The weight of coarse aggregate, measured in kilograms, present in one cubic meter of the concrete mixture. Coarse aggregate consists of larger particles such as crushed stone, gravel, or recycled concrete, and provides strength and stability to the concrete.

**Fine Aggregate (component 7) (kg in a m^3 mixture)**: The amount of fine aggregate, measured in kilograms, included in one cubic meter of the concrete mixture. Fine aggregate typically consists of sand and is responsible for filling the gaps between coarse aggregates, contributing to the overall strength and workability of concrete.

**Age (day)**: The age of the concrete specimen, measured in days, at which the compressive strength is determined. Concrete gains strength over time as the hydration process progresses, so the age of the concrete is an important factor in assessing its compressive strength.

**Concrete compressive strength (MPa, megapascals)**: The compressive strength of the concrete specimen, measured in megapascals (MPa). Compressive strength is a fundamental property of concrete that indicates its ability to withstand loads or pressure without breaking.

1. Problem Statement-
    To accurately predict the strength of new concrete mixtures based on their input characteristics.

2. Sources:
   (a) Date:    4th April 2024. (Project Date)

3. Dataset-

    data that can be downloaded at:
https://www.kaggle.com/datasets/prathamtripathi/regression-with-neural-networking

The feature set includes:

Cement
Blast Furnace Slag
Fly Ash
Water
Super-plasticizer
Coarse Aggregate
Fine Aggregate
Age

The target set is:
Strength of the Cement


4. Techniques and Algorithms used -

     1.In this project Implemented ML Techniques Like Linear Regression, Random Forest Regressor, XGboost Regressor To To accurately predict the strength of new concrete mixtures based on their input characteristics

5. Conclusions-
    1. Model_1:
        1. Got MSE 23.85 and R2 0.90 on test data using Xgboost regressor.
        2. We can also reduce this loss by using deep learning algorithms however at the cost of computational expense.



         

