import math
from starlette.requests import Request
import traceback
def get_error_mess_in_ex(ex: Exception) -> (str):
    """Get error message in exeption

    Args:
        ex (Exception): Base Exeption

    Returns:
        str: Error
    """
    trace = str(traceback.format_exception(etype=type(ex),value=ex, tb=ex.__traceback__))
    retVal = f"ERROR IN: {trace}".replace("\\n", "\n")
    return retVal

def ss_pagination(query_set=None, request=Request, is_docs=None):
    """Pagination

    Args:
        query_set (queryset, optional): _description_. Defaults to None.
        request (_type_, optional): _description_. Defaults to Request.
        is_docs (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    metadata = None
    if not query_set:
        metadata={
            "valid_page": False,
        }
    try:
        _limit = int(request.query_params.get('limit')) if request.query_params.get(
                'limit') and int(request.query_params.get('limit')) > 0 else 100
        _page = int(request.query_params.get('page')) if request.query_params.get(
                'page') and int(request.query_params.get('page')) > 0 else 1
        _skip = _limit * (_page - 1) if _page > 1 else 0
        if is_docs:
            _count_docs = len(query_set)
            query_set = query_set[_skip: _skip+_limit]
        else:
            _count_docs = query_set.count()    
            query_set = query_set.skip(_skip).limit(_limit)
        _num_pages = _count_docs / _limit if _count_docs / _limit > 1 else 1
        if _skip - _count_docs >= 0:
            metadata = {'msg': 'current page does not exist'} 
            return [], metadata
        _page_range = list(range(1, math.ceil(_num_pages) + 1))
        metadata = {
                "valid_page": True,
                "count": _count_docs,
                "num_pages":  math.ceil(_num_pages),
                "page_range": _page_range,
                "has_next": _page < len(_page_range),
                "has_previous": _page > 1,
                "current_page": _page,
                "next_page_number": _page + 1 if _page < len(_page_range) else None,
                "previous_page_number": _page - 1 if _page > 1 else None
            }
        return query_set, metadata  
    except Exception as e:
        metadata = {
            'valid_page': False,
            'page_number': request.query_params.get('page'),
            'message': f'{e}'
        }
        print(get_error_mess_in_ex(e))
        return [], metadata  