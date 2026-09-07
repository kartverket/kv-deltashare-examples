"""Print the metadata for a shared table.

Usage: uv run examples/show_metadata_for_shared_table.py SHARE.SCHEMA.TABLE
"""

import argparse

import delta_sharing


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--table", required=True, metavar="SHARE.SCHEMA.TABLE")
    parser.add_argument("--profile", default="config/oauth_config.share")
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    table_url = f"{arguments.profile}#{arguments.table}"
    print(delta_sharing.get_table_metadata(table_url))


if __name__ == "__main__":
    main()
