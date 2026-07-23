from cpg.help import help
from cpg.master import assist
from cpg.problemHelp import details
from cpg.tags import add_tags,display,remove
from cpg.version_info import info
from cpg.version_open import show,checkout
from cpg.version_save import save
from cpg.versioning_checks import version_check,version_track
from cpg.versioning_control import enable,disable
import sys
def main():
    largs=len(sys.argv)

    if largs<=0:
        print("Command not found")
    else:
        command=str(sys.argv[largs-1])

        if command=='help':
            help()
        elif command=='assist':
            assist()
        elif command=='details':
            details()
        elif command=='add_tags':
            add_tags()
        elif command=='display':
            display()
        elif command=='remove':
            remove()
        elif command=='info':
            info()
        elif command=='show':
            show()
        elif command=='checkout':
            checkout()
        elif command=='save':
            save()
        elif command=='check':
            version_check()
        elif command=='track':
            version_track()
        elif command=='enable':
            enable()
        elif command=='disable':
            disable()
        else:
            print("Command not found")

if __name__=="__main__":
    main()