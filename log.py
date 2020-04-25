#!/usr/bin/env python3
import logging
from logging.config import fileConfig





def main():
    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    logging.info('Started')
    logger.debug('often makes a very good meal of %s', 'visiting tourists')
    print("Running Something...")
    logging.info('Finished')

if __name__ == '__main__':

    [main() for item in list(range(0,1000))]
print("Hello World!")