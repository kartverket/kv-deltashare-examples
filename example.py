import delta_sharing

SOURCE_PATH = "config.share"
sharing_client = delta_sharing.SharingClient(SOURCE_PATH)

tables = []
try:
    tables = sharing_client.list_all_tables()
except Exception as e:
    print(e)
    print("Sharen har ikke tilgang til noen tabeller")
    raise SystemExit(1)


for table in tables:
    print(table.name)


schema_name = "gold"
share_name = f"kartverket_matrikkelen_utlevering_med_fødselsnummer_v1_dev"
table_name = "dim_fylke"


table_url = f"{SOURCE_PATH}#{share_name}.{schema_name}.{table_name}"

##metadata = delta_sharing.get_table_metadata(table_url)
##print(metadata)

data = delta_sharing.load_as_pandas(table_url)
print(data.head())

#historical_changes = delta_sharing.load_table_changes_as_pandas(
#    table_url, 
#    starting_version=0, 
#    ending_version=1

#print(historical_changes[['_commit_version', '_commit_timestamp', '_change_type']])

#print(historical_changes.head())
