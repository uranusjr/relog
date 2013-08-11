from django.core.paginator import Paginator, InvalidPage, EmptyPage


def paginate(objs, current_page_num, objs_per_page, max_page_num=10):
    """
    Return a paginated page for objs. Inspired from Mezzanine's paginating
    paradigm.
    """
    paginator = Paginator(objs, objs_per_page)
    try:
        page = paginator.page(current_page_num)
    except (EmptyPage, InvalidPage):
        page = paginator.page(paginator.num_pages)
    page_range = page.paginator.page_range
    if len(page_range) > max_page_num:
        start = min(page.paginator.num_pages - max_page_num,
                    max(0, current_page_num - max_page_num // 2 - 1))
        end = start + max_page_num
        page_range = page_range[start:end]
    page.visible_page_range = page_range
    return page
