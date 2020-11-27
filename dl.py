import sys
from skillshare import Skillshare

# or by class ID:
# dl.download_course_by_class_id(189505397)

def main():
    dl = Skillshare()
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


def info():
    print(r"""   
         ____  _    _ _ _     _                          ____  _     
        / ___|| | _(_) | |___| |__   __ _ _ __ ___      |  _ \| |    
        \___ \| |/ / | | / __| '_ \ / _` | '__/ _ \_____| | | | |    
         ___) |   <| | | \__ \ | | | (_| | | |  __/_____| |_| | |___ 
        |____/|_|\_\_|_|_|___/_| |_|\__,_|_|  \___|     |____/|_____|  

    """)



if __name__ == "__main__":
    info()
    main()

