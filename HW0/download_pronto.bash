mkdir pronto
echo "This folder contains the data records from the Pronto bike data collected on 2015." > pronto/README.txt
mkdir pronto/data
cd pronto/data
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv
