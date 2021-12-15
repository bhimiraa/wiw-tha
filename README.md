## Instructions to Setup and Run program

### Clone repo

`git clone https://github.com/bhimiraa/wiw-tha.git`

### Change directory into "wiw-tha"

`cd wiw-tha`

### Make runCompute.sh file as a executable

`chmod +x runCompute.sh`

### At the root folder execute the following command

`./runCompute.sh "<path to result directory>" "<source url for data>" "<value of debug flag>"`

`Note: "path to result directory" only takes in one folder at present and it resides in the root directory`


### If the program runs successfully then you will find result and before_pivot(if debug flag is set to true) csv files under result_path_directory
before_pivot - processed file with user data before pivot and final tranformation in required format
result - file processed in the required format
