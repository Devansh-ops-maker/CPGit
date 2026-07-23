import sys
from pathlib import Path
from cpg.database import session
import hashlib
from datetime import datetime

def save():
    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("The file does not exist")
        return
    query1="""SELECT tracking_enabled,file_id,latest_version FROM CPG.tracked_files
    WHERE path=%s
    """
    check=session.execute(query1,(file_path,)).one()

    if check:
        if check.tracking_enabled:
            with open(Path(file_path),"rb") as f:
                data=f.read()
            hash_value=hashlib.sha256(data).hexdigest()
            file_id=check.file_id

            query2="""SELECT hash FROM CPG.versions
            WHERE file_id=%s
            """

            versions=session.execute(query2,(file_id,))
            flag=True
            for version in versions:
                if version.hash==hash_value:
                    flag=False
                    break
            if flag:
                new_version=check.latest_version+1
                current_time=datetime.now()

                query3="""UPDATE CPG.tracked_files
                SET latest_version=%s
                WHERE path=%s
                """

                session.execute(query3,(new_version,file_path,))

                query4="""INSERT INTO CPG.versions
                (file_id,version_id,commit_time,author,hash)
                VALUES (%s,%s,%s,%s,%s)
                """

                session.execute(query4,(file_id,new_version,current_time,"Devansh",hash_value)) # author is hardcoded for now

                project_dir=Path(file_path).parent
                objects_dir=project_dir/".cpvcs"/"objects"

                objects_dir.mkdir(parents=True,exist_ok=True)

                object_file=objects_dir/hash_value

                with open(object_file,"wb") as f:
                    f.write(data)

                print("Version created successfully")
                return
            else:
                print("No changes in the file are detected")
                return

            
        else:
            print("Versioning is currently disabled for this file")
            return
    else:
        print("This file is not being tracked")
        return
    