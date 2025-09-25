import { APIGatewayProxyHandler } from 'aws-lambda';
import { DynamoDBClient, ScanCommand } from "@aws-sdk/client-dynamodb";

const client = new DynamoDBClient({});

export const handler: APIGatewayProxyHandler = async () => {
  try {
    const command = new ScanCommand({ TableName: process.env.DDB_TABLE });
    const data = await client.send(command);

    return {
      statusCode: 200,
      body: JSON.stringify({
        alerts: data.Items?.map(item => ({
          userId: item.userId.S,
          name: item.name.S,
          stress_level: item.stress_level.N,
          alert: item.alert.BOOL,
        }))
      }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: (err as Error).message }),
    };
  }
};