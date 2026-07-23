from pathlib import Path
import sys
from cpg.database import session
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("GEMINI_API_KEY")

client=genai.Client(api_key=API_KEY)

def assist():

    file_path=str(Path(sys.argv[1]).resolve())

    if not Path(file_path).is_file():
        print("This file does not exist")
        return
    else:
        query1="""SELECT latest_version,file_id
        FROM CPG.tracked_files
        WHERE path=%s
        """

        check=session.execute(query1,(file_path,)).one()

        if check:
            version_input=int(sys.argv[2])
            latest_version=check.latest_version
            file_id=check.file_id

            if version_input>latest_version:
                print("This version does not exist")
                return
            else:
                query2="""SELECT hash FROM CPG.versions
                WHERE file_id=%s AND version_id=%s
                """

                check2=session.execute(query2,(file_id,version_input,)).one()

                if check2 is None:
                    print("Version not found")
                    return
                else:

                    hash_value=check2.hash

                    parent_dir=Path(file_path).parent

                    objects_dir=parent_dir/".cpvcs"/"objects"

                    objects_file=objects_dir/hash_value

                    if not objects_file.exists():
                        print("The version object file is missing")
                        return
                    
                    else:
                        with open(objects_file,"r",encoding="utf-8") as f:
                            code=f.read()

                        response = client.models.generate_content(
                        model="gemini-flash-latest",
                        contents=code,
                        config=types.GenerateContentConfig(
                            system_instruction="""
                        You are a command-line assistant for competitive programming.

                        The input is the source code of a competitive programming solution.

                        Your task:
                        - Identify logical mistakes, syntax errors, runtime issues, edge cases, or implementation flaws.
                        - Do not rewrite the code.
                        - Give concise numbered points.
                        - Return at most 5 points.
                        - If no obvious issues are found, reply exactly:
                        1. No obvious mistakes detected.
                        """
                        )
                        )

                        print(response.text)
                        return
        else:
            print("This file is not being tracked")
            return