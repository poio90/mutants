import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_stats = dynamodb.Table('stats')

def lambda_handler(event, context):
    
    response = {}
    ratio = 0
    
    items = table_stats.scan(AttributesToGet=['count_mutant_dna','count_human_dna'])
    
    humans = items['Items'][0].get('count_human_dna')
    mutants = items['Items'][1].get('count_mutant_dna')
    
    if humans > 0:
        ratio = mutants / humans
        
    
    response['count_mutant_dna'] = mutants
    response['count_human_dna'] = humans
    response['ratio'] = ratio
    
    return response