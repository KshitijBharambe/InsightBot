from pinecone import Pinecone as PineconeClient

# Initialize Pinecone client
pinecone_client = PineconeClient(api_key="pcsk_6reuE9_QNTBXM9quQqBZcBtXSMydyBuWMhRfZhpHmdbPH2huGt8H4bv3ATG2SW6zxC2PA3", environment="us-east1-gcp")

# List and delete indexes
indexes_to_delete = [
    "university-recommendations-university",
    "university-recommendations-living-expenses",
    "university-recommendations-employment"
]

for index_name in indexes_to_delete:
    if index_name in pinecone_client.list_indexes():
        pinecone_client.delete_index(index_name)
        print(f"✅ Deleted index: {index_name}")
    else:
        print(f"ℹ️ Index {index_name} does not exist.")

# Verify deletion
remaining_indexes = pinecone_client.list_indexes()
print("Remaining indexes:", remaining_indexes)
