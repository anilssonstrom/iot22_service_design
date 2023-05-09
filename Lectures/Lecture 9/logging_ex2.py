import logging


# Start by creating a logger object. Then do some basic config of it.
logger = logging.getLogger('backend')
logger.setLevel(logging.INFO)  # Controls the entire loggers lowest level
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Log to console
ch = logging.StreamHandler()
ch.setFormatter(formatter)
ch.setLevel(logging.WARNING)  # WARNING level will only be used if main logger object has at least WARNING level too
logger.addHandler(ch)

# Log to file
fh = logging.FileHandler('ex2.log')
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)  # DEBUG level will only be used if the main logger object has at least DEBUG level too
logger.addHandler(fh)


def buy_groceries():
    logger.debug('Finding cheese')
    logger.info('Buying groceries...')

    n_products = 0

    if n_products < 1:
        raise ValueError("Couldn't find products")

    return n_products  # Number of bought products


def make_pizza():
    logger.info('Making pizza!')


def eat_pizza():
    logger.info('Eating pizza!')


def main():
    logger.info('Starting program')
    logger.warning('Testing warnings')
    logger.critical('Testing critical')

    var1 = 'Look'
    var2 = 'log'
    logger.error(f'{var1} before you {var2}')


    try:
        bought_products = buy_groceries()
    except ValueError as e:
        # logging.error(e)
        logger.exception(e)
        return

    # if bought_products < 1:
    #    logging.error('No groceries to make pizza with!')

    make_pizza()
    eat_pizza()


if __name__ == '__main__':
    main()
