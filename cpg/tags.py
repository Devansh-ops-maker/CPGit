import sys
from pathlib import Path
from cpg.database import session

def add_tags():
    file_path=str(Path(sys.argv[1]).resolve())
    
    if not Path(file_path).is_file():
        print("This file does not exist")
        return
    else:
        query1="""SELECT latest_version,file_id FROM CPG.tracked_files
        WHERE path=%s
        """
        
        version_input=int(sys.argv[2])

        check=session.execute(query1,(file_path,)).one()

        if check:

            latest_version=check.latest_version
            file_id=check.file_id
            largs=len(sys.argv) 
            tagstrt=4

            if version_input>latest_version or version_input<=0:
                print("This version does not exist")
                return
            else:
                tags=set()
                query2="""SELECT tags FROM CPG.tags
                WHERE file_id=%s AND version_id=%s
                """
                
                check2=session.execute(query2,(file_id,version_input,)).one()

                if check2:
                    tags=check2.tags
                
                for tagindx in range(tagstrt,largs):
                    tags.add(sys.argv[tagindx])
                
                query3="""UPDATE CPG.tags
                SET tags=%s
                WHERE file_id=%s AND version_id=%s
                """

                session.execute(query3,(tags,file_id,version_input,))

                print("Tags are successfully added to the version")
                return

        else:
            print("Tracking is not enabled for this file")
            return 
        
def display():

    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("This file does not exist")
        return 
    else:

        query1="""SELECT latest_version,file_id FROM CPG.tracked_files
        WHERE path=%s
        """

        check=session.execute(query1,(file_path,)).one()

        if check:
            latest_version=check.latest_version
            version_input=int(sys.argv[2])
            file_id=check.file_id

            if version_input>latest_version or version_input<=0:
                print("This version does not exist")
                return
            else:

                query2="""SELECT tags FROM CPG.tags
                WHERE file_id=%s AND version_id=%s
                """

                check2=session.execute(query2,(file_id,version_input,)).one()

                if check2:
                    tags=check2.tags

                    for tag in tags:
                        print(tag," ")

                    return
                else:
                    print("No tags are present for this version")
                    return
        else:
            print("This file is not being tracked")
            return
def remove():

    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("This file does not exist")
        return
    else:

        query1="""SELECT file_id,latest_version FROM CPG.tracked_files
        WHERE path=%s
        """

        check=session.execute(query1,(file_path,)).one()

        if check:
            file_id=check.file_id
            latest_version=check.latest_version
            version_input=int(sys.argv[2])
            largs=len(sys.argv)
            argsrt=4

            if version_input>latest_version or version_input<=0:
                print("This version does not exist")
                return
            else:
                tags=set()

                query2="""SELECT tags FROM CPG.tags
                WHERE file_id=%s AND version_id=%s
                """

                check2=session.execute(query2,(file_id,version_input,)).one()

                if check2:
                    tags=set(check2.tags)

                    for argindx in range(argsrt,largs):
                        if sys.argv[argindx] in tags:
                            tags.remove(sys.argv[argindx])
                    
                    query3="""UPDATE CPG.tags
                    SET tags=%s
                    WHERE file_id=%s AND version_id=%s
                    """

                    session.execute(query3,(tags,file_id,version_input,))

                    print("Tags updated sucessfully")
                    return
                else:
                    print("Tags are not present for this version")
                    return 
        else:
            print("Tracking is not enabled for this file")
            return 

