"""List or read tables made available through a Delta Sharing profile."""

from __future__ import annotations

import argparse
from pathlib import Path

import delta_sharing


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="List or read tables from a Delta Sharing profile."
    )
    parser.add_argument(
        "--profile",
        default="config/oauth_config.share",
        help="Path to the local Delta Sharing profile.",
    )
    parser.add_argument(
        "--table",
        metavar="SHARE.SCHEMA.TABLE",
        help="Fully qualified table to retrieve.",
    )
    return parser.parse_args()


def main() -> None:
    arguments = parse_arguments()
    profile = Path(arguments.profile)
    if not profile.is_file():
        raise FileNotFoundError(
            f"Profile not found: {profile}. Copy "
            "config/oauth_config.example.share to config/oauth_config.share "
            "and fill in the values."
        )

    profile_path = str(profile)
    client = delta_sharing.SharingClient(profile_path)

    if arguments.table is None:
        for table in client.list_all_tables():
            print(f"{table.share}.{table.schema}.{table.name}")
        return

    if len(arguments.table.split(".")) != 3:
        raise ValueError("--table must have the form SHARE.SCHEMA.TABLE.")

    table_url = f"{profile_path}#{arguments.table}"
    print(delta_sharing.load_as_pandas(table_url).head())


if __name__ == "__main__":
    main()
