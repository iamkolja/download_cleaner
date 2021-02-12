import os, datetime, shutil

def content():
        os.chdir("G:/Downloads/")
        for file in os.scandir():
                file_modified = datetime.datetime.fromtimestamp(file.stat().st_mtime)
                if datetime.datetime.now() - file_modified > datetime.timedelta(days=7) and file.name != "Permanent":
                        if file.is_dir():
                                shutil.rmtree(file.path)
                        else:
                                os.remove(file.path)
content()
