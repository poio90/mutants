import json
import boto3
from datetime import datetime
from mutant import isMutant
from funciones import listasIguales
from boto3.dynamodb.conditions import Key

    
dynamodb = boto3.resource('dynamodb')
table_mutant = dynamodb.Table('mutant')
table_stats = dynamodb.Table('stats')

    
def lambda_handler(event, context):

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    response = {}
    item = None
    
    
    is_mutant = isMutant(event["dna"])
    existe = False

    if is_mutant:
        item = table_stats.get_item(
            Key={'type': 'mutant'},
            AttributesToGet=[
                'count_mutant_dna',
            ],)
        
        count = item['Item'].get('count_mutant_dna') + 1
        
        table_stats.update_item(
            Key={'type': 'mutant'},
            UpdateExpression="set count_mutant_dna = :r",
            ExpressionAttributeValues={
                ':r': count,
            },
            ReturnValues="UPDATED_NEW"
        )
        
        lista = table_mutant.scan(AttributesToGet=['dna'])
        
        # Si no hay registros en la tabla, hace el primer input, si no compara con los que ya existen
        if len(lista['Items']) > 0:
            for i in range(len(lista['Items'])):
                if listasIguales(lista['Items'][i].get('dna'), event["dna"]):
                    existe = True
                    i = len(lista['Items']) - 1
        else:
            existe = False
        
        if not existe:
            table_mutant.put_item(Item={"created-at" : str(timestamp) , "dna" : event["dna"]})
            
        response['statusCode'] = 'HTTP 200-OK'
    else:
        item = table_stats.get_item(
            Key={'type': 'human'},
            AttributesToGet=[
                'count_human_dna',
            ],)
        
        count = item['Item'].get('count_human_dna') + 1
        
        table_stats.update_item(
            Key={'type': 'human'},
            UpdateExpression="set count_human_dna = :r",
            ExpressionAttributeValues={
                ':r': count,
            },
            ReturnValues="UPDATED_NEW"
        )

        response['statusCode'] = '403'
        response['body']= 'Forbidden'
    
        raise Exception(response)  
    return response
