import sys
from pathlib import Path
from cpg.database import session
import subprocess

def show():
    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("This file does not exist")
        return 
    else:
        query1="""SELECT file_id,latest_version FROM CPG.tracked_files
        WHERE path=%s
        """

        version_input=int(sys.argv[2])

        check=session.execute(query1,(file_path,)).one()

        if check:
            file_id=check.file_id
            latest_version=check.latest_version

            if version_input<=0 or version_input>latest_version:
                print("This version does not exist")
                return
            else:
                query2="""SELECT hash FROM CPG.versions 
                WHERE file_id=%s AND version_id=%s
                """

                check2=session.execute(query2,(file_id,version_input,)).one()

                hash_value=check2.hash

                parent_dir=Path(file_path).parent
                objects_dir=parent_dir/".cpvcs"/"objects"

                object_file=objects_dir/hash_value

                subprocess.run(["code",str(object_file)])

                print("Successfully opened the requested file")
                return
        else:
            print("This file is not being tracked")
            return
def checkout():
    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("This file does not exist")
        return 
    
    else:
        query1="""SELECT file_id,latest_version FROM CPG.tracked_files
        WHERE path=%s
        """

        version_input=int(sys.argv[2])

        check=session.execute(query1,(file_path,)).one()

        if check:
            file_id=check.file_id
            latest_version=check.latest_version

            if version_input<=0 or version_input>latest_version:
                print("This version does not exist")
                return
            else:
                query2="""SELECT hash FROM CPG.versions 
                WHERE file_id=%s AND version_id=%s
                """

                check2=session.execute(query2,(file_id,version_input,)).one()

                hash_value=check2.hash

                parent_dir=Path(file_path).parent
                objects_dir=parent_dir/".cpvcs"/"objects"

                object_file=objects_dir/hash_value

                with open(object_file,"rb") as f:
                    data=f.read()
                with open(file_path,"wb") as f:
                    f.write(data)
                
                print(f"Successfully Restored Version {version_input}")
                return
        else:
             print("This file is not being tracked")
             return
