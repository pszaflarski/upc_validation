
def check_length(upc_string):
    # data from http://www.gtin.info/

    GTIN_LENGTHS = {
        8: {'gtin_data_structure': 'GTIN-8',
            'legacy_terminology': ['EAN-8'],
            'symbology': ['EAN-8'],
            'use_at_pos': 'Yes'},
        12: {'gtin_data_structure': 'GTIN-12',
             'legacy_terminology': ['UPC', ' UCC-12'],
             'symbology': ['UPC-A', ' UPC-E'],
             'use_at_pos': 'Yes'},
        13: {'gtin_data_structure': 'GTIN-13',
             'legacy_terminology': ['EAN', ' JAN', ' EAN-13'],
             'symbology': ['EAN-13'],
             'use_at_pos': 'Yes'},
        14: {'gtin_data_structure': 'GTIN-14',
             'legacy_terminology': ['EAN / UCC-14',
                                    ' ITF Symbol',
                                    ' SCC-14',
                                    ' DUN-14',
                                    ' UPC Case Code',
                                    ' UPC Shipping Container Code',
                                    ' UCC Code 128',
                                    ' EAN Code 128'],
             'symbology': ['GS1 Databar Family'],
             'use_at_pos': 'Not Yet'}}

    length = len(upc_string)

    r = {
        'valid_length': None,
        'metadata': {
            'code_length':None
        }
    }
    r['metadata']['code_length'] = length

    if length not in GTIN_LENGTHS:
        r['valid_length'] = False
    else:
        r['valid_length'] = True
        r['metadata'].update(GTIN_LENGTHS[length])
    return r


def check_digit(upc_string):
    r = list(reversed(upc_string))

    check_digit = int(r[0])
    sum_digits = r[1:]

    by3 = [3 * int(x) for i, x in enumerate(sum_digits) if i % 2 == 0]
    by1 = [int(x) for i, x in enumerate(sum_digits) if i % 2 == 1]

    summed_total = sum(by3 + by1) + check_digit

    return summed_total % 10 == 0


def is_valid_upc(upc_string):
    upc_string = str(upc_string)

    valid_check_digit = check_digit(upc_string)

    r = {
        'check_digit_valid': valid_check_digit
    }
    r.update(check_length(upc_string))
    is_valid = r['check_digit_valid'] and r['valid_length']

    r.update({'is_valid':is_valid})

    return r


if __name__ == '__main__':
    d = is_valid_upc('796030114976')

    print(d)