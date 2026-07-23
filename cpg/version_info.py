import sys
from pathlib import Path
from cpg.database import session
import hashlib

def info():
    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("This file does not exist")
        return
    
    version_input=int(sys.argv[2])

    query1="""SELECT file_id,latest_version FROM CPG.tracked_files
    WHERE path=%s
    """

    check=session.execute(query1,(file_path,)).one()

    if check:
        file_id=check.file_id
        latest_version=check.latest_version
        if version_input>latest_version:
            print("This version is not present")
            return
        else:
            query2="""SELECT file_id,version_id,commit_time,author
            FROM CPG.versions
            WHERE file_id=%s AND version_id=%s
            """

            version=session.execute(query2,(file_id,version_input,)).one()

            print("File id: ",version.file_id)
            print("Version Number: ",version.version_id)
            print("Commit Time: ",version.commit_time)
            print("Author: ",version.author)
            return
    else:
        print("This file is not being tracked")
        return
