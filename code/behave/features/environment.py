import os

def before_all(context):
    context.configstring = os.environ.get('key','default strng from befor all')
