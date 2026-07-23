import sys
import uuid
from pathlib import Path
from cpg.database import session
def enable():
    file_path=str(Path(sys.argv[1]).resolve())
    if not Path(file_path).is_file():
         print("File does not exist")
         return
    query1="""SELECT tracking_enabled FROM tracked_files
       WHERE path=%s
    """
    check=session.execute(query1,(file_path,)).one()

    if check:
            if check.tracking_enabled:
              print("Versioning is already enabled for this file")
              return 
            else:
                 query2="""UPDATE CPG.tracked_files
                 SET tracking_enabled=%s
                 WHERE path=%s
                 """
                 session.execute(query2,(True,file_path,))
                 print("Versioning enabled successfully")
                 return 
    else:
         file_uuid=uuid.uuid4()
         query3="""INSERT INTO CPG.tracked_files
         (file_id,path,tracking_enabled,latest_version) 
         VALUES (%s,%s,%s,%s)
         """
         session.execute(query3,(file_uuid,file_path,True,0))
         print("Versioning enabled successfully")
         return
def disable():
     file_path=str(Path(sys.argv[1]).resolve())
     if not Path(file_path).is_file():
          print("File does not exist")
          return 
     query1="""SELECT tracking_enabled FROM tracked_files
     WHERE path=%s
     """

     check=session.execute(query1,(file_path,)).one()

     if check:
          if check.tracking_enabled:
               query2="""UPDATE CPG.tracked_files
               SET tracking_enabled=%s
               WHERE path=%s
               """
               session.execute(query2,(False,file_path,))
               print("Versioning disabled successfully")
               return
          else:
               print("Versioning is already disabled for this file")
               return
     else:
          print("This file is not being tracked")
          return

        




