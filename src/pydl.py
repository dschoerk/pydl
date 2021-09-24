import wget
from pathlib import Path
from urllib.parse import urlparse
import hashlib

def md5_from_file(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get(url, localpath=None, md5=None):

    url_parsed = urlparse(url)
    filename = Path(url_parsed.path).name
    
    if localpath is None:
        localpath = Path('./' + filename)
    else:
        localpath = Path(localpath)

    if not Path(url).is_file():
        wget.download(url, out = localpath.as_posix())

    if md5 is not None:
        if md5_from_file(localpath.as_posix()) != md5:
            localpath.unlink()
            raise Exception('MD5 checksum for %s does not match' % localpath)

    return localpath