#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##################################################
#  _   __      _   _               _             #
# | | / /     | | | |             (_)            #
# | |/ /  __ _| |_| |__   ___ _ __ _ _ __   ___  #
# |    \ / _` | __| '_ \ / _ \ '__| | '_ \ / _ \ #
# | |\  \ (_| | |_| | | |  __/ |  | | | | |  __/ #
# \_| \_/\__,_|\__|_| |_|\___|_|  |_|_| |_|\___| #
#                                                #
# General Video Game AI                          #
# Copyright (C) 2020-2021 d33are                 #
##################################################


from kat_framework import parsers, KatherineApplication
from argparse import Namespace


def main(args: Namespace, enable_logo: bool = True) -> None:
    """
    Application entry point.

    :param enable_logo:
        enables the logo in the configured log handlers
    :param args:
        parsed CLI arguments for the framework
    """
    KatherineApplication.run(args.factory_class, args.config_class, args.config_uri, enable_logo)


if __name__ == "__main__":
    main(parsers.parse_cli_args(), True)
