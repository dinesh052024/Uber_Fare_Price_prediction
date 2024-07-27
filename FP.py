import streamlit as st
from datetime import datetime,timedelta
from geosky import geo_plug
from geopy.distance import geodesic as GD
from geopy.geocoders import Nominatim
import pickle
from catboost import CatBoostRegressor
import boto3
import os

st.image("UBER.jpg")
st.sidebar.image("updp.jpeg")
ak=st.secrets["ak"]
sk=st.secrets["sk"]
st.sidebar.title('Upload/Download file to Cloud S3 bucket')
s3_client=boto3.client('s3',aws_access_key_id=ak,aws_secret_access_key=sk)
#up_file = st.sidebar.file_uploader("Choose a file to upload")
folder_path='C:/Users/Praveen/Downloads'
#folder_path='.'
filenames = os.listdir(folder_path)
selected_filename = st.sidebar.selectbox('Select a file from Downloads Folder', filenames)
up_file= os.path.join(folder_path, selected_filename)
if up_file is not None and st.sidebar.button('Upload'):
   s3_client.upload_file(up_file, 'mdsfp007', selected_filename) 
   st.sidebar.write("Uploaded Successfully" )
dl_file = st.sidebar.text_input("Please Enter file name to download")
if dl_file is not None and st.sidebar.button('Download'):
   s3_client.download_file('mdsfp007', dl_file, "D://Down_file_s3")
   st.sidebar.write("Downloaded Successfully ")
st.title('Uber Fare price Prediction')

loc=geo_plug.all_State_CityNames('New York')
sub_loc=loc[0:16]
sub_loc_last=loc[-3:]
loc=loc.replace(sub_loc,'')
loc=loc.replace('"','')
loc_list=list(loc.split(","))
curr_loc=st.selectbox('Pickup Location',loc_list)
dest_loc=st.selectbox('Destination Location',loc_list)
pass_cnt=st.selectbox('Passanger Count',(1,2,3,4,5,6,7,8))

if pass_cnt > 0 and pass_cnt < 3:
    car_type =0
elif pass_cnt > 2 and pass_cnt < 5:
    car_type =1
elif pass_cnt >= 5:
    car_type= 2 

geolocator = Nominatim(user_agent="my-geocoder-app")
location_city1 = geolocator.geocode(curr_loc)
location_city2 = geolocator.geocode(dest_loc)
lat_long_city1 = (location_city1.latitude ,location_city1.longitude)
lat_long_city2 = (location_city2.latitude ,location_city2.longitude)
distance = GD(lat_long_city1 , lat_long_city2).km

pickup_lat=lat_long_city1[0]
pickup_lon=lat_long_city1[1]
dropoff_lat=lat_long_city2[0]
dropoff_lon=lat_long_city2[1]

date=datetime.today()
dt=datetime.strptime(str(date),'%Y-%m-%d %H:%M:%S.%f')
year=dt.year
month=dt.month
day=dt.day
hour=dt.hour
min=dt.minute
sec=dt.second
msec=dt.microsecond
dname=dt.strftime("%A")
if dname=='Thursday':
  day_name=4
elif dname=='Friday':
  day_name=0
elif dname=='Saturday':
  day_name=2
elif dname=='Sunday':
  day_name=3
elif dname=='Monday':
  day_name=1
elif dname=='Tuesday':
  day_name=5
elif dname=='Wednesday':
  day_name=6
week_of_year=dt.isocalendar().week
qut=(month-1)//3 + 1

a=[pickup_lon,pickup_lat,dropoff_lon,dropoff_lat,pass_cnt,car_type,year,month,day,day_name,week_of_year,hour,min,sec,qut,distance]
if None not in a and st.button('predict'):
    feature=[pickup_lon,pickup_lat,dropoff_lon,dropoff_lat,pass_cnt,car_type,year,month,day,day_name,week_of_year,hour,min,sec,qut,distance]
    model=pickle.load(open('model_fp.pkl','rb'))
    prediction=model.predict([feature])[0]
    st.title(f'Your Uber Price for this ride is $:{round(prediction)}/-')
#st.write(pass_cnt,car_type,distance,year,month,day,day_name,week_of_year,hour,min,sec,qut)