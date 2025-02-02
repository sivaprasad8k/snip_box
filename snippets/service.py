import pandas as pd
from django.db.models import F
from core.exceptions import DataFetchFailedException
from snippets.models import Snippet


def format_data(data):
    """Method to format data using pandas"""
    df = pd.DataFrame(list(data))
    df['created_at'] = df['created_at'].dt.strftime('%b %d %Y %I:%M %p')
    if 'updated_at' in df.columns:
        df['updated_at'] = df['updated_at'].apply(lambda x: x.strftime('%b %d %Y %I:%M %p') if pd.notnull(x) else x)

    result = df.to_dict(orient='records')

    return result


def get_snippet_data(filter_condition):
    """Method for getting snippet data based on filter condition passed"""
    result = Snippet.objects
    if filter_condition:
        result = result.filter(**filter_condition)
    result = result.values('id', 'note', 'created_at', 'tag_id', 'updated_at', created=F('created_by__username'),
                           title=F('tag__title'))
    if not result:
        raise DataFetchFailedException
    result = format_data(result)

    return result
