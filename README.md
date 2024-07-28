# Uber_Fare_Price_prediction
This is the Final project for Uber Fare Price Prediction


The project is about Uber price prediction. In this project, we're looking to predict the fare for their future travel when Uber is used. Uber delivers service to lakhs of customers daily. Now it becomes really important to manage their data properly to come up with new business ideas to get best results. Eventually, it becomes really important to estimate the fare prices accurately.

The datset contains the following fields:

Unnamed 0 - a unique identifier for each trip
key - Date and Time
fare_amount - the cost of each trip 
pickup_datetime - date and time when the meter was engaged
pickup_longitude - the longitude where the meter was engaged
pickup_latitude - the latitude where the meter was engaged
dropoff_longitude - the longitude where the meter was disengaged
dropoff_latitude - the latitude where the meter was disengaged
passenger_count - the number of passengers in the vehicle

Objective:
Understand the Dataset & cleanup (if required).
Build Regression models to predict the fare price of uber ride.



Understand Data & Cleanup
   The data provied is newyork city ride details and its price. Removing the unwanted columns like Unnamed & key.
   Read the CSV file and load it to Dataframe
   Removing the unwanted data with 0 in pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude ny making it NaN, as we cannot do data imputation on latitude and logitude data.
   After which are doing data imputation on Passenger count with the mode value as it ia categorical column

Data Engineering & Data Preprocessing:
   We are converting Pick Date to date column and seperate the data to day,month,year,week,quarter and week day as part of data engineering.
   Car Type column was created using the passenger count column,based the number of customers.
   We are using encoding technique(LabelEncoder) to convert the alphabetical data to numberic(day_name & Car_type).
   Checking the pickup_latitude,dropoff_latitude is within the range of -90 to 90,if not we are removing those records as well.
   Checking the pickup_longitude,dropoff_longitude is within the range of -180 to 180,if not we are removing those records as well.
   Using the latitude & longitude we are finding the distance travelled and adding it as a column.
   Pickup time as been removed as we seperated that column to simple columns

Data Manipulation
   Splitting the data intro training & testing sets
   Testing a Linear Regression model
   Testing a KNeighborsRegressor model
   Testing a DecisionTreeRegressor model
   Testing a GradientBoostingRegressor model  
   Testing a RandomForestRegressor model
   Testing a XGBRegressor model
   Testing a CatBoostRegressor model
   Caculated the score and MSE values and found the CatBoostRegressor model is the best fit model

Web Application:
   Generate a Pickle file 
   Using stremlit create a application with basic search criteria
   Generate the input parameters for model prediction
   Run the model the generated value and predict the price
   

   
   
   




