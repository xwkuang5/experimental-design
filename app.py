import os
import sys
import json
import argparse

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'design')))

from design.core import Design


def main(config_filename, output_filename=None):

    with open(config_filename, 'r') as f:
        config = json.load(f)

    design_instance = Design(config)

    output_config = design_instance.get_experimental_design()

    if output_filename:
        with open(output_filename, 'w') as f:
            print("Writing to {} ...".format(output_filename))
            json.dump(output_config, f)
            print("Done!")
    else:
        print(output_config)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('config', type=str, help='/path/to/config.json')
    parser.add_argument(
        "--out", dest='output_filename', type=str, help='/path/to/output.json')
    args = vars(parser.parse_args())

    main(args['config'], args.get('output_filename', None))
