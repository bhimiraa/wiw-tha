'''
TODO 
1. If there was enough time, write some test scripts
'''

try:
    import pandas as pd
    import sys
    import time
    import os
    from string import ascii_lowercase
except ImportError:
    print("Installing dependencies")
    os.system("pip install -r requirements.txt")
    print("Depencies installed successfully")

"""
wiwThaComputeTimeSpentAtEachPath class is used to 
compute total time spent at each path from logs

This performs the following actions
1. Reads data from a URL into a dataframe
2. Creates a comprehensive dataframe combining data 
   under that path
3. Computes time spent by user at each path
4. Pivots the dataframe to massage data in the required format 
"""
class wiwThaComputeTimeSpentAtEachPath():
    # setting class attributes
    def __init__(self, url, result_write_directory_path, debug=False):
        '''
            Initializes class objects with
            1. read_url - url from where we load data into the dataframe
            2. debug - determines if we need to run object in debug mode
            3. result_write_directory_path - path to which we can write result to
        '''
        self.read_url = url
        self.debug = debug
        self.result_write_directory_path = result_write_directory_path

    def __setup_dir(self):
        os.system("mkdir {}".format(self.result_write_directory_path))

    def __readDataFromUrlToDf(self, complete_url):
        '''
        This private function is used to read data from an url and load it 
        into a dataframe

        params
        :param complete_url: path to load data into a dataframe

        :return - returns a dataframe
        ''' 
        df=pd.read_csv(complete_url, engine="python")
        return df

    def __createCompleteDf(self):
        '''
        This private function is used to create a complete dataframe
        from data at individual files under root url
        '''
        completeDf = pd.DataFrame()
        completeRows = 0
        completeColumns = 0
        for c in ascii_lowercase:
            URL = "{}/{}.csv".format(self.read_url,c)
            try:
                df = self.__readDataFromUrlToDf(URL)
            except ConnectionResetError:
                time.sleep(30)
                self.__readDataFromUrlToDf(URL)
            completeDf = completeDf.append(df)
            rows, columns = df.shape
            completeRows+=rows
            if completeColumns != columns:
                if completeColumns != 0:
                    print("Warning: Different number of columns found in dataframe {}.csv".format(c))
                completeColumns+=columns
            print("Completed read of data from file {}.csv".format(c))
        self.completeDf = completeDf
    
    def __computeTimeSpentByUserAtPath(self):
        '''
        This private function is used to compute the total time spent by user
        at each path from complete dataframe computed in method - "__createCompleteDf"
        '''
        sumTimeUserSpentOnPath = self.completeDf.groupby(by=["user_id","path"])["length"].sum().reset_index()
        self.processedDf = pd.DataFrame(sumTimeUserSpentOnPath)

        if self.debug:
            self.processedDf.to_csv("{}/{}.csv".format(self.result_write_directory_path, "before_pivot"))

    def __pivotCompleteDf(self):
        '''
        This private function is used to pivot the processed dataframe from 
        method - "__computeTimeSpentByUserAtPath" above giving the user_id 
        spent at each path
        '''
        pivotedDf = self.processedDf.pivot(index="user_id", columns = "path", values="length")

        pivotedDf.to_csv("{}/{}.csv".format(self.result_write_directory_path, "result"))
    
    def start(self):
        '''
        This method starts the processing operations for this object
        It performs the following functions
        1. Creates a complete DataFrame from the data under the root url
        2. Computes the time spent by user at each path
        3. Pivots the computed dataframe in step 2 to the required format
        '''
        self.__setup_dir()
        self.__createCompleteDf()
        self.__computeTimeSpentByUserAtPath()
        self.__pivotCompleteDf()
    

if __name__=="__main__":
    if len(sys.argv) > 3:
        print('You have specified too many arguments')
        print('Usage - python3 processLogs.py "<path to the result folder>" "<url path>" <debug flag value>')
        sys.exit()

    result_write_directory_path = sys.argv[1]
    url = sys.argv[2]
    debug = sys.argv[3]

    wiwTha = wiwThaComputeTimeSpentAtEachPath(result_write_directory_path=result_write_directory_path, debug=debug, url=url)

    wiwTha.start()
