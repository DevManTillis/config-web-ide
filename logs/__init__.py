from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from logging.config import fileConfig
import logging
from os.path import dirname, basename, splitext, join, exists
from os import listdir, remove
import gzip
import shutil


class RotatingFileHandler(RotatingFileHandler):
    def __init__(self,
            filename=str(),
            mode=str(),
            maxBytes=int(),
            backupCount=int(),
            encoding=str(),
            delay=False):
        super(RotatingFileHandler, self).__init__(
            filename=filename,
            mode=mode,
            maxBytes=int(maxBytes),
            backupCount=int(backupCount),
            encoding=encoding,
            delay=False
        )

    def doRollover(self):
        super(RotatingFileHandler, self).doRollover()
        log_dir = dirname(self.baseFilename)
        to_compress = [
            join(log_dir, f) for f in listdir(log_dir) if f.startswith(
                basename(splitext(self.baseFilename)[0])
            ) and not f.endswith((".gz", ".log"))
        ]
        for f in to_compress:
            print(f)
            if exists(f):
                with open(f, "rb") as _old, gzip.open(f + ".gz", "wb") as _new:
                    shutil.copyfileobj(_old, _new)
                remove(f)


class TimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename="", when="", interval=int(),
                 backup_count=int()):
        super(TimedRotatingFileHandler, self).__init__(
            filename=filename,
            when=when,
            interval=int(interval),
            backupCount=int(backup_count)
        )
    
    def doRollover(self):
        super(TimedRotatingFileHandler, self).doRollover()
        log_dir = dirname(self.baseFilename)
        to_compress = [
            join(log_dir, f) for f in listdir(log_dir) if f.startswith(
                basename(splitext(self.baseFilename)[0])
            ) and not f.endswith((".gz", ".log"))
        ]
        for f in to_compress:
            if exists(f):
                with open(f, "rb") as _old, gzip.open(f + ".gz", "wb") as _new:
                    shutil.copyfileobj(_old, _new)
                remove(f)