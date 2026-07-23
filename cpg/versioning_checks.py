import sys
from pathlib import Path
from cpg.database import session

def version_check():
    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("File does not exist")
        return
    else:
        query1="""SELECT tracking_enabled FROM CPG.tracked_files
        WHERE path=%s
        """

        check=session.execute(query1,(file_path,)).one()

        if check:
            if check.tracking_enabled:
                print("Versioning is enabled for this file")
                return 
            else:
                print("Versioning is disabled for this file")
                return
        else:
            print("This file is not being tracked")
            return
def version_track():
    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("File does not exist")
        return
    else:
        query1="""SELECT latest_version FROM CPG.tracked_files
        WHERE path=%s
        """

        check=session.execute(query1,(file_path,)).one()

        if check:
            if check.latest_version ==0:
                print("There are no versions for this file")
                return
            else:
                print("The latest version of the file is ",check.latest_version)
                return
        else:
            print("This file is not being tracked")
            return