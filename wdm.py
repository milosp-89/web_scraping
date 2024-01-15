def wdm():
    """
    1. Description: function to donwload, unzip and store content of the file within specific path
    3. Parameters: None
    3. Returns: None
    4. Output: store downloaded and uziped webdriver.exe file within "C:\\Users\\Public\\driver\\wdriver\\" path
    """
    # modules/libraries:
    import os, requests, zipfile
    # main variables:
    url = "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.71/win64/chromedriver-win64.zip"
    fn = url.split("/")[-1]
    loc = f"C:\\Users\\Public\\driver\\wdriver\\{fn}"
    files_to_del = [fn, "chromedriver.exe"]
    # check and delete all files within a path:
    try: [os.remove(x) for x in files_to_del]
    except: pass
    # donwload a .zip file:
    response = requests.get(url)
    with open(loc, "wb") as f:
        f.write(response.content)
    # unzip a .zip file and store the webdriver.exe:
    with zipfile.ZipFile(loc,"r") as to_zip:
        loc2 = "\\".join(loc.split("\\")[0:-1])
        to_zip.extractall(loc2, 
                          members = [files_to_del[1]])
    print("Script executed!")

if __name__ == "__main__":
    wdm()