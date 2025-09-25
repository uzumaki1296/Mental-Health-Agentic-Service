import json
import boto3
import csv
import os
from uuid import uuid4

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DDB_TABLE"])

STRESS_THRESHOLD = 70  # Example threshold

def lambda_handler(event, context):
    try:
        alerts = []
        # load the dataset 
        with open("university_mental_health_iot_dataset.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                stress_level = int(row["stress_level"])
                if stress_level > STRESS_THRESHOLD:
                    alert_item = {
                        "userId": str(uuid4()),
                        "name": row["name"],
                        "stress_level": stress_level,
                        "alert": True
                    }
                    table.put_item(Item=alert_item)
                    alerts.append(alert_item)

        return {
            "statusCode": 200,
            "body": json.dumps({"alerts": alerts})
        }
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
