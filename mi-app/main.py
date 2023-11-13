import json

def pruebacloudbuild(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = open(event['name'])
    data = json.load(file)
    print(f"Processing file: {event['name']}.")
    print(data['emp_details'])
    file.close()