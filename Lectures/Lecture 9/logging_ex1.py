import logging


logging.basicConfig(
    filename='mylogfile.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def buy_groceries():
    logging.debug('Finding cheese')
    logging.info('Buying groceries...')

    n_products = 0

    if n_products < 1:
        raise ValueError("Couldn't find products")

    return n_products  # Antalet varor vi köpt


def make_pizza():
    logging.info('Making pizza!')


def eat_pizza():
    logging.info('Eating pizza!')


def main():
    try:
        bought_products = buy_groceries()
    except ValueError as e:
        # logging.error(e)
        logging.exception(e)
        return

    # if bought_products < 1:
    #    logging.error('No groceries to make pizza with!')

    make_pizza()
    eat_pizza()


if __name__ == '__main__':
    main()
