import argparse
from core import banner


class Args:
    """Class to handle the arguments"""

    def get_args():
        """Parse all the arguments!"""

        # the base argument parser
        parser = argparse.ArgumentParser(
            prog="Bluffy",
            description=banner.brrr(),
            formatter_class=argparse.RawDescriptionHelpFormatter,
            add_help=True,
        )

        # Bin to read
        parser.add_argument(
            "-b", "--bin", help="Specify bin file to load", metavar="", required=True
        ),

        # File to output to
        parser.add_argument(
            "-o",
            "--output",
            help="Specify file to output too",
            metavar="",
            required=True,
        ),

        # Always required, but the choices[] param is needed too
        parser.add_argument(
            "-m",
            "--mask",
            help="Specify the mask for the shellcode",
            choices=["svg", "css", "uuid", "clsid"],
            metavar="",
            required=True,
        )

        # parse all the flags
        args = parser.parse_args()

        # handle what happens if nothing is passed
        if not any(vars(args).values()):
            # if nothing is passed, print the help
            parser.print_help()
            quit()
        else:
            return args