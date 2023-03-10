""" Argument Treatments """

import argparse

from modules.logger_config import initialize_logger


def treat_arguments(software_acronym, software_name, software_version, software_url):
    """ Treats user ontologies arguments. """

    logger = initialize_logger()
    logger.debug("Parsing arguments...")

    about_message = software_acronym + " - version " + software_version

    # PARSING ARGUMENTS
    arguments_parser = argparse.ArgumentParser(prog="ontouml-models-tools",
                                               description=software_acronym + " - " + software_name,
                                               allow_abbrev=False,
                                               epilog=software_url)

    arguments_parser.version = about_message

    # AUTOMATIC ARGUMENT
    arguments_parser.add_argument("-v", "--version", action="version", help="Prints the software version and exit.")

    # POSITIONAL ARGUMENT
    arguments_parser.add_argument("catalog_path", type=str, action="store",
                                  help="The path of the OntoUML/UFO Catalog directory.")

    # Execute arguments parser
    arguments = arguments_parser.parse_args()

    received_arguments = {"catalog_path": arguments.catalog_path}

    logger.debug(f"Arguments Parsed. Obtained values are: {received_arguments}")

    return received_arguments
