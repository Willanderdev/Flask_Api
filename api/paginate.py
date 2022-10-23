from flask import request, url_for

def paginate(model, schema):
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 2))
    page_obj = model.query.paginate(page=page, per_page=per_page)

    next = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page, per_page=per_page, **request.view_args
    )

    prev = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page, per_page=per_page, **request.view_args
    )

    return {
        'total': page_obj.total,
        'pages': page_obj.pages,
        'next': next,
        'prev': prev,

        'results': schema.dump(page_obj.items)
    }


