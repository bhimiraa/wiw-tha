import sys
from lib.wiwAssignmentDataProcessing import wiwThaComputeTimeSpentAtEachPath
import sys

def main():
    if len(sys.argv) > 4:
        print('You have specified too many arguments')
        print('Usage - python3 processLogs.py "<path to the result directory>" "<url path>" <debug flag>')
        sys.exit()

    result_write_directory_path = sys.argv[1]
    url = sys.argv[2]
    debug = sys.argv[3]

    if debug == "True":
        debug = True
    else:
        debug = False

    wiwTha = wiwThaComputeTimeSpentAtEachPath(result_write_directory_path=result_write_directory_path, url=url, debug=debug)

    wiwTha.start()

main()